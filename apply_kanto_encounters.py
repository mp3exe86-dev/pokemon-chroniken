#!/usr/bin/env python3
"""
Clean Kanto encounter redistribution. Only valid species. Auto-deduplicates.
"""
import json, re
from collections import Counter, OrderedDict

with open("/tmp/valid_species.txt") as f:
    VALID = set(l.strip() for l in f if l.strip())

ROAMERS = {'RAIKOU','ENTEI','LATIAS'}
LEGENDARIES = {'ARTICUNO','ZAPDOS','MOLTRES','MEWTWO','MEW','SUICUNE','HO_OH','LUGIA',
               'REGIROCK','REGICE','REGISTEEL','LATIOS','KYOGRE','GROUDON','RAYQUAZA',
               'CELEBI','JIRACHI','DEOXYS'}
POOL = sorted(VALID - ROAMERS - LEGENDARIES)

# ── 32 AREAS, no intended cross-area species duplicates ──────────────────────
# (auto-dedup handles any residual conflicts)
AREAS = OrderedDict([
    ("Route2", {  # Baby/Fairy/Normal lv3-7
        "maps": ["MAP_ROUTE2"], "rate": 12,
        "mons": [(4,"PIDGEY"),(4,"RATTATA"),(5,"NIDORAN_F"),(5,"NIDORAN_M"),
                 (5,"CLEFAIRY"),(5,"JIGGLYPUFF"),(6,"IGGLYBUFF"),(6,"CLEFFA"),
                 (6,"TOGEPI"),(6,"TOGETIC"),(7,"SNUBBULL"),(7,"GRANBULL")],
    }),
    ("ViridianForest", {  # Bug lv3-8
        "maps": ["MAP_VIRIDIAN_FOREST"], "rate": 15,
        "mons": [(4,"CATERPIE"),(4,"WEEDLE"),(5,"METAPOD"),(5,"KAKUNA"),
                 (5,"BUTTERFREE"),(5,"BEEDRILL"),(5,"PIKACHU"),(6,"LEDYBA"),
                 (6,"SPINARAK"),(6,"WURMPLE"),(7,"SILCOON"),(7,"CASCOON")],
    }),
    ("Route3", {  # Normal/Poison lv6-10
        "maps": ["MAP_ROUTE3"], "rate": 12,
        "mons": [(6,"SPEAROW"),(7,"EKANS"),(7,"SANDSHREW"),(7,"MEOWTH"),
                 (8,"MANKEY"),(8,"SENTRET"),(8,"HOOTHOOT"),(9,"AIPOM"),
                 (9,"SMEARGLE"),(9,"LOTAD"),(10,"LOMBRE"),(10,"STANTLER")],
    }),
    ("Route22", {  # Nidoran/Normal lv4-10
        "maps": ["MAP_ROUTE22"], "rate": 12,
        "mons": [(4,"NIDORINA"),(4,"NIDORINO"),(5,"RATICATE"),(5,"ARBOK"),
                 (6,"SANDSLASH"),(6,"PERSIAN"),(7,"PIDGEOTTO"),(7,"PRIMEAPE"),
                 (8,"POOCHYENA"),(8,"MIGHTYENA"),(9,"SUDOWOODO"),(9,"AZUMARILL")],
    }),
    ("MtMoon", {  # Cave/Rock lv8-12
        "maps": ["MAP_MT_MOON_1F","MAP_MT_MOON_B1F","MAP_MT_MOON_B2F"],
        "rate": 10,
        "mons": [(8,"ZUBAT"),(8,"GEODUDE"),(9,"PARAS"),(9,"CLEFABLE"),
                 (10,"GOLBAT"),(10,"GRAVELER"),(11,"PARASECT"),(11,"WIGGLYTUFF"),
                 (11,"NOSEPASS"),(12,"ARON"),(12,"LAIRON"),(12,"AGGRON")],
    }),
    ("Route4", {  # Grass east Cerulean lv12-16
        "maps": ["MAP_ROUTE4"], "rate": 12,
        "mons": [(12,"ODDISH"),(12,"BELLSPROUT"),(13,"HOPPIP"),(13,"SKIPLOOM"),
                 (14,"JUMPLUFF"),(14,"SUNKERN"),(14,"SUNFLORA"),(15,"ROSELIA"),
                 (15,"SHROOMISH"),(15,"BRELOOM"),(16,"SEEDOT"),(16,"NIDOKING")],
    }),
    ("Route5", {  # Grass/Fire Celadon lv13-18
        "maps": ["MAP_ROUTE5"], "rate": 12,
        "mons": [(13,"GLOOM"),(13,"WEEPINBELL"),(14,"VILEPLUME"),(14,"VICTREEBEL"),
                 (15,"VULPIX"),(15,"GROWLITHE"),(16,"NINETALES"),(16,"ARCANINE"),
                 (17,"TANGELA"),(17,"PONYTA"),(18,"RAPIDASH"),(18,"BELLOSSOM")],
    }),
    ("Route6", {  # Psychic Vermilion lv14-19
        "maps": ["MAP_ROUTE6"], "rate": 12,
        "mons": [(14,"DROWZEE"),(14,"ABRA"),(15,"JYNX"),(15,"KADABRA"),
                 (16,"HYPNO"),(16,"SLOWPOKE"),(17,"SLOWBRO"),(17,"SLOWKING"),
                 (18,"MR_MIME"),(18,"ALAKAZAM"),(19,"SMOOCHUM"),(19,"GIRAFARIG")],
    }),
    ("Route7", {  # Eevee/Bug Celadon lv17-21
        "maps": ["MAP_ROUTE7"], "rate": 12,
        "mons": [(17,"EEVEE"),(17,"FLAREON"),(17,"VAPOREON"),(18,"JOLTEON"),
                 (18,"ESPEON"),(18,"UMBREON"),(19,"SKITTY"),(19,"DELCATTY"),
                 (20,"NATU"),(20,"XATU"),(21,"VOLBEAT"),(21,"ILLUMISE")],
    }),
    ("Route8", {  # Electric/Fire Lavender lv17-22
        "maps": ["MAP_ROUTE8"], "rate": 12,
        "mons": [(17,"PICHU"),(17,"RAICHU"),(18,"VOLTORB"),(18,"MAGNEMITE"),
                 (19,"ELECTRODE"),(19,"MAGNETON"),(20,"ELECTABUZZ"),(20,"FLAAFFY"),
                 (21,"AMPHAROS"),(21,"ELEKID"),(22,"MAGBY"),(22,"ELECTRIKE")],
    }),
    ("RockTunnel", {  # Rock/Fighting lv16-21
        "maps": ["MAP_ROCK_TUNNEL_1F","MAP_ROCK_TUNNEL_B1F"],
        "rate": 10,
        "mons": [(16,"MACHOP"),(16,"ONIX"),(17,"RHYHORN"),(17,"MACHOKE"),
                 (18,"RHYDON"),(18,"MACHAMP"),(19,"STEELIX"),(19,"LARVITAR"),
                 (20,"PUPITAR"),(20,"MAWILE"),(21,"LILEEP"),(21,"CRADILY")],
    }),
    ("Route9", {  # Bug/Water north Cerulean lv20-25
        "maps": ["MAP_ROUTE9"], "rate": 12,
        "mons": [(20,"VENONAT"),(20,"VENOMOTH"),(21,"PSYDUCK"),(21,"GOLDUCK"),
                 (22,"PLUSLE"),(22,"MINUN"),(23,"MANECTRIC"),(23,"MAREEP"),
                 (24,"WOOPER"),(24,"QUAGSIRE"),(25,"MARILL"),(25,"AZURILL")],
    }),
    ("Route10", {  # Ground/Rock Power Plant lv22-27
        "maps": ["MAP_ROUTE10"], "rate": 12,
        "mons": [(22,"CUBONE"),(22,"MAROWAK"),(23,"DIGLETT"),(23,"DUGTRIO"),
                 (24,"TRAPINCH"),(24,"VIBRAVA"),(25,"FLYGON"),(25,"GOLEM"),
                 (26,"PHANPY"),(26,"DONPHAN"),(27,"SLUGMA"),(27,"MAGCARGO")],
    }),
    ("Route11", {  # Flying east Vermilion lv21-26
        "maps": ["MAP_ROUTE11"], "rate": 12,
        "mons": [(21,"FARFETCHD"),(21,"DODUO"),(22,"DODRIO"),(22,"TAILLOW"),
                 (23,"SWELLOW"),(23,"WINGULL"),(24,"PELIPPER"),(24,"SWABLU"),
                 (25,"ALTARIA"),(25,"NOCTOWL"),(26,"PIDGEOT"),(26,"FEAROW")],
    }),
    ("Route12", {  # Bug/Grass south lv23-28
        "maps": ["MAP_ROUTE12"], "rate": 12,
        "mons": [(23,"SCYTHER"),(23,"PINSIR"),(24,"HERACROSS"),(24,"LEDIAN"),
                 (25,"ARIADOS"),(25,"BEAUTIFLY"),(26,"DUSTOX"),(26,"SURSKIT"),
                 (27,"MASQUERAIN"),(27,"YANMA"),(28,"NINCADA"),(28,"NINJASK")],
    }),
    ("Route13", {  # Normal/Exotic Fuchsia north lv24-29
        "maps": ["MAP_ROUTE13"], "rate": 12,
        "mons": [(24,"DITTO"),(24,"LICKITUNG"),(25,"KANGASKHAN"),(25,"TAUROS"),
                 (26,"MILTANK"),(26,"DUNSPARCE"),(27,"ZANGOOSE"),(27,"SEVIPER"),
                 (28,"SPINDA"),(28,"TORKOAL"),(29,"KECLEON"),(29,"TROPIUS")],
    }),
    ("Route14", {  # Poison/Dark Fuchsia west lv25-30
        "maps": ["MAP_ROUTE14"], "rate": 12,
        "mons": [(25,"KOFFING"),(25,"WEEZING"),(26,"GRIMER"),(26,"MUK"),
                 (27,"GULPIN"),(27,"SWALOT"),(28,"NUMEL"),(28,"CAMERUPT"),
                 (29,"CACNEA"),(29,"CACTURNE"),(30,"SHIFTRY"),(30,"WHISMUR")],
    }),
    ("Route15", {  # Normal Fuchsia east lv25-30
        "maps": ["MAP_ROUTE15"], "rate": 12,
        "mons": [(25,"SNORLAX"),(25,"TEDDIURSA"),(26,"URSARING"),(26,"FURRET"),
                 (27,"LINOONE"),(27,"ZIGZAGOON"),(28,"VIGOROTH"),(28,"SLAKOTH"),
                 (29,"SLAKING"),(29,"LOUDRED"),(30,"EXPLOUD"),(30,"PORYGON")],
    }),
    ("Route16", {  # Dark/Flying Celadon west lv26-31
        "maps": ["MAP_ROUTE16"], "rate": 12,
        "mons": [(26,"MURKROW"),(26,"HOUNDOUR"),(27,"HOUNDOOM"),(27,"ABSOL"),
                 (28,"SNEASEL"),(28,"DELIBIRD"),(29,"SKARMORY"),(29,"NUZLEAF"),
                 (30,"MEDITITE"),(30,"MEDICHAM"),(31,"SPOINK"),(31,"GRUMPIG")],
    }),
    ("Route17", {  # Dragon/Flying Cycling Road lv30-35 + Rayquaza
        "maps": ["MAP_ROUTE17"], "rate": 12,
        "mons": [(30,"BAGON"),(30,"SHELGON"),(31,"SALAMENCE"),(31,"DRATINI"),
                 (32,"DRAGONAIR"),(32,"DRAGONITE"),(33,"AERODACTYL"),(33,"GYARADOS"),
                 (34,"TREECKO"),(34,"GROVYLE"),(35,"SCEPTILE"),(50,"RAYQUAZA")],
    }),
    ("Route18", {  # Ground/Misc south lv27-32
        "maps": ["MAP_ROUTE18"], "rate": 12,
        "mons": [(27,"BARBOACH"),(27,"WHISCASH"),(28,"GLIGAR"),(28,"FORRETRESS"),
                 (29,"PINECO"),(29,"BALTOY"),(30,"CLAYDOL"),(30,"SOLROCK"),
                 (31,"LUNATONE"),(31,"CASTFORM"),(32,"SHUCKLE"),(32,"ANORITH")],
    }),
    ("Route23", {  # Starter evos pre-VR lv35-41
        "maps": ["MAP_ROUTE23"], "rate": 12,
        "mons": [(35,"VENUSAUR"),(35,"CHARIZARD"),(36,"BLASTOISE"),(36,"MEGANIUM"),
                 (37,"TYPHLOSION"),(37,"FERALIGATR"),(38,"IVYSAUR"),(38,"CHARMELEON"),
                 (39,"WARTORTLE"),(39,"BAYLEEF"),(40,"QUILAVA"),(40,"CROCONAW")],
    }),
    ("Route24", {  # Water/Ice Cerulean north lv12-16 + 2 legs
        "maps": ["MAP_ROUTE24"], "rate": 12,
        "mons": [(12,"HORSEA"),(12,"SEADRA"),(13,"KINGDRA"),(13,"LAPRAS"),
                 (14,"SEEL"),(14,"DEWGONG"),(15,"SHELLDER"),(15,"CLOYSTER"),
                 (16,"POLIWAG"),(16,"POLIWHIRL"),(50,"REGICE"),(50,"LATIOS")],
    }),
    ("Route25", {  # Water starters + 4 legs lv12-15
        "maps": ["MAP_ROUTE25"], "rate": 12,
        "mons": [(12,"BULBASAUR"),(12,"CHARMANDER"),(13,"SQUIRTLE"),(13,"CHIKORITA"),
                 (14,"CYNDAQUIL"),(14,"TOTODILE"),(50,"REGISTEEL"),(50,"JIRACHI"),
                 (15,"MUDKIP"),(15,"TORCHIC"),(50,"CELEBI"),(50,"DEOXYS")],
    }),
    ("Route21North", {  # Sea route lv25-30
        "maps": ["MAP_ROUTE21_NORTH"], "rate": 12,
        "mons": [(25,"TENTACOOL"),(25,"TENTACRUEL"),(26,"CORSOLA"),(26,"LUVDISC"),
                 (27,"REMORAID"),(27,"OCTILLERY"),(28,"MANTINE"),(28,"QWILFISH"),
                 (29,"CLAMPERL"),(29,"HUNTAIL"),(30,"GOREBYSS"),(30,"RELICANTH")],
    }),
    ("Route21South", {  # Sea route south lv28-33
        "maps": ["MAP_ROUTE21_SOUTH"], "rate": 12,
        "mons": [(28,"STARYU"),(28,"STARMIE"),(29,"WAILMER"),(29,"WAILORD"),
                 (30,"CHINCHOU"),(30,"LANTURN"),(31,"CORPHISH"),(31,"CRAWDAUNT"),
                 (32,"CARVANHA"),(32,"SHARPEDO"),(33,"FEEBAS"),(33,"MILOTIC")],
    }),
    ("PokemonTower", {  # Ghost lv25-30 + Moltres
        "maps": ["MAP_POKEMON_TOWER_3F","MAP_POKEMON_TOWER_4F","MAP_POKEMON_TOWER_5F",
                 "MAP_POKEMON_TOWER_6F","MAP_POKEMON_TOWER_7F"],
        "rate": 10,
        "mons": [(25,"GASTLY"),(25,"HAUNTER"),(26,"GENGAR"),(26,"SHUPPET"),
                 (27,"BANETTE"),(27,"DUSKULL"),(28,"DUSCLOPS"),(28,"SABLEYE"),
                 (29,"MISDREAVUS"),(29,"CHIMECHO"),(30,"SHEDINJA"),(50,"MOLTRES")],
    }),
    ("PowerPlant", {  # Steel/Fighting/Psychic lv30-35 + Zapdos
        "maps": ["MAP_POWER_PLANT"], "rate": 10,
        "mons": [(30,"BELDUM"),(30,"METANG"),(31,"METAGROSS"),(31,"RALTS"),
                 (32,"KIRLIA"),(32,"GARDEVOIR"),(33,"MAKUHITA"),(33,"HARIYAMA"),
                 (34,"TYROGUE"),(34,"HITMONLEE"),(35,"HITMONCHAN"),(50,"ZAPDOS")],
    }),
    ("SafariZone", {  # Fossil/Rare lv25-30
        "maps": ["MAP_SAFARI_ZONE_CENTER","MAP_SAFARI_ZONE_EAST",
                 "MAP_SAFARI_ZONE_NORTH","MAP_SAFARI_ZONE_WEST"],
        "rate": 12,
        "mons": [(25,"KRABBY"),(25,"KINGLER"),(26,"GOLDEEN"),(26,"SEAKING"),
                 (27,"KABUTO"),(27,"KABUTOPS"),(28,"OMANYTE"),(28,"OMASTAR"),
                 (29,"ARMALDO"),(29,"CHANSEY"),(30,"POLITOED"),(30,"POLIWRATH")],
    }),
    ("Seafoam", {  # Ice/Sea lv35-50 + 3 legs
        "maps": ["MAP_SEAFOAM_ISLANDS_1F","MAP_SEAFOAM_ISLANDS_B1F",
                 "MAP_SEAFOAM_ISLANDS_B2F","MAP_SEAFOAM_ISLANDS_B3F",
                 "MAP_SEAFOAM_ISLANDS_B4F"],
        "rate": 10,
        "mons": [(35,"SWINUB"),(35,"PILOSWINE"),(36,"SNORUNT"),(36,"GLALIE"),
                 (37,"SEALEO"),(37,"WALREIN"),(38,"SPHEAL"),(38,"MAGIKARP"),
                 (39,"WOBBUFFET"),(50,"KYOGRE"),(50,"ARTICUNO"),(50,"LUGIA")],
    }),
    ("VictoryRoad", {  # Strong cave lv40-50 + 2 legs
        "maps": ["MAP_VICTORY_ROAD_1F","MAP_VICTORY_ROAD_2F","MAP_VICTORY_ROAD_3F"],
        "rate": 10,
        "mons": [(40,"CROBAT"),(40,"TYRANITAR"),(41,"WYNAUT"),(41,"HITMONTOP"),
                 (42,"PORYGON2"),(42,"SWAMPERT"),(43,"MARSHTOMP"),(43,"NIDOQUEEN"),
                 (44,"COMBUSKEN"),(44,"BLAZIKEN"),(50,"REGIROCK"),(50,"GROUDON")],
    }),
    ("CeruleanCave", {  # Endgame lv55-70 + Mew + Mewtwo
        # ~4 species are accepted duplicates (pool exhausted): WOBBUFFET, WYNAUT, DRAGONAIR, DRAGONITE
        "maps": ["MAP_CERULEAN_CAVE_1F","MAP_CERULEAN_CAVE_2F","MAP_CERULEAN_CAVE_B1F"],
        "rate": 10,
        "mons": [(55,"PORYGON2"),(55,"BLISSEY"),(56,"LUDICOLO"),(56,"SCIZOR"),
                 (57,"MAGMAR"),(57,"NIDOQUEEN"),(58,"WOBBUFFET"),(58,"WYNAUT"),
                 (59,"DRAGONAIR"),(59,"DRAGONITE"),(70,"MEW"),(70,"MEWTWO")],
    }),
])

# ── VALIDATE SPECIES ──────────────────────────────────────────────────────────
bad = [(sp, aname) for aname, adata in AREAS.items()
       for lv, sp in adata["mons"] if sp not in VALID]
if bad:
    for sp, a in bad: print(f"INVALID: {sp} in {a}")
    exit(1)

# ── AUTO-DEDUPLICATE ──────────────────────────────────────────────────────────
assignments = [[aname, i, lv, sp]
               for aname, adata in AREAS.items()
               for i, (lv, sp) in enumerate(adata["mons"])]

used = set()
for e in assignments:
    sp = e[3]
    if sp in LEGENDARIES: used.add(sp); continue
    if sp not in used: used.add(sp)
    else: e[3] = None  # mark duplicate

rep_pool = [sp for sp in POOL if sp not in (used - LEGENDARIES)]
n_replace = sum(1 for e in assignments if e[3] is None)
print(f"Slots to replace: {n_replace},  Pool available: {len(rep_pool)}")
if n_replace > len(rep_pool):
    print("ERROR: not enough replacement species!")

ri = 0
for e in assignments:
    if e[3] is None:
        if ri < len(rep_pool):
            e[3] = rep_pool[ri]; ri += 1
        else:
            # No more unique species; find the original by re-scanning
            aname, idx = e[0], e[1]
            e[3] = AREAS[aname]["mons"][idx][1]  # restore original (accepts duplicate)

for aname, i, lv, sp in assignments:
    AREAS[aname]["mons"][i] = (lv, sp)

# ── REPORT ────────────────────────────────────────────────────────────────────
all_mons = [(sp, aname) for aname, adata in AREAS.items() for lv, sp in adata["mons"]]
counts = Counter(sp for sp, _ in all_mons)
dupes = {sp: c for sp, c in counts.items() if c > 1}
print(f"Total: {len(all_mons)}, Unique: {len(counts)}, Residual dupes: {len(dupes)}")
for sp, c in sorted(dupes.items()):
    print(f"  {sp}: {c}x → {[a for s,a in all_mons if s==sp]}")

# ── APPLY ─────────────────────────────────────────────────────────────────────
with open("/tmp/wild_encounters_original.json") as f:
    data = json.load(f)
entries = data["wild_encounter_groups"][0]["encounters"]
map_to_idx = {}
for i, e in enumerate(entries):
    map_to_idx.setdefault(e["map"], []).append(i)

changed = 0
for aname, adata in AREAS.items():
    new_mons = [{"min_level": lv, "max_level": lv, "species": f"SPECIES_{sp}"}
                for lv, sp in adata["mons"]]
    for map_id in adata["maps"]:
        for idx in map_to_idx.get(map_id, []):
            e = entries[idx]
            if e.get("land_mons") is None:
                e["land_mons"] = {"encounter_rate": adata["rate"], "mons": new_mons}
            else:
                e["land_mons"]["encounter_rate"] = adata["rate"]
                e["land_mons"]["mons"] = new_mons
            changed += 1

print(f"Changed {changed} entries")
with open("src/data/wild_encounters.json", "w") as f:
    json.dump(data, f, indent=4)
    f.write("\n")
print("Done.")
