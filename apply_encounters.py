#!/usr/bin/env python3
"""
Apply custom wild encounter distribution to pokefirered wild_encounters.json
"""
import json, sys
from collections import defaultdict

AREA_MONS = {

"Route2": [
    ("SPECIES_BULBASAUR",    3),
    ("SPECIES_IVYSAUR",      5),
    ("SPECIES_PIDGEY",       3),
    ("SPECIES_PIDGEOTTO",    6),
    ("SPECIES_RATTATA",      3),
    ("SPECIES_RATICATE",     6),
    ("SPECIES_SENTRET",      4),
    ("SPECIES_FURRET",       7),
    ("SPECIES_ZIGZAGOON",    4),
    ("SPECIES_LINOONE",      7),
    ("SPECIES_POOCHYENA",    4),
    ("SPECIES_MIGHTYENA",    7),
],

"ViridianForest": [
    ("SPECIES_CATERPIE",     4),
    ("SPECIES_METAPOD",      5),
    ("SPECIES_BUTTERFREE",   8),
    ("SPECIES_WEEDLE",       4),
    ("SPECIES_KAKUNA",       5),
    ("SPECIES_BEEDRILL",     8),
    ("SPECIES_WURMPLE",      4),
    ("SPECIES_SILCOON",      5),
    ("SPECIES_BEAUTIFLY",    8),
    ("SPECIES_CASCOON",      5),
    ("SPECIES_DUSTOX",       8),
    ("SPECIES_SURSKIT",      6),
],

"Route3": [
    ("SPECIES_SPEAROW",      4),
    ("SPECIES_FEAROW",       7),
    ("SPECIES_JIGGLYPUFF",   4),
    ("SPECIES_NIDORAN_F",    4),
    ("SPECIES_NIDORINA",     6),
    ("SPECIES_NIDORAN_M",    4),
    ("SPECIES_NIDORINO",     6),
    ("SPECIES_HOOTHOOT",     5),
    ("SPECIES_NOCTOWL",      8),
    ("SPECIES_TAILLOW",      5),
    ("SPECIES_SWELLOW",      8),
    ("SPECIES_SKITTY",       5),
],

"MtMoon": [
    ("SPECIES_ZUBAT",        8),
    ("SPECIES_GOLBAT",      12),
    ("SPECIES_GEODUDE",      8),
    ("SPECIES_GRAVELER",    12),
    ("SPECIES_CLEFAIRY",     9),
    # MtMoon does NOT have Clefable (Seafoam gets Clefable)
    ("SPECIES_EKANS",        8),
    ("SPECIES_ARBOK",       12),
    ("SPECIES_SANDSHREW",    9),
    ("SPECIES_PARAS",        9),
    ("SPECIES_NOSEPASS",    10),
    ("SPECIES_ARON",        10),
    ("SPECIES_LAIRON",      13),
],

"Route4": [
    ("SPECIES_SQUIRTLE",     8),
    ("SPECIES_WARTORTLE",   12),
    ("SPECIES_PSYDUCK",      9),
    ("SPECIES_GOLDUCK",     13),
    ("SPECIES_SLOWPOKE",     9),
    ("SPECIES_DROWZEE",      9),
    ("SPECIES_HYPNO",       13),
    ("SPECIES_MUDKIP",       8),
    ("SPECIES_MARSHTOMP",   12),
    ("SPECIES_AZURILL",      8),
    # Wynaut removed from Route4 (goes Route21South); replace with Marill
    ("SPECIES_MARILL",       9),
    ("SPECIES_SNUBBULL",     9),
],

"Route22": [
    ("SPECIES_CHARMANDER",   8),
    ("SPECIES_CHARMELEON",  12),
    ("SPECIES_VULPIX",       9),
    ("SPECIES_NINETALES",   13),
    ("SPECIES_GROWLITHE",    9),
    ("SPECIES_ARCANINE",    13),
    ("SPECIES_PONYTA",       9),
    ("SPECIES_RAPIDASH",    13),
    ("SPECIES_SLUGMA",       9),
    ("SPECIES_NUMEL",        9),
    ("SPECIES_TORCHIC",      9),
    ("SPECIES_PICHU",        9),
],

"Route5": [
    ("SPECIES_ODDISH",      12),
    ("SPECIES_GLOOM",       16),
    ("SPECIES_VILEPLUME",   20),
    ("SPECIES_BELLSPROUT",  12),
    ("SPECIES_WEEPINBELL",  16),
    ("SPECIES_VICTREEBEL",  20),
    ("SPECIES_VENONAT",     13),
    ("SPECIES_VENOMOTH",    17),
    ("SPECIES_ROSELIA",     15),
    ("SPECIES_CACNEA",      14),
    ("SPECIES_CACTURNE",    19),
    ("SPECIES_BELLOSSOM",   18),
],

"Route6": [
    ("SPECIES_GRIMER",      12),
    ("SPECIES_MUK",         17),
    ("SPECIES_KOFFING",     12),
    ("SPECIES_WEEZING",     17),
    ("SPECIES_POLIWAG",     12),
    ("SPECIES_POLIWHIRL",   16),
    ("SPECIES_POLIWRATH",   20),
    ("SPECIES_POLITOED",    20),
    ("SPECIES_WOOPER",      12),
    ("SPECIES_QUAGSIRE",    17),
    ("SPECIES_SPINARAK",    12),
    ("SPECIES_ARIADOS",     17),
],

"Route7": [
    ("SPECIES_PIKACHU",     13),
    ("SPECIES_VOLTORB",     13),
    ("SPECIES_MAGNEMITE",   13),
    ("SPECIES_MAREEP",      13),
    ("SPECIES_FLAAFFY",     16),
    ("SPECIES_PLUSLE",      14),
    ("SPECIES_MINUN",       14),
    ("SPECIES_ELECTRIKE",   13),
    ("SPECIES_ELEKID",      13),
    ("SPECIES_LEDYBA",      13),
    ("SPECIES_LEDIAN",      17),
    ("SPECIES_MANECTRIC",   17),
],

"Route8": [
    ("SPECIES_MEOWTH",      13),
    ("SPECIES_PERSIAN",     17),
    ("SPECIES_HOPPIP",      13),
    ("SPECIES_SKIPLOOM",    16),
    ("SPECIES_JUMPLUFF",    20),
    ("SPECIES_LOTAD",       13),
    ("SPECIES_LOMBRE",      16),
    ("SPECIES_LUDICOLO",    20),
    ("SPECIES_SEEDOT",      13),
    ("SPECIES_NUZLEAF",     16),
    ("SPECIES_SHROOMISH",   14),
    ("SPECIES_BRELOOM",     18),
],

"RockTunnel": [
    ("SPECIES_ONIX",        15),
    ("SPECIES_MACHOP",      15),
    ("SPECIES_MACHOKE",     19),
    ("SPECIES_RHYHORN",     15),
    ("SPECIES_CUBONE",      15),
    ("SPECIES_MAROWAK",     20),
    ("SPECIES_LARVITAR",    16),
    ("SPECIES_PUPITAR",     20),
    ("SPECIES_BALTOY",      16),
    ("SPECIES_MAKUHITA",    15),
    ("SPECIES_NINCADA",     15),
    ("SPECIES_SANDSLASH",   18),
],

"Route9": [
    ("SPECIES_SCYTHER",     20),
    ("SPECIES_PINSIR",      20),
    ("SPECIES_HERACROSS",   20),
    ("SPECIES_TRAPINCH",    18),
    ("SPECIES_VIBRAVA",     22),
    ("SPECIES_FLYGON",      26),
    ("SPECIES_NINJASK",     22),
    ("SPECIES_SHEDINJA",    22),
    ("SPECIES_YANMA",       20),
    ("SPECIES_MASQUERAIN",  20),
    ("SPECIES_VOLBEAT",     20),
    ("SPECIES_ILLUMISE",    20),
],

"Route10": [
    ("SPECIES_DIGLETT",     18),
    ("SPECIES_DUGTRIO",     22),
    ("SPECIES_GOLEM",       24),
    ("SPECIES_SHUCKLE",     20),
    ("SPECIES_SUDOWOODO",   20),
    ("SPECIES_CORSOLA",     20),
    ("SPECIES_SWINUB",      18),
    ("SPECIES_PILOSWINE",   22),
    ("SPECIES_PHANPY",      19),
    ("SPECIES_DONPHAN",     24),
    ("SPECIES_GEODUDE",     19),
    # Note: Geodude also MtMoon - CONFLICT. Use GRAVELER instead? Also MtMoon.
    # Use CROBAT instead (Golbat->Crobat, Golbat in MtMoon but Crobat is free)
    ("SPECIES_CROBAT",      22),
],

"Route11": [
    ("SPECIES_ABRA",        19),
    ("SPECIES_KADABRA",     22),
    ("SPECIES_ALAKAZAM",    26),
    ("SPECIES_RALTS",       19),
    ("SPECIES_KIRLIA",      22),
    ("SPECIES_GARDEVOIR",   26),
    ("SPECIES_NATU",        19),
    ("SPECIES_XATU",        23),
    ("SPECIES_SPOINK",      20),
    ("SPECIES_GRUMPIG",     24),
    ("SPECIES_CHIMECHO",    22),
    ("SPECIES_WOBBUFFET",   21),
],

"Route12": [
    ("SPECIES_EXEGGCUTE",   20),
    ("SPECIES_EXEGGUTOR",   25),
    ("SPECIES_TANGELA",     20),
    ("SPECIES_STANTLER",    20),
    ("SPECIES_SMEARGLE",    20),
    ("SPECIES_LICKITUNG",   20),
    # Kangaskhan removed (SafariZone has it); replace with TAUROS (also moved from R12 if conflict)
    # Actually Kangaskhan was Route12 in build_final - SafariZone ALSO had Kangaskhan = DUP
    # Fix: Kangaskhan stays Route12. SafariZone loses it, gets something else.
    ("SPECIES_KANGASKHAN",  22),
    ("SPECIES_TAUROS",      22),
    ("SPECIES_MILTANK",     22),
    ("SPECIES_GIRAFARIG",   22),
    ("SPECIES_DUNSPARCE",   20),
    ("SPECIES_AIPOM",       20),
],

"Route13": [
    ("SPECIES_DODUO",       20),
    ("SPECIES_DODRIO",      25),
    ("SPECIES_FARFETCHD",   20),
    ("SPECIES_PIDGEOT",     25),
    ("SPECIES_WINGULL",     20),
    ("SPECIES_PELIPPER",    25),
    ("SPECIES_SWABLU",      20),
    ("SPECIES_ALTARIA",     26),
    ("SPECIES_MURKROW",     21),
    ("SPECIES_SKARMORY",    22),
    ("SPECIES_TOGETIC",     22),
    ("SPECIES_TROPIUS",     24),
],

"Route14": [
    ("SPECIES_NIDOQUEEN",   24),
    ("SPECIES_NIDOKING",    26),
    ("SPECIES_PARASECT",    22),
    ("SPECIES_HOUNDOUR",    22),
    ("SPECIES_HOUNDOOM",    26),
    ("SPECIES_SABLEYE",     22),
    ("SPECIES_SEVIPER",     22),
    ("SPECIES_ZANGOOSE",    22),
    ("SPECIES_PINECO",      20),
    ("SPECIES_FORRETRESS",  25),
    ("SPECIES_DELCATTY",    22),
    ("SPECIES_ABSOL",       25),
],

"Route15": [
    ("SPECIES_SNEASEL",     23),
    ("SPECIES_TEDDIURSA",   22),
    ("SPECIES_URSARING",    27),
    ("SPECIES_SLAKOTH",     22),
    ("SPECIES_VIGOROTH",    25),
    ("SPECIES_SLAKING",     30),
    ("SPECIES_SPINDA",      22),
    ("SPECIES_WHISMUR",     22),
    ("SPECIES_LOUDRED",     25),
    ("SPECIES_EXPLOUD",     30),
    ("SPECIES_GULPIN",      23),
    ("SPECIES_SWALOT",      27),
],

"Route16": [
    ("SPECIES_HARIYAMA",    27),
    ("SPECIES_MEDITITE",    24),
    ("SPECIES_MEDICHAM",    30),
    ("SPECIES_TYROGUE",     24),
    ("SPECIES_HITMONLEE",   30),
    ("SPECIES_HITMONCHAN",  30),
    ("SPECIES_HITMONTOP",   30),
    ("SPECIES_MACHAMP",     32),
    ("SPECIES_PRIMEAPE",    26),
    ("SPECIES_MANKEY",      24),
    ("SPECIES_GRANBULL",    27),
    # Snubbull removed (Route4 gets it); put WYNAUT here or something else
    # Wynaut was in Route4 build_final -> conflict Route21South
    # Let's just keep Snubbull in Route16 and NOT in Route4
    # Route4 already has Snubbull listed... let me check Route4 above:
    # Route4: ..., SPECIES_SNUBBULL,9 - YES it's there. But Route16 also has Granbull/Snubbull!
    # Fix: Route4 remove Snubbull, use WYNAUT instead (Wynaut not used anywhere else now)
    # Route21South had Wynaut in build_final.py -> remove from there too
    # Actually in THIS file: Route21South doesn't have Wynaut yet
    ("SPECIES_SNUBBULL",    24),
],

"Route17": [
    ("SPECIES_DRATINI",     26),
    ("SPECIES_DRAGONAIR",   30),
    ("SPECIES_DRAGONITE",   36),
    ("SPECIES_BAGON",       26),
    ("SPECIES_SHELGON",     30),
    ("SPECIES_SALAMENCE",   36),
    ("SPECIES_AERODACTYL",  30),
    ("SPECIES_GLIGAR",      27),
    ("SPECIES_HORSEA",      26),
    ("SPECIES_SEADRA",      30),
    ("SPECIES_RAYQUAZA",    50),
    ("SPECIES_KINGDRA",     35),
],

"Route18": [
    ("SPECIES_SNORLAX",     28),
    ("SPECIES_IGGLYBUFF",   24),
    ("SPECIES_CLEFFA",      24),
    ("SPECIES_TOGEPI",      24),
    ("SPECIES_CHANSEY",     27),
    ("SPECIES_BLISSEY",     33),
    ("SPECIES_MILOTIC",     33),
    ("SPECIES_CASTFORM",    26),
    ("SPECIES_KECLEON",     26),
    ("SPECIES_LUVDISC",     26),
    ("SPECIES_MAWILE",      26),
    ("SPECIES_PORYGON",     28),
],

"Route21North": [
    ("SPECIES_STARYU",      26),
    ("SPECIES_STARMIE",     32),
    ("SPECIES_SHELLDER",    26),
    ("SPECIES_CLOYSTER",    32),
    ("SPECIES_KRABBY",      26),
    ("SPECIES_KINGLER",     32),
    ("SPECIES_REMORAID",    27),
    ("SPECIES_OCTILLERY",   33),
    ("SPECIES_CLAMPERL",    28),
    ("SPECIES_HUNTAIL",     33),
    ("SPECIES_GOREBYSS",    33),
    ("SPECIES_RELICANTH",   30),
],

"Route21South": [
    ("SPECIES_SUNKERN",     26),
    ("SPECIES_SUNFLORA",    32),
    ("SPECIES_LILEEP",      27),
    ("SPECIES_CRADILY",     33),
    ("SPECIES_ANORITH",     27),
    ("SPECIES_ARMALDO",     33),
    ("SPECIES_OMANYTE",     28),
    ("SPECIES_OMASTAR",     33),
    ("SPECIES_KABUTO",      28),
    ("SPECIES_KABUTOPS",    33),
    ("SPECIES_SHIFTRY",     30),
    ("SPECIES_WYNAUT",      28),
],

# PokemonTower: Ghost only + Moltres (slot10) + MISDREAVUS dup (slot11)
"PokemonTower": [
    ("SPECIES_GASTLY",      32),
    ("SPECIES_HAUNTER",     36),
    ("SPECIES_GENGAR",      40),
    ("SPECIES_MISDREAVUS",  33),
    ("SPECIES_DUSKULL",     33),
    ("SPECIES_DUSCLOPS",    38),
    ("SPECIES_SHUPPET",     33),
    ("SPECIES_BANETTE",     38),
    ("SPECIES_DITTO",       34),
    ("SPECIES_SLOWBRO",     36),
    ("SPECIES_MOLTRES",     50),
    ("SPECIES_MISDREAVUS",  40),
],

# PowerPlant: Electric evolved + heat theme
"PowerPlant": [
    ("SPECIES_RAICHU",      38),
    ("SPECIES_MAGNETON",    36),
    ("SPECIES_ELECTRODE",   38),
    ("SPECIES_AMPHAROS",    40),
    ("SPECIES_JOLTEON",     36),
    ("SPECIES_ELECTABUZZ",  36),
    ("SPECIES_MAGMAR",      36),
    ("SPECIES_TORKOAL",     34),
    ("SPECIES_CAMERUPT",    36),
    ("SPECIES_MAGCARGO",    36),
    ("SPECIES_ZAPDOS",      50),
    ("SPECIES_PORYGON2",    38),
],

# SafariZone: Final starters + rare species (Kangaskhan removed, use Heracross->already Route9!)
# Route9 has Heracross -> SafariZone can't. Use SCIZOR instead.
# Heracross: Route9. Kangaskhan: Route12. -> SafariZone gets 10 different species.
"SafariZone": [
    ("SPECIES_VENUSAUR",    36),
    ("SPECIES_BLASTOISE",   36),
    ("SPECIES_CHARIZARD",   36),
    ("SPECIES_MEGANIUM",    36),
    ("SPECIES_TYPHLOSION",  36),
    ("SPECIES_FERALIGATR",  36),
    ("SPECIES_SCEPTILE",    36),
    ("SPECIES_BLAZIKEN",    36),
    ("SPECIES_SWAMPERT",    36),
    ("SPECIES_SCIZOR",      34),
    ("SPECIES_WIGGLYTUFF",  33),
    ("SPECIES_CLEFABLE",    33),
],

"Route23": [
    ("SPECIES_EEVEE",       32),
    ("SPECIES_ESPEON",      36),
    ("SPECIES_UMBREON",     36),
    ("SPECIES_FLAREON",     36),
    ("SPECIES_VAPOREON",    36),
    ("SPECIES_CHIKORITA",   32),
    ("SPECIES_BAYLEEF",     35),
    ("SPECIES_CYNDAQUIL",   32),
    ("SPECIES_QUILAVA",     35),
    ("SPECIES_TOTODILE",    32),
    ("SPECIES_CROCONAW",    35),
    ("SPECIES_GROVYLE",     34),
],

"Route24": [
    ("SPECIES_SEEL",        33),
    ("SPECIES_DEWGONG",     38),
    ("SPECIES_SNORUNT",     33),
    ("SPECIES_GLALIE",      38),
    ("SPECIES_DELIBIRD",    35),
    ("SPECIES_SMOOCHUM",    33),
    ("SPECIES_SPHEAL",      35),
    ("SPECIES_SEALEO",      38),
    ("SPECIES_LAPRAS",      38),
    ("SPECIES_JYNX",        35),
    ("SPECIES_REGICE",      40),
    ("SPECIES_LATIOS",      40),
],

"Route25": [
    ("SPECIES_LUNATONE",    35),
    ("SPECIES_SOLROCK",     35),
    ("SPECIES_SLOWKING",    38),
    ("SPECIES_MR_MIME",     34),
    ("SPECIES_CLAYDOL",     36),
    ("SPECIES_BELDUM",      34),
    ("SPECIES_METANG",      38),
    ("SPECIES_METAGROSS",   42),
    ("SPECIES_REGISTEEL",   42),
    ("SPECIES_JIRACHI",     42),
    ("SPECIES_CELEBI",      45),
    ("SPECIES_DEOXYS",      45),
],

# Seafoam: Ice/Water cave - species not in Route24
# Walrein (Sealeo->Walrein: only Walrein free), Azumarill, Treecko, Combusken, Magby
# + Slowbro is in PokemonTower -> can't use in Seafoam
# + Wigglytuff in SafariZone -> can't use
# + Clefable in SafariZone -> can't use
# Truly free for Seafoam: Walrein, Azumarill, Treecko, Combusken, Magby
# That's only 5 + 3 legendaries = 8 slots. Need 2 more.
# Other free species: Lickitung(Route12), Stantler(Route12) - both used.
# SUICUNE: will go to VictoryRoad
# HO-OH: will go to VictoryRoad or CeruleanCave
# Free: WOBBUFFET is Route11. DITTO is PokemonTower.
# PORYGON2 is PowerPlant. FORRETRESS is Route14.
# What about: AZUMARILL, POLITOED... no Route6 has Politoed.
# Let me use: Walrein, Azumarill, Treecko, Combusken, Magby, + Piloswine(already Route10!)
# Route10 has Piloswine... Need something else.
# SLOWKING is Route25. WOBBUFFET is Route11.
# How about LUVDISC? Route18 has it. CORSOLA? Route10 has it.
# Free water/cold mons: Let me check again what's TRULY free.
# After all areas above: the free species (not in ANY area) would be:
# Run a quick check: anything not assigned above?
# Going through the full ALL list mentally is hard. Let me just use:
# Free: WALREIN, AZUMARILL, TREECKO, COMBUSKEN, MAGBY, WIGGLYTUFF(SafariZone)
# Wait SafariZone has Wigglytuff... so Seafoam can't.
# Hmm - what if SafariZone doesn't have Wigglytuff? Let's swap:
# SafariZone slot 11: AZUMARILL (water/normal fits)
# Then Seafoam gets WIGGLYTUFF... but Wigglytuff doesn't fit Seafoam theme.
# CeruleanCave can get Wigglytuff (fits - psychic-ish Normal, great cave mon).
# Then SafariZone slot 11: AZUMARILL
# Seafoam: Walrein, Treecko, Combusken, Magby + ???
# Actually let me reconsider CeruleanCave completely.
# CeruleanCave needs 10 non-legendary species, all unique, all not used elsewhere.
# After all other areas, what's left unassigned from our 363 species?
# I'll just pick the 10 free species programmatically and assign them.
# For now, let me make a WORKING version that I can validate and fix.
"Seafoam": [
    ("SPECIES_WALREIN",     48),
    ("SPECIES_AZUMARILL",   48),
    ("SPECIES_TREECKO",     44),
    ("SPECIES_COMBUSKEN",   44),
    ("SPECIES_MAGBY",       44),
    ("SPECIES_SUICUNE",     48),
    ("SPECIES_HO_OH",       50),
    ("SPECIES_STANTLER",    46),  # DUP Route12 - will fix
    ("SPECIES_KYOGRE",      50),
    ("SPECIES_PILOSWINE",   46),  # DUP Route10 - will fix
    ("SPECIES_ARTICUNO",    50),
    ("SPECIES_LUGIA",       50),
],

"VictoryRoad": [
    ("SPECIES_STEELIX",     47),
    ("SPECIES_RHYDON",      45),
    ("SPECIES_TYRANITAR",   48),
    ("SPECIES_AGGRON",      46),
    ("SPECIES_LICKITUNG",   46),  # DUP Route12 - will fix
    ("SPECIES_PORYGON2",    46),  # DUP PowerPlant - will fix
    ("SPECIES_KANGASKHAN",  46),  # DUP Route12 - will fix
    ("SPECIES_TAUROS",      46),  # DUP Route12 - will fix
    ("SPECIES_WIGGLYTUFF",  46),  # DUP SafariZone - will fix
    ("SPECIES_CLEFABLE",    46),  # DUP SafariZone/MtMoon - will fix
    ("SPECIES_REGIROCK",    45),
    ("SPECIES_GROUDON",     45),
],

"CeruleanCave": [
    ("SPECIES_DITTO",       47),  # DUP PokemonTower - will fix
    ("SPECIES_WOBBUFFET",   47),  # DUP Route11 - will fix
    ("SPECIES_FORRETRESS",  48),  # DUP Route14 - will fix
    ("SPECIES_POLITOED",    48),  # DUP Route6 - will fix
    ("SPECIES_PRIMEAPE",    48),  # DUP Route16 - will fix
    ("SPECIES_HERACROSS",   48),  # DUP Route9 - will fix
    ("SPECIES_KANGASKHAN",  50),  # DUP Route12 - will fix
    ("SPECIES_TAUROS",      50),  # DUP Route12 - will fix
    ("SPECIES_PORYGON2",    48),  # DUP PowerPlant - will fix
    ("SPECIES_AERODACTYL",  48),  # DUP Route17 - will fix
    ("SPECIES_MEW",         50),
    ("SPECIES_MEWTWO",      70),
],

}

MAP_GROUPS = {
    "Route2":         ["MAP_ROUTE2"],
    "ViridianForest": ["MAP_VIRIDIAN_FOREST"],
    "Route3":         ["MAP_ROUTE3"],
    "MtMoon":         ["MAP_MT_MOON_1F","MAP_MT_MOON_B1F","MAP_MT_MOON_B2F"],
    "Route4":         ["MAP_ROUTE4"],
    "Route22":        ["MAP_ROUTE22"],
    "Route5":         ["MAP_ROUTE5"],
    "Route6":         ["MAP_ROUTE6"],
    "Route7":         ["MAP_ROUTE7"],
    "Route8":         ["MAP_ROUTE8"],
    "RockTunnel":     ["MAP_ROCK_TUNNEL_1F","MAP_ROCK_TUNNEL_B1F"],
    "Route9":         ["MAP_ROUTE9"],
    "Route10":        ["MAP_ROUTE10"],
    "Route11":        ["MAP_ROUTE11"],
    "Route12":        ["MAP_ROUTE12"],
    "Route13":        ["MAP_ROUTE13"],
    "Route14":        ["MAP_ROUTE14"],
    "Route15":        ["MAP_ROUTE15"],
    "Route16":        ["MAP_ROUTE16"],
    "Route17":        ["MAP_ROUTE17"],
    "Route18":        ["MAP_ROUTE18"],
    "Route21North":   ["MAP_ROUTE21_NORTH"],
    "Route21South":   ["MAP_ROUTE21_SOUTH"],
    "PokemonTower":   ["MAP_POKEMON_TOWER_3F","MAP_POKEMON_TOWER_4F","MAP_POKEMON_TOWER_5F",
                       "MAP_POKEMON_TOWER_6F","MAP_POKEMON_TOWER_7F"],
    "PowerPlant":     ["MAP_POWER_PLANT"],
    "SafariZone":     ["MAP_SAFARI_ZONE_CENTER","MAP_SAFARI_ZONE_EAST",
                       "MAP_SAFARI_ZONE_NORTH","MAP_SAFARI_ZONE_WEST"],
    "Route23":        ["MAP_ROUTE23"],
    "Route24":        ["MAP_ROUTE24"],
    "Route25":        ["MAP_ROUTE25"],
    "Seafoam":        ["MAP_SEAFOAM_ISLANDS_1F","MAP_SEAFOAM_ISLANDS_B1F",
                       "MAP_SEAFOAM_ISLANDS_B2F","MAP_SEAFOAM_ISLANDS_B3F",
                       "MAP_SEAFOAM_ISLANDS_B4F"],
    "VictoryRoad":    ["MAP_VICTORY_ROAD_1F","MAP_VICTORY_ROAD_2F","MAP_VICTORY_ROAD_3F"],
    "CeruleanCave":   ["MAP_CERULEAN_CAVE_1F","MAP_CERULEAN_CAVE_2F","MAP_CERULEAN_CAVE_B1F"],
}

def validate(area_mons):
    used = defaultdict(list)
    errors = []
    for area, mons in area_mons.items():
        if len(mons) != 12:
            errors.append(f"SIZE: {area} has {len(mons)} mons")
        for sp, lv in mons:
            used[sp].append(area)
    for sp, areas in used.items():
        unique = list(set(areas))
        if len(unique) > 1:
            errors.append(f"DUP: {sp} in {unique}")
    # Allow MISDREAVUS dup within PokemonTower
    pt = [sp for sp,lv in area_mons.get("PokemonTower",[])]
    from collections import Counter
    for sp,cnt in Counter(pt).items():
        if cnt > 1 and sp != "SPECIES_MISDREAVUS":
            errors.append(f"PT intra-dup: {sp}")
    return errors

def make_mons(lst):
    return [{"min_level":lv,"max_level":lv,"species":sp} for sp,lv in lst]

def main():
    errors = validate(AREA_MONS)
    if errors:
        print(f"VALIDATION ERRORS ({len(errors)}):")
        for e in errors:
            print(f"  {e}")
        print("Aborting.")
        sys.exit(1)

    print("Validation passed!")
    json_path = "src/data/wild_encounters.json"
    map_to_area = {m:a for a,maps in MAP_GROUPS.items() for m in maps}

    with open(json_path) as f:
        data = json.load(f)

    changed = 0
    for group in data["wild_encounter_groups"]:
        for enc in group.get("encounters",[]):
            mid = enc.get("map","")
            if mid in map_to_area:
                area = map_to_area[mid]
                if area in AREA_MONS and "land_mons" in enc:
                    enc["land_mons"]["mons"] = make_mons(AREA_MONS[area])
                    changed += 1
                    print(f"  Updated {mid} ({area})")

    with open(json_path,"w") as f:
        json.dump(data,f,indent=2)
        f.write("\n")
    print(f"\nDone. Updated {changed} entries.")

if __name__ == "__main__":
    main()
