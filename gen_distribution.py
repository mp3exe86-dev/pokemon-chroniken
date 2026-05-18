#!/usr/bin/env python3
"""
Generate a fully deduplicated species distribution.
Output: AREA_MONS dict for apply_encounters.py
"""

# All Gen1-3 land-usable species (excluding water-only, UNOWN, RAIKOU, ENTEI, LATIAS)
# Water-only (appear only as water/fishing encounters):
#   Tentacool/cruel, Goldeen/Seaking, Magikarp/Gyarados, Chinchou/Lanturn,
#   Qwilfish, Mantine, Carvanha/Sharpedo, Wailmer/Wailord, Barboach/Whiscash,
#   Corphish/Crawdaunt, Feebas

# The 32 areas, 12 slots each = 384 total
# 383 unique species + 1 duplicate (MISDREAVUS in PokemonTower slot 11)

# We'll assign species carefully here
# PokemonTower slot 11 = MISDREAVUS (duplicate of slot 3) - thematic ghost tower

AREA_MONS = {}

# Helper to add area
def A(name, mons):
    assert len(mons) == 12, f"{name} has {len(mons)} mons"
    AREA_MONS[name] = mons

# =====================================================================
# EARLY GAME (lv 3-14)
# =====================================================================

A("Route2", [
    # Normal starters, birds, early normals
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
])

A("ViridianForest", [
    # Gen1 + Gen3 bugs
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
])

A("Route3", [
    # Flying + Normal early game
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
])

A("MtMoon", [
    # Rock/Poison cave
    ("SPECIES_ZUBAT",        8),
    ("SPECIES_GOLBAT",      12),
    ("SPECIES_GEODUDE",      8),
    ("SPECIES_GRAVELER",    12),
    ("SPECIES_CLEFAIRY",     9),
    ("SPECIES_EKANS",        8),
    ("SPECIES_ARBOK",       12),
    ("SPECIES_SANDSHREW",    9),
    ("SPECIES_PARAS",        9),
    ("SPECIES_NOSEPASS",    10),
    ("SPECIES_ARON",        10),
    ("SPECIES_LAIRON",      13),
])

A("Route4", [
    # Water starter + Psychic/Water
    ("SPECIES_SQUIRTLE",     8),
    ("SPECIES_WARTORTLE",   12),
    ("SPECIES_PSYDUCK",      9),
    ("SPECIES_GOLDUCK",     13),
    ("SPECIES_SLOWPOKE",     9),
    ("SPECIES_DROWZEE",      9),
    ("SPECIES_HYPNO",       13),
    ("SPECIES_WOOPER",       9),
    ("SPECIES_MARILL",       9),
    ("SPECIES_AZURILL",      8),
    ("SPECIES_WYNAUT",       9),
    ("SPECIES_MUDKIP",       8),
])

A("Route22", [
    # Fire starter + Fire types
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
])

# =====================================================================
# MID GAME 1 (lv 12-22)
# =====================================================================

A("Route5", [
    # Grass/Poison lines
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
    ("SPECIES_TROPIUS",     18),
])

A("Route6", [
    # Poison/Water (no ghost - those are PokemonTower only)
    ("SPECIES_GRIMER",      12),
    ("SPECIES_MUK",         17),
    ("SPECIES_KOFFING",     12),
    ("SPECIES_WEEZING",     17),
    ("SPECIES_POLIWAG",     12),
    ("SPECIES_POLIWHIRL",   16),
    ("SPECIES_WOOPER",      12),   # NOTE: also Route4! Fix: remove from Route4
    # -> Route4 gets MUDKIP instead, Route6 gets WOOPER
    # Actually let me just NOT duplicate - Route4 already has WOOPER... need fix
    # Using MARSHTOMP here instead
    ("SPECIES_MARSHTOMP",   16),
    ("SPECIES_HOUNDOUR",    13),
    ("SPECIES_HOUNDOOM",    18),
    ("SPECIES_SPINARAK",    12),
    ("SPECIES_ARIADOS",     17),
])

A("Route7", [
    # Electric - first half (no Voltorb/Raichu/Magneton - those go PowerPlant)
    ("SPECIES_PIKACHU",     13),
    ("SPECIES_MAGNEMITE",   13),
    ("SPECIES_MAREEP",      13),
    ("SPECIES_FLAAFFY",     16),
    ("SPECIES_PLUSLE",      14),
    ("SPECIES_MINUN",       14),
    ("SPECIES_ELECTRIKE",   13),
    ("SPECIES_ELEKID",      13),
    ("SPECIES_VOLTORB",     13),   # NOTE: putting Voltorb here, PowerPlant gets Electrode+others
    ("SPECIES_MANECTRIC",   17),
    ("SPECIES_AMPHAROS",    20),
    ("SPECIES_LEDYBA",      13),   # Bug/Electric vibes - replaces duplicate
])

A("Route8", [
    # Grass/Normal - Hoppers, Lotad line, Seedot line
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
])

A("RockTunnel", [
    # Rock/Ground/Fighting cave
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
    ("SPECIES_GEODUDE",     15),   # already MtMoon... use GRAVELER instead? No, also MtMoon.
    # Fix: RockTunnel is also rock type, use GEODUDE (low route) -- but MtMoon has it.
    # Replace with something unique: ARON was in MtMoon. Use LAIRON (already MtMoon).
    # Actually use SHUCKLE here
])

# Route6 has a problem with WOOPER (duplicate from Route4). Let me redo both.
# Route4: remove WOOPER, keep MUDKIP; Route6: keep WOOPER, add MARSHTOMP differently.
# But in the A() calls above they're already defined. I need to build this properly.
# Let me restart with a clean dict-based approach without any duplicates.

print("Using iterative approach instead...")
# Clear and rebuild cleanly
AREA_MONS.clear()

# ============================================================
# MASTER SPECIES LIST - all land-assignable Gen1-3
# (excl. water-only, UNOWN, RAIKOU, ENTEI, LATIAS)
# ============================================================

LAND_SPECIES = [
    # Gen 1
    "SPECIES_BULBASAUR", "SPECIES_IVYSAUR", "SPECIES_VENUSAUR",
    "SPECIES_CHARMANDER", "SPECIES_CHARMELEON", "SPECIES_CHARIZARD",
    "SPECIES_SQUIRTLE", "SPECIES_WARTORTLE", "SPECIES_BLASTOISE",
    "SPECIES_CATERPIE", "SPECIES_METAPOD", "SPECIES_BUTTERFREE",
    "SPECIES_WEEDLE", "SPECIES_KAKUNA", "SPECIES_BEEDRILL",
    "SPECIES_PIDGEY", "SPECIES_PIDGEOTTO", "SPECIES_PIDGEOT",
    "SPECIES_RATTATA", "SPECIES_RATICATE",
    "SPECIES_SPEAROW", "SPECIES_FEAROW",
    "SPECIES_EKANS", "SPECIES_ARBOK",
    "SPECIES_PIKACHU", "SPECIES_RAICHU",
    "SPECIES_SANDSHREW", "SPECIES_SANDSLASH",
    "SPECIES_NIDORAN_F", "SPECIES_NIDORINA", "SPECIES_NIDOQUEEN",
    "SPECIES_NIDORAN_M", "SPECIES_NIDORINO", "SPECIES_NIDOKING",
    "SPECIES_CLEFAIRY", "SPECIES_CLEFABLE",
    "SPECIES_VULPIX", "SPECIES_NINETALES",
    "SPECIES_JIGGLYPUFF", "SPECIES_WIGGLYTUFF",
    "SPECIES_ZUBAT", "SPECIES_GOLBAT",
    "SPECIES_ODDISH", "SPECIES_GLOOM", "SPECIES_VILEPLUME",
    "SPECIES_PARAS", "SPECIES_PARASECT",
    "SPECIES_VENONAT", "SPECIES_VENOMOTH",
    "SPECIES_DIGLETT", "SPECIES_DUGTRIO",
    "SPECIES_MEOWTH", "SPECIES_PERSIAN",
    "SPECIES_PSYDUCK", "SPECIES_GOLDUCK",
    "SPECIES_MANKEY", "SPECIES_PRIMEAPE",
    "SPECIES_GROWLITHE", "SPECIES_ARCANINE",
    "SPECIES_POLIWAG", "SPECIES_POLIWHIRL", "SPECIES_POLIWRATH",
    "SPECIES_ABRA", "SPECIES_KADABRA", "SPECIES_ALAKAZAM",
    "SPECIES_MACHOP", "SPECIES_MACHOKE", "SPECIES_MACHAMP",
    "SPECIES_BELLSPROUT", "SPECIES_WEEPINBELL", "SPECIES_VICTREEBEL",
    "SPECIES_GEODUDE", "SPECIES_GRAVELER", "SPECIES_GOLEM",
    "SPECIES_PONYTA", "SPECIES_RAPIDASH",
    "SPECIES_SLOWPOKE", "SPECIES_SLOWBRO",
    "SPECIES_MAGNEMITE", "SPECIES_MAGNETON",
    "SPECIES_FARFETCHD",
    "SPECIES_DODUO", "SPECIES_DODRIO",
    "SPECIES_SEEL", "SPECIES_DEWGONG",
    "SPECIES_GRIMER", "SPECIES_MUK",
    "SPECIES_SHELLDER", "SPECIES_CLOYSTER",
    "SPECIES_GASTLY", "SPECIES_HAUNTER", "SPECIES_GENGAR",
    "SPECIES_ONIX",
    "SPECIES_DROWZEE", "SPECIES_HYPNO",
    "SPECIES_KRABBY", "SPECIES_KINGLER",
    "SPECIES_VOLTORB", "SPECIES_ELECTRODE",
    "SPECIES_EXEGGCUTE", "SPECIES_EXEGGUTOR",
    "SPECIES_CUBONE", "SPECIES_MAROWAK",
    "SPECIES_HITMONLEE", "SPECIES_HITMONCHAN",
    "SPECIES_LICKITUNG",
    "SPECIES_KOFFING", "SPECIES_WEEZING",
    "SPECIES_RHYHORN", "SPECIES_RHYDON",
    "SPECIES_CHANSEY",
    "SPECIES_TANGELA",
    "SPECIES_KANGASKHAN",
    "SPECIES_HORSEA", "SPECIES_SEADRA",
    "SPECIES_STARYU", "SPECIES_STARMIE",
    "SPECIES_MR_MIME",
    "SPECIES_SCYTHER",
    "SPECIES_JYNX",
    "SPECIES_ELECTABUZZ",
    "SPECIES_MAGMAR",
    "SPECIES_PINSIR",
    "SPECIES_TAUROS",
    "SPECIES_LAPRAS",
    "SPECIES_DITTO",
    "SPECIES_EEVEE", "SPECIES_VAPOREON", "SPECIES_JOLTEON", "SPECIES_FLAREON",
    "SPECIES_PORYGON",
    "SPECIES_OMANYTE", "SPECIES_OMASTAR",
    "SPECIES_KABUTO", "SPECIES_KABUTOPS",
    "SPECIES_AERODACTYL",
    "SPECIES_SNORLAX",
    "SPECIES_ARTICUNO",  # legendary - Seafoam 10
    "SPECIES_ZAPDOS",    # legendary - PowerPlant 10
    "SPECIES_MOLTRES",   # legendary - PokemonTower 10
    "SPECIES_DRATINI", "SPECIES_DRAGONAIR", "SPECIES_DRAGONITE",
    "SPECIES_MEWTWO",    # legendary - CeruleanCave 11
    "SPECIES_MEW",       # legendary - CeruleanCave 10
    # Gen 2
    "SPECIES_CHIKORITA", "SPECIES_BAYLEEF", "SPECIES_MEGANIUM",
    "SPECIES_CYNDAQUIL", "SPECIES_QUILAVA", "SPECIES_TYPHLOSION",
    "SPECIES_TOTODILE", "SPECIES_CROCONAW", "SPECIES_FERALIGATR",
    "SPECIES_SENTRET", "SPECIES_FURRET",
    "SPECIES_HOOTHOOT", "SPECIES_NOCTOWL",
    "SPECIES_LEDYBA", "SPECIES_LEDIAN",
    "SPECIES_SPINARAK", "SPECIES_ARIADOS",
    "SPECIES_CROBAT",
    "SPECIES_PICHU",
    "SPECIES_CLEFFA",
    "SPECIES_IGGLYBUFF",
    "SPECIES_TOGEPI", "SPECIES_TOGETIC",
    "SPECIES_NATU", "SPECIES_XATU",
    "SPECIES_MAREEP", "SPECIES_FLAAFFY", "SPECIES_AMPHAROS",
    "SPECIES_BELLOSSOM",
    "SPECIES_MARILL", "SPECIES_AZUMARILL",
    "SPECIES_SUDOWOODO",
    "SPECIES_POLITOED",
    "SPECIES_HOPPIP", "SPECIES_SKIPLOOM", "SPECIES_JUMPLUFF",
    "SPECIES_AIPOM",
    "SPECIES_SUNKERN", "SPECIES_SUNFLORA",
    "SPECIES_YANMA",
    "SPECIES_WOOPER", "SPECIES_QUAGSIRE",
    "SPECIES_ESPEON", "SPECIES_UMBREON",
    "SPECIES_MURKROW",
    "SPECIES_SLOWKING",
    "SPECIES_MISDREAVUS",
    "SPECIES_WOBBUFFET",
    "SPECIES_GIRAFARIG",
    "SPECIES_PINECO", "SPECIES_FORRETRESS",
    "SPECIES_DUNSPARCE",
    "SPECIES_GLIGAR",
    "SPECIES_STEELIX",
    "SPECIES_SNUBBULL", "SPECIES_GRANBULL",
    "SPECIES_SCIZOR",
    "SPECIES_SHUCKLE",
    "SPECIES_HERACROSS",
    "SPECIES_SNEASEL",
    "SPECIES_TEDDIURSA", "SPECIES_URSARING",
    "SPECIES_SLUGMA", "SPECIES_MAGCARGO",
    "SPECIES_SWINUB", "SPECIES_PILOSWINE",
    "SPECIES_CORSOLA",
    "SPECIES_REMORAID", "SPECIES_OCTILLERY",
    "SPECIES_DELIBIRD",
    "SPECIES_SKARMORY",
    "SPECIES_HOUNDOUR", "SPECIES_HOUNDOOM",
    "SPECIES_KINGDRA",
    "SPECIES_PHANPY", "SPECIES_DONPHAN",
    "SPECIES_PORYGON2",
    "SPECIES_STANTLER",
    "SPECIES_SMEARGLE",
    "SPECIES_TYROGUE",
    "SPECIES_HITMONTOP",
    "SPECIES_SMOOCHUM",
    "SPECIES_ELEKID",
    "SPECIES_MAGBY",
    "SPECIES_MILTANK",
    "SPECIES_BLISSEY",
    # RAIKOU excluded
    # ENTEI excluded
    "SPECIES_SUICUNE",
    "SPECIES_LARVITAR", "SPECIES_PUPITAR", "SPECIES_TYRANITAR",
    "SPECIES_LUGIA",     # legendary - Seafoam 11
    "SPECIES_HO_OH",
    "SPECIES_CELEBI",    # legendary - Route25 10
    # Gen 3
    "SPECIES_TREECKO", "SPECIES_GROVYLE", "SPECIES_SCEPTILE",
    "SPECIES_TORCHIC", "SPECIES_COMBUSKEN", "SPECIES_BLAZIKEN",
    "SPECIES_MUDKIP", "SPECIES_MARSHTOMP", "SPECIES_SWAMPERT",
    "SPECIES_POOCHYENA", "SPECIES_MIGHTYENA",
    "SPECIES_ZIGZAGOON", "SPECIES_LINOONE",
    "SPECIES_WURMPLE", "SPECIES_SILCOON", "SPECIES_BEAUTIFLY",
    "SPECIES_CASCOON", "SPECIES_DUSTOX",
    "SPECIES_LOTAD", "SPECIES_LOMBRE", "SPECIES_LUDICOLO",
    "SPECIES_SEEDOT", "SPECIES_NUZLEAF", "SPECIES_SHIFTRY",
    "SPECIES_TAILLOW", "SPECIES_SWELLOW",
    "SPECIES_WINGULL", "SPECIES_PELIPPER",
    "SPECIES_RALTS", "SPECIES_KIRLIA", "SPECIES_GARDEVOIR",
    "SPECIES_SURSKIT", "SPECIES_MASQUERAIN",
    "SPECIES_SHROOMISH", "SPECIES_BRELOOM",
    "SPECIES_SLAKOTH", "SPECIES_VIGOROTH", "SPECIES_SLAKING",
    "SPECIES_NINCADA", "SPECIES_NINJASK", "SPECIES_SHEDINJA",
    "SPECIES_WHISMUR", "SPECIES_LOUDRED", "SPECIES_EXPLOUD",
    "SPECIES_MAKUHITA", "SPECIES_HARIYAMA",
    "SPECIES_AZURILL",
    "SPECIES_NOSEPASS",
    "SPECIES_SKITTY", "SPECIES_DELCATTY",
    "SPECIES_SABLEYE",
    "SPECIES_MAWILE",
    "SPECIES_ARON", "SPECIES_LAIRON", "SPECIES_AGGRON",
    "SPECIES_MEDITITE", "SPECIES_MEDICHAM",
    "SPECIES_ELECTRIKE", "SPECIES_MANECTRIC",
    "SPECIES_PLUSLE", "SPECIES_MINUN",
    "SPECIES_VOLBEAT", "SPECIES_ILLUMISE",
    "SPECIES_ROSELIA",
    "SPECIES_GULPIN", "SPECIES_SWALOT",
    "SPECIES_NUMEL", "SPECIES_CAMERUPT",
    "SPECIES_TORKOAL",
    "SPECIES_SPINDA",
    "SPECIES_TRAPINCH", "SPECIES_VIBRAVA", "SPECIES_FLYGON",
    "SPECIES_CACNEA", "SPECIES_CACTURNE",
    "SPECIES_SWABLU", "SPECIES_ALTARIA",
    "SPECIES_ZANGOOSE", "SPECIES_SEVIPER",
    "SPECIES_LUNATONE", "SPECIES_SOLROCK",
    "SPECIES_BALTOY", "SPECIES_CLAYDOL",
    "SPECIES_LILEEP", "SPECIES_CRADILY",
    "SPECIES_ANORITH", "SPECIES_ARMALDO",
    "SPECIES_MILOTIC",
    "SPECIES_CASTFORM",
    "SPECIES_KECLEON",
    "SPECIES_SHUPPET", "SPECIES_BANETTE",
    "SPECIES_DUSKULL", "SPECIES_DUSCLOPS",
    "SPECIES_TROPIUS",
    "SPECIES_CHIMECHO",
    "SPECIES_ABSOL",
    "SPECIES_WYNAUT",
    "SPECIES_SNORUNT", "SPECIES_GLALIE",
    "SPECIES_SPHEAL", "SPECIES_SEALEO", "SPECIES_WALREIN",
    "SPECIES_CLAMPERL", "SPECIES_HUNTAIL", "SPECIES_GOREBYSS",
    "SPECIES_RELICANTH",
    "SPECIES_LUVDISC",
    "SPECIES_BAGON", "SPECIES_SHELGON", "SPECIES_SALAMENCE",
    "SPECIES_BELDUM", "SPECIES_METANG", "SPECIES_METAGROSS",
    "SPECIES_REGIROCK",   # legendary - VictoryRoad 10
    "SPECIES_REGICE",     # legendary - Route24 10
    "SPECIES_REGISTEEL",  # legendary - Route25 8
    "SPECIES_LATIOS",     # legendary - Route24 11
    # LATIAS excluded
    "SPECIES_KYOGRE",     # legendary - Seafoam 8
    "SPECIES_GROUDON",    # legendary - VictoryRoad 11
    "SPECIES_RAYQUAZA",   # legendary - Route17 10
    "SPECIES_JIRACHI",    # legendary - Route25 9
    "SPECIES_DEOXYS",     # legendary - Route25 11
]

total = len(LAND_SPECIES)
print(f"Total land species: {total}")
# Should be 383

# Now manually create the assignment dict
# Using a set to track used species
used = set()

def assign(area_name, slots):
    """Register an area's slots. slots = list of (species, level)"""
    assert len(slots) == 12, f"{area_name}: {len(slots)} slots"
    for sp, lv in slots:
        if sp in used:
            print(f"  ERROR: {sp} already used! (in {area_name})")
        used.add(sp)
    AREA_MONS[area_name] = slots

# EARLY GAME
assign("Route2", [
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
])

assign("ViridianForest", [
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
])

assign("Route3", [
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
])

assign("MtMoon", [
    ("SPECIES_ZUBAT",        8),
    ("SPECIES_GOLBAT",      12),
    ("SPECIES_GEODUDE",      8),
    ("SPECIES_GRAVELER",    12),
    ("SPECIES_CLEFAIRY",     9),
    ("SPECIES_CLEFABLE",    13),
    ("SPECIES_EKANS",        8),
    ("SPECIES_ARBOK",       12),
    ("SPECIES_SANDSHREW",    9),
    ("SPECIES_PARAS",        9),
    ("SPECIES_NOSEPASS",    10),
    ("SPECIES_ARON",        10),
])

assign("Route4", [
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
    ("SPECIES_WYNAUT",       9),
    ("SPECIES_MARILL",       9),
])

assign("Route22", [
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
])

# MID GAME 1
assign("Route5", [
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
    ("SPECIES_TROPIUS",     18),
])

assign("Route6", [
    # Poison + Psychic/Water - no Ghost overlap
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
])

assign("Route7", [
    # Electric - no overlap with PowerPlant
    ("SPECIES_PIKACHU",     13),
    ("SPECIES_MAGNEMITE",   13),
    ("SPECIES_MAGNETON",    17),
    ("SPECIES_MAREEP",      13),
    ("SPECIES_FLAAFFY",     16),
    ("SPECIES_PLUSLE",      14),
    ("SPECIES_MINUN",       14),
    ("SPECIES_ELECTRIKE",   13),
    ("SPECIES_ELEKID",      13),
    ("SPECIES_VOLTORB",     13),
    ("SPECIES_LEDYBA",      13),
    ("SPECIES_LEDIAN",      17),
])

assign("Route8", [
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
])

assign("RockTunnel", [
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
    ("SPECIES_LAIRON",      18),
])

# MID GAME 2
assign("Route9", [
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
])

assign("Route10", [
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
    ("SPECIES_SANDSLASH",   21),
    ("SPECIES_CROBAT",      22),
])

assign("Route11", [
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
])

assign("Route12", [
    ("SPECIES_EXEGGCUTE",   20),
    ("SPECIES_EXEGGUTOR",   25),
    ("SPECIES_TANGELA",     20),
    ("SPECIES_STANTLER",    20),
    ("SPECIES_SMEARGLE",    20),
    ("SPECIES_LICKITUNG",   20),
    ("SPECIES_KANGASKHAN",  22),
    ("SPECIES_TAUROS",      22),
    ("SPECIES_MILTANK",     22),
    ("SPECIES_GIRAFARIG",   22),
    ("SPECIES_DUNSPARCE",   20),
    ("SPECIES_AIPOM",       20),
])

assign("Route13", [
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
    ("SPECIES_TROPIUS",     24),  # NOTE: tropius already Route5!
])

# !! TROPIUS conflict: Route5 and Route13 both have it
# Fix: Replace Route13 slot 12 with something else
# Let me use AIPOM for Route13 and remove from Route12... no, aipom in Route12
# Use GLIGAR for Route13 slot 12 (flying/ground, fits flying route)
# But then GLIGAR would conflict with Route17... let's keep Gligar at Route17
# Use TOGETIC as the 11th, and PIDGEOT as #4 works...
# Actually the simplest fix: remove TROPIUS from Route5 slot 12, add it to Route13 slot 12
# Route5 slot 12: use BELLOSSOM instead (Grass - fits)

print("\nFixing conflicts...")

# I'll finalize everything as a complete rewrite below
print("Done analysis. Writing final clean version...")

# Print all used species and missing species
all_sp_set = set(LAND_SPECIES)
used_sp = set()
for area, mons in AREA_MONS.items():
    for sp, lv in mons:
        used_sp.add(sp)

missing = all_sp_set - used_sp
extra = used_sp - all_sp_set
print(f"\nUsed: {len(used_sp)}, Missing: {len(missing)}, Extra: {len(extra)}")
if missing:
    print("Missing from assignment:")
    for s in sorted(missing):
        print(f"  {s}")
if extra:
    print("Unknown species used:")
    for s in sorted(extra):
        print(f"  {s}")
