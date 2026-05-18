#include "global.h"
#include "random.h"
#include "overworld.h"
#include "field_specials.h"
#include "constants/maps.h"
#include "constants/region_map_sections.h"
#include "constants/species.h"

// Alle Wanderer laufen immer in Kartengruppe 3 (TownsAndRoutes)
#define ROAMER_MAP_GROUP 3

// Anzahl gleichzeitiger Wanderer: Raikou (0), Entei (1), Latias (2)
#define NUM_ROAMERS 3

enum
{
    MAP_GRP,
    MAP_NUM,
};

// Wanderer 0 (Raikou)  → gSaveBlock1Ptr->roamer
// Wanderer 1 (Entei)   → gSaveBlock1Ptr->extraRoamers[0]
// Wanderer 2 (Latias)  → gSaveBlock1Ptr->extraRoamers[1]
static struct Roamer *GetRoamerByIndex(u8 idx)
{
    if (idx == 0)
        return &gSaveBlock1Ptr->roamer;
    return &gSaveBlock1Ptr->extraRoamers[idx - 1];
}

// Feste Arten und Stufen für die drei Wanderer
static const u16 sRoamerSpecies[NUM_ROAMERS] = { SPECIES_RAIKOU, SPECIES_ENTEI, SPECIES_LATIAS };
static const u8  sRoamerLevels [NUM_ROAMERS] = { 50, 50, 50 };

// EWRAM: Aktuelle Position jedes Wanderers
EWRAM_DATA u8 sRoamerLocation[NUM_ROAMERS][2] = {};
// EWRAM: Die letzten 3 Orte des Spielers (gemeinsam, da der Spieler nur einen Ort hat)
EWRAM_DATA u8 sLocationHistory[3][2] = {};
// EWRAM: Welcher Wanderer gerade im Kampf ist (Index 0-2)
EWRAM_DATA u8 sActiveRoamerIndex = 0;

#define ___ MAP_NUM(MAP_UNDEFINED)

// Verbindungstabelle der Routen (identisch zum Original, gilt für alle Wanderer)
static const u8 sRoamerLocations[][7] = {
    {MAP_NUM(MAP_ROUTE1),        MAP_NUM(MAP_ROUTE2),         MAP_NUM(MAP_ROUTE21_NORTH), MAP_NUM(MAP_ROUTE22), ___, ___, ___},
    {MAP_NUM(MAP_ROUTE2),        MAP_NUM(MAP_ROUTE1),         MAP_NUM(MAP_ROUTE3),        MAP_NUM(MAP_ROUTE22), ___, ___, ___},
    {MAP_NUM(MAP_ROUTE3),        MAP_NUM(MAP_ROUTE2),         MAP_NUM(MAP_ROUTE4),        ___, ___, ___, ___},
    {MAP_NUM(MAP_ROUTE4),        MAP_NUM(MAP_ROUTE3),         MAP_NUM(MAP_ROUTE5),        MAP_NUM(MAP_ROUTE9),  MAP_NUM(MAP_ROUTE24), ___, ___},
    {MAP_NUM(MAP_ROUTE5),        MAP_NUM(MAP_ROUTE4),         MAP_NUM(MAP_ROUTE6),        MAP_NUM(MAP_ROUTE7),  MAP_NUM(MAP_ROUTE8),  MAP_NUM(MAP_ROUTE9), MAP_NUM(MAP_ROUTE24)},
    {MAP_NUM(MAP_ROUTE6),        MAP_NUM(MAP_ROUTE5),         MAP_NUM(MAP_ROUTE7),        MAP_NUM(MAP_ROUTE8),  MAP_NUM(MAP_ROUTE11), ___, ___},
    {MAP_NUM(MAP_ROUTE7),        MAP_NUM(MAP_ROUTE5),         MAP_NUM(MAP_ROUTE6),        MAP_NUM(MAP_ROUTE8),  MAP_NUM(MAP_ROUTE16), ___, ___},
    {MAP_NUM(MAP_ROUTE8),        MAP_NUM(MAP_ROUTE5),         MAP_NUM(MAP_ROUTE6),        MAP_NUM(MAP_ROUTE7),  MAP_NUM(MAP_ROUTE10), MAP_NUM(MAP_ROUTE12), ___},
    {MAP_NUM(MAP_ROUTE9),        MAP_NUM(MAP_ROUTE4),         MAP_NUM(MAP_ROUTE5),        MAP_NUM(MAP_ROUTE10), MAP_NUM(MAP_ROUTE24), ___, ___},
    {MAP_NUM(MAP_ROUTE10),       MAP_NUM(MAP_ROUTE8),         MAP_NUM(MAP_ROUTE9),        MAP_NUM(MAP_ROUTE12), ___, ___, ___},
    {MAP_NUM(MAP_ROUTE11),       MAP_NUM(MAP_ROUTE6),         MAP_NUM(MAP_ROUTE12),       ___, ___, ___, ___},
    {MAP_NUM(MAP_ROUTE12),       MAP_NUM(MAP_ROUTE10),        MAP_NUM(MAP_ROUTE11),       MAP_NUM(MAP_ROUTE13), ___, ___, ___},
    {MAP_NUM(MAP_ROUTE13),       MAP_NUM(MAP_ROUTE12),        MAP_NUM(MAP_ROUTE14),       ___, ___, ___, ___},
    {MAP_NUM(MAP_ROUTE14),       MAP_NUM(MAP_ROUTE13),        MAP_NUM(MAP_ROUTE15),       ___, ___, ___, ___},
    {MAP_NUM(MAP_ROUTE15),       MAP_NUM(MAP_ROUTE14),        MAP_NUM(MAP_ROUTE18),       MAP_NUM(MAP_ROUTE19), ___, ___, ___},
    {MAP_NUM(MAP_ROUTE16),       MAP_NUM(MAP_ROUTE7),         MAP_NUM(MAP_ROUTE17),       ___, ___, ___, ___},
    {MAP_NUM(MAP_ROUTE17),       MAP_NUM(MAP_ROUTE16),        MAP_NUM(MAP_ROUTE18),       ___, ___, ___, ___},
    {MAP_NUM(MAP_ROUTE18),       MAP_NUM(MAP_ROUTE15),        MAP_NUM(MAP_ROUTE17),       MAP_NUM(MAP_ROUTE19), ___, ___, ___},
    {MAP_NUM(MAP_ROUTE19),       MAP_NUM(MAP_ROUTE15),        MAP_NUM(MAP_ROUTE18),       MAP_NUM(MAP_ROUTE20), ___, ___, ___},
    {MAP_NUM(MAP_ROUTE20),       MAP_NUM(MAP_ROUTE19),        MAP_NUM(MAP_ROUTE21_NORTH), ___, ___, ___, ___},
    {MAP_NUM(MAP_ROUTE21_NORTH), MAP_NUM(MAP_ROUTE1),         MAP_NUM(MAP_ROUTE20),       ___, ___, ___, ___},
    {MAP_NUM(MAP_ROUTE22),       MAP_NUM(MAP_ROUTE1),         MAP_NUM(MAP_ROUTE2),        MAP_NUM(MAP_ROUTE23), ___, ___, ___},
    {MAP_NUM(MAP_ROUTE23),       MAP_NUM(MAP_ROUTE22),        MAP_NUM(MAP_ROUTE2),        ___, ___, ___, ___},
    {MAP_NUM(MAP_ROUTE24),       MAP_NUM(MAP_ROUTE4),         MAP_NUM(MAP_ROUTE5),        MAP_NUM(MAP_ROUTE9),  ___, ___, ___},
    {MAP_NUM(MAP_ROUTE25),       MAP_NUM(MAP_ROUTE24),        MAP_NUM(MAP_ROUTE9),        ___, ___, ___, ___},
    {___, ___, ___, ___, ___, ___, ___}
};

#undef ___
#define NUM_LOCATION_SETS      (ARRAY_COUNT(sRoamerLocations) - 1)
#define NUM_LOCATIONS_PER_SET  (ARRAY_COUNT(sRoamerLocations[0]))

// ── Hilfsfunktionen ───────────────────────────────────────────────────────────

static void CreateSingleRoamerMon(u8 idx)
{
    struct Pokemon *mon = &gEnemyParty[0];
    struct Roamer *roamer = GetRoamerByIndex(idx);
    u16 species = sRoamerSpecies[idx];
    u8  level   = sRoamerLevels[idx];

    CreateMon(mon, species, level, USE_RANDOM_IVS, FALSE, 0, OT_ID_PLAYER_ID, 0);
    roamer->species     = species;
    roamer->level       = level;
    roamer->status      = 0;
    roamer->active      = TRUE;
    roamer->ivs         = GetMonData(mon, MON_DATA_IVS);
    roamer->personality = GetMonData(mon, MON_DATA_PERSONALITY);
    roamer->hp          = GetMonData(mon, MON_DATA_MAX_HP);
    roamer->cool        = GetMonData(mon, MON_DATA_COOL);
    roamer->beauty      = GetMonData(mon, MON_DATA_BEAUTY);
    roamer->cute        = GetMonData(mon, MON_DATA_CUTE);
    roamer->smart       = GetMonData(mon, MON_DATA_SMART);
    roamer->tough       = GetMonData(mon, MON_DATA_TOUGH);

    sRoamerLocation[idx][MAP_GRP] = ROAMER_MAP_GROUP;
    sRoamerLocation[idx][MAP_NUM] = sRoamerLocations[Random() % NUM_LOCATION_SETS][0];
}

static void MoveRoamerToOtherLocationSet(u8 idx)
{
    u8 mapNum = 0;
    struct Roamer *roamer = GetRoamerByIndex(idx);
    if (!roamer->active)
        return;
    sRoamerLocation[idx][MAP_GRP] = ROAMER_MAP_GROUP;
    while (1)
    {
        mapNum = sRoamerLocations[Random() % NUM_LOCATION_SETS][0];
        if (sRoamerLocation[idx][MAP_NUM] != mapNum)
        {
            sRoamerLocation[idx][MAP_NUM] = mapNum;
            return;
        }
    }
}

static void MoveSingleRoamer(u8 idx)
{
    u8 locSet = 0;
    struct Roamer *roamer = GetRoamerByIndex(idx);

    if ((Random() % 16) == 0)
    {
        MoveRoamerToOtherLocationSet(idx);
    }
    else
    {
        if (!roamer->active)
            return;
        while (locSet < NUM_LOCATION_SETS)
        {
            if (sRoamerLocation[idx][MAP_NUM] == sRoamerLocations[locSet][0])
            {
                u8 mapNum;
                while (1)
                {
                    mapNum = sRoamerLocations[locSet][(Random() % (NUM_LOCATIONS_PER_SET - 1)) + 1];
                    if (!(sLocationHistory[2][MAP_GRP] == ROAMER_MAP_GROUP
                       && sLocationHistory[2][MAP_NUM] == mapNum)
                       && mapNum != MAP_NUM(MAP_UNDEFINED))
                        break;
                }
                sRoamerLocation[idx][MAP_NUM] = mapNum;
                return;
            }
            locSet++;
        }
    }
}

// ── Öffentliche API ───────────────────────────────────────────────────────────

void ClearRoamerData(void)
{
    u32 i, j;
    gSaveBlock1Ptr->roamer = (struct Roamer){};
    for (i = 0; i < 2; i++)
        gSaveBlock1Ptr->extraRoamers[i] = (struct Roamer){};
    for (i = 0; i < NUM_ROAMERS; i++)
    {
        sRoamerLocation[i][MAP_GRP] = 0;
        sRoamerLocation[i][MAP_NUM] = 0;
    }
    for (i = 0; i < ARRAY_COUNT(sLocationHistory); i++)
    {
        sLocationHistory[i][MAP_GRP] = 0;
        sLocationHistory[i][MAP_NUM] = 0;
    }
    sActiveRoamerIndex = 0;
}

void InitRoamer(void)
{
    u8 i;
    ClearRoamerData();
    for (i = 0; i < NUM_ROAMERS; i++)
        CreateSingleRoamerMon(i);
}

void UpdateLocationHistoryForRoamer(void)
{
    sLocationHistory[2][MAP_GRP] = sLocationHistory[1][MAP_GRP];
    sLocationHistory[2][MAP_NUM] = sLocationHistory[1][MAP_NUM];
    sLocationHistory[1][MAP_GRP] = sLocationHistory[0][MAP_GRP];
    sLocationHistory[1][MAP_NUM] = sLocationHistory[0][MAP_NUM];
    sLocationHistory[0][MAP_GRP] = gSaveBlock1Ptr->location.mapGroup;
    sLocationHistory[0][MAP_NUM] = gSaveBlock1Ptr->location.mapNum;
}

void RoamerMoveToOtherLocationSet(void)
{
    // Bewegt nur den aktiven Wanderer (nach Kampf/Flucht)
    MoveRoamerToOtherLocationSet(sActiveRoamerIndex);
}

void RoamerMove(void)
{
    u8 i;
    for (i = 0; i < NUM_ROAMERS; i++)
        MoveSingleRoamer(i);
}

bool8 IsRoamerAt(u8 mapGroup, u8 mapNum)
{
    u8 i;
    for (i = 0; i < NUM_ROAMERS; i++)
    {
        struct Roamer *roamer = GetRoamerByIndex(i);
        if (roamer->active
            && mapGroup == sRoamerLocation[i][MAP_GRP]
            && mapNum   == sRoamerLocation[i][MAP_NUM])
        {
            sActiveRoamerIndex = i;
            return TRUE;
        }
    }
    return FALSE;
}

void CreateRoamerMonInstance(void)
{
    u32 status;
    struct Roamer *roamer = GetRoamerByIndex(sActiveRoamerIndex);
    struct Pokemon *mon = &gEnemyParty[0];
    ZeroEnemyPartyMons();
    CreateMonWithIVsPersonality(mon, roamer->species, roamer->level, roamer->ivs, roamer->personality);
#ifdef BUGFIX
    status = roamer->status;
    SetMonData(mon, MON_DATA_STATUS, &status);
#else
    SetMonData(mon, MON_DATA_STATUS, &roamer->status);
#endif
    SetMonData(mon, MON_DATA_HP,     &roamer->hp);
    SetMonData(mon, MON_DATA_COOL,   &roamer->cool);
    SetMonData(mon, MON_DATA_BEAUTY, &roamer->beauty);
    SetMonData(mon, MON_DATA_CUTE,   &roamer->cute);
    SetMonData(mon, MON_DATA_SMART,  &roamer->smart);
    SetMonData(mon, MON_DATA_TOUGH,  &roamer->tough);
}

bool8 TryStartRoamerEncounter(void)
{
    if (IsRoamerAt(gSaveBlock1Ptr->location.mapGroup, gSaveBlock1Ptr->location.mapNum) == TRUE && (Random() % 4) == 0)
    {
        CreateRoamerMonInstance();
        return TRUE;
    }
    return FALSE;
}

void UpdateRoamerHPStatus(struct Pokemon *mon)
{
    struct Roamer *roamer = GetRoamerByIndex(sActiveRoamerIndex);
    roamer->hp     = GetMonData(mon, MON_DATA_HP);
    roamer->status = GetMonData(mon, MON_DATA_STATUS);
    MoveRoamerToOtherLocationSet(sActiveRoamerIndex);
}

void SetRoamerInactive(void)
{
    GetRoamerByIndex(sActiveRoamerIndex)->active = FALSE;
}

void GetRoamerLocation(u8 *mapGroup, u8 *mapNum)
{
    // Gibt die Position des ersten aktiven Wanderers zurück (Raikou)
    *mapGroup = sRoamerLocation[0][MAP_GRP];
    *mapNum   = sRoamerLocation[0][MAP_NUM];
}

u16 GetRoamerLocationMapSectionId(void)
{
    u8 i;
    for (i = 0; i < NUM_ROAMERS; i++)
    {
        struct Roamer *roamer = GetRoamerByIndex(i);
        if (roamer->active)
            return Overworld_GetMapHeaderByGroupAndId(
                sRoamerLocation[i][MAP_GRP],
                sRoamerLocation[i][MAP_NUM])->regionMapSectionId;
    }
    return MAPSEC_NONE;
}

struct Roamer *GetActiveRoamer(void)
{
    return GetRoamerByIndex(sActiveRoamerIndex);
}
