#!/usr/bin/env python3
"""
Build final clean distribution. Run this to generate apply_encounters.py
"""
from collections import defaultdict

# All land-assignable Gen1-3 species (not water-only, not UNOWN, not RAIKOU/ENTEI/LATIAS)
# Total: 383 species (we'll assign all + 1 dup = 384 slots)

ALL = [
 "SPECIES_BULBASAUR","SPECIES_IVYSAUR","SPECIES_VENUSAUR",
 "SPECIES_CHARMANDER","SPECIES_CHARMELEON","SPECIES_CHARIZARD",
 "SPECIES_SQUIRTLE","SPECIES_WARTORTLE","SPECIES_BLASTOISE",
 "SPECIES_CATERPIE","SPECIES_METAPOD","SPECIES_BUTTERFREE",
 "SPECIES_WEEDLE","SPECIES_KAKUNA","SPECIES_BEEDRILL",
 "SPECIES_PIDGEY","SPECIES_PIDGEOTTO","SPECIES_PIDGEOT",
 "SPECIES_RATTATA","SPECIES_RATICATE",
 "SPECIES_SPEAROW","SPECIES_FEAROW",
 "SPECIES_EKANS","SPECIES_ARBOK",
 "SPECIES_PIKACHU","SPECIES_RAICHU",
 "SPECIES_SANDSHREW","SPECIES_SANDSLASH",
 "SPECIES_NIDORAN_F","SPECIES_NIDORINA","SPECIES_NIDOQUEEN",
 "SPECIES_NIDORAN_M","SPECIES_NIDORINO","SPECIES_NIDOKING",
 "SPECIES_CLEFAIRY","SPECIES_CLEFABLE",
 "SPECIES_VULPIX","SPECIES_NINETALES",
 "SPECIES_JIGGLYPUFF","SPECIES_WIGGLYTUFF",
 "SPECIES_ZUBAT","SPECIES_GOLBAT",
 "SPECIES_ODDISH","SPECIES_GLOOM","SPECIES_VILEPLUME",
 "SPECIES_PARAS","SPECIES_PARASECT",
 "SPECIES_VENONAT","SPECIES_VENOMOTH",
 "SPECIES_DIGLETT","SPECIES_DUGTRIO",
 "SPECIES_MEOWTH","SPECIES_PERSIAN",
 "SPECIES_PSYDUCK","SPECIES_GOLDUCK",
 "SPECIES_MANKEY","SPECIES_PRIMEAPE",
 "SPECIES_GROWLITHE","SPECIES_ARCANINE",
 "SPECIES_POLIWAG","SPECIES_POLIWHIRL","SPECIES_POLIWRATH",
 "SPECIES_ABRA","SPECIES_KADABRA","SPECIES_ALAKAZAM",
 "SPECIES_MACHOP","SPECIES_MACHOKE","SPECIES_MACHAMP",
 "SPECIES_BELLSPROUT","SPECIES_WEEPINBELL","SPECIES_VICTREEBEL",
 "SPECIES_GEODUDE","SPECIES_GRAVELER","SPECIES_GOLEM",
 "SPECIES_PONYTA","SPECIES_RAPIDASH",
 "SPECIES_SLOWPOKE","SPECIES_SLOWBRO",
 "SPECIES_MAGNEMITE","SPECIES_MAGNETON",
 "SPECIES_FARFETCHD",
 "SPECIES_DODUO","SPECIES_DODRIO",
 "SPECIES_SEEL","SPECIES_DEWGONG",
 "SPECIES_GRIMER","SPECIES_MUK",
 "SPECIES_SHELLDER","SPECIES_CLOYSTER",
 "SPECIES_GASTLY","SPECIES_HAUNTER","SPECIES_GENGAR",
 "SPECIES_ONIX",
 "SPECIES_DROWZEE","SPECIES_HYPNO",
 "SPECIES_KRABBY","SPECIES_KINGLER",
 "SPECIES_VOLTORB","SPECIES_ELECTRODE",
 "SPECIES_EXEGGCUTE","SPECIES_EXEGGUTOR",
 "SPECIES_CUBONE","SPECIES_MAROWAK",
 "SPECIES_HITMONLEE","SPECIES_HITMONCHAN",
 "SPECIES_LICKITUNG",
 "SPECIES_KOFFING","SPECIES_WEEZING",
 "SPECIES_RHYHORN","SPECIES_RHYDON",
 "SPECIES_CHANSEY",
 "SPECIES_TANGELA",
 "SPECIES_KANGASKHAN",
 "SPECIES_HORSEA","SPECIES_SEADRA",
 "SPECIES_STARYU","SPECIES_STARMIE",
 "SPECIES_MR_MIME",
 "SPECIES_SCYTHER",
 "SPECIES_JYNX",
 "SPECIES_ELECTABUZZ",
 "SPECIES_MAGMAR",
 "SPECIES_PINSIR",
 "SPECIES_TAUROS",
 "SPECIES_LAPRAS",
 "SPECIES_DITTO",
 "SPECIES_EEVEE","SPECIES_VAPOREON","SPECIES_JOLTEON","SPECIES_FLAREON",
 "SPECIES_PORYGON",
 "SPECIES_OMANYTE","SPECIES_OMASTAR",
 "SPECIES_KABUTO","SPECIES_KABUTOPS",
 "SPECIES_AERODACTYL",
 "SPECIES_SNORLAX",
 "SPECIES_ARTICUNO",
 "SPECIES_ZAPDOS",
 "SPECIES_MOLTRES",
 "SPECIES_DRATINI","SPECIES_DRAGONAIR","SPECIES_DRAGONITE",
 "SPECIES_MEWTWO",
 "SPECIES_MEW",
 # Gen2
 "SPECIES_CHIKORITA","SPECIES_BAYLEEF","SPECIES_MEGANIUM",
 "SPECIES_CYNDAQUIL","SPECIES_QUILAVA","SPECIES_TYPHLOSION",
 "SPECIES_TOTODILE","SPECIES_CROCONAW","SPECIES_FERALIGATR",
 "SPECIES_SENTRET","SPECIES_FURRET",
 "SPECIES_HOOTHOOT","SPECIES_NOCTOWL",
 "SPECIES_LEDYBA","SPECIES_LEDIAN",
 "SPECIES_SPINARAK","SPECIES_ARIADOS",
 "SPECIES_CROBAT",
 "SPECIES_PICHU",
 "SPECIES_CLEFFA",
 "SPECIES_IGGLYBUFF",
 "SPECIES_TOGEPI","SPECIES_TOGETIC",
 "SPECIES_NATU","SPECIES_XATU",
 "SPECIES_MAREEP","SPECIES_FLAAFFY","SPECIES_AMPHAROS",
 "SPECIES_BELLOSSOM",
 "SPECIES_MARILL","SPECIES_AZUMARILL",
 "SPECIES_SUDOWOODO",
 "SPECIES_POLITOED",
 "SPECIES_HOPPIP","SPECIES_SKIPLOOM","SPECIES_JUMPLUFF",
 "SPECIES_AIPOM",
 "SPECIES_SUNKERN","SPECIES_SUNFLORA",
 "SPECIES_YANMA",
 "SPECIES_WOOPER","SPECIES_QUAGSIRE",
 "SPECIES_ESPEON","SPECIES_UMBREON",
 "SPECIES_MURKROW",
 "SPECIES_SLOWKING",
 "SPECIES_MISDREAVUS",
 "SPECIES_WOBBUFFET",
 "SPECIES_GIRAFARIG",
 "SPECIES_PINECO","SPECIES_FORRETRESS",
 "SPECIES_DUNSPARCE",
 "SPECIES_GLIGAR",
 "SPECIES_STEELIX",
 "SPECIES_SNUBBULL","SPECIES_GRANBULL",
 "SPECIES_SCIZOR",
 "SPECIES_SHUCKLE",
 "SPECIES_HERACROSS",
 "SPECIES_SNEASEL",
 "SPECIES_TEDDIURSA","SPECIES_URSARING",
 "SPECIES_SLUGMA","SPECIES_MAGCARGO",
 "SPECIES_SWINUB","SPECIES_PILOSWINE",
 "SPECIES_CORSOLA",
 "SPECIES_REMORAID","SPECIES_OCTILLERY",
 "SPECIES_DELIBIRD",
 "SPECIES_SKARMORY",
 "SPECIES_HOUNDOUR","SPECIES_HOUNDOOM",
 "SPECIES_KINGDRA",
 "SPECIES_PHANPY","SPECIES_DONPHAN",
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
 "SPECIES_SUICUNE",
 "SPECIES_LARVITAR","SPECIES_PUPITAR","SPECIES_TYRANITAR",
 "SPECIES_LUGIA",
 "SPECIES_HO_OH",
 "SPECIES_CELEBI",
 # Gen3
 "SPECIES_TREECKO","SPECIES_GROVYLE","SPECIES_SCEPTILE",
 "SPECIES_TORCHIC","SPECIES_COMBUSKEN","SPECIES_BLAZIKEN",
 "SPECIES_MUDKIP","SPECIES_MARSHTOMP","SPECIES_SWAMPERT",
 "SPECIES_POOCHYENA","SPECIES_MIGHTYENA",
 "SPECIES_ZIGZAGOON","SPECIES_LINOONE",
 "SPECIES_WURMPLE","SPECIES_SILCOON","SPECIES_BEAUTIFLY",
 "SPECIES_CASCOON","SPECIES_DUSTOX",
 "SPECIES_LOTAD","SPECIES_LOMBRE","SPECIES_LUDICOLO",
 "SPECIES_SEEDOT","SPECIES_NUZLEAF","SPECIES_SHIFTRY",
 "SPECIES_TAILLOW","SPECIES_SWELLOW",
 "SPECIES_WINGULL","SPECIES_PELIPPER",
 "SPECIES_RALTS","SPECIES_KIRLIA","SPECIES_GARDEVOIR",
 "SPECIES_SURSKIT","SPECIES_MASQUERAIN",
 "SPECIES_SHROOMISH","SPECIES_BRELOOM",
 "SPECIES_SLAKOTH","SPECIES_VIGOROTH","SPECIES_SLAKING",
 "SPECIES_NINCADA","SPECIES_NINJASK","SPECIES_SHEDINJA",
 "SPECIES_WHISMUR","SPECIES_LOUDRED","SPECIES_EXPLOUD",
 "SPECIES_MAKUHITA","SPECIES_HARIYAMA",
 "SPECIES_AZURILL",
 "SPECIES_NOSEPASS",
 "SPECIES_SKITTY","SPECIES_DELCATTY",
 "SPECIES_SABLEYE",
 "SPECIES_MAWILE",
 "SPECIES_ARON","SPECIES_LAIRON","SPECIES_AGGRON",
 "SPECIES_MEDITITE","SPECIES_MEDICHAM",
 "SPECIES_ELECTRIKE","SPECIES_MANECTRIC",
 "SPECIES_PLUSLE","SPECIES_MINUN",
 "SPECIES_VOLBEAT","SPECIES_ILLUMISE",
 "SPECIES_ROSELIA",
 "SPECIES_GULPIN","SPECIES_SWALOT",
 "SPECIES_NUMEL","SPECIES_CAMERUPT",
 "SPECIES_TORKOAL",
 "SPECIES_SPINDA",
 "SPECIES_TRAPINCH","SPECIES_VIBRAVA","SPECIES_FLYGON",
 "SPECIES_CACNEA","SPECIES_CACTURNE",
 "SPECIES_SWABLU","SPECIES_ALTARIA",
 "SPECIES_ZANGOOSE","SPECIES_SEVIPER",
 "SPECIES_LUNATONE","SPECIES_SOLROCK",
 "SPECIES_BALTOY","SPECIES_CLAYDOL",
 "SPECIES_LILEEP","SPECIES_CRADILY",
 "SPECIES_ANORITH","SPECIES_ARMALDO",
 "SPECIES_MILOTIC",
 "SPECIES_CASTFORM",
 "SPECIES_KECLEON",
 "SPECIES_SHUPPET","SPECIES_BANETTE",
 "SPECIES_DUSKULL","SPECIES_DUSCLOPS",
 "SPECIES_TROPIUS",
 "SPECIES_CHIMECHO",
 "SPECIES_ABSOL",
 "SPECIES_WYNAUT",
 "SPECIES_SNORUNT","SPECIES_GLALIE",
 "SPECIES_SPHEAL","SPECIES_SEALEO","SPECIES_WALREIN",
 "SPECIES_CLAMPERL","SPECIES_HUNTAIL","SPECIES_GOREBYSS",
 "SPECIES_RELICANTH",
 "SPECIES_LUVDISC",
 "SPECIES_BAGON","SPECIES_SHELGON","SPECIES_SALAMENCE",
 "SPECIES_BELDUM","SPECIES_METANG","SPECIES_METAGROSS",
 "SPECIES_REGIROCK",
 "SPECIES_REGICE",
 "SPECIES_REGISTEEL",
 "SPECIES_LATIOS",
 "SPECIES_KYOGRE",
 "SPECIES_GROUDON",
 "SPECIES_RAYQUAZA",
 "SPECIES_JIRACHI",
 "SPECIES_DEOXYS",
 # Missing from earlier list:
 "SPECIES_SPOINK","SPECIES_GRUMPIG",
]

ALL = list(dict.fromkeys(ALL))  # deduplicate preserving order
print(f"Total assignable species: {len(ALL)}")

# Manually designed assignments - each species appears ONCE
# MISDREAVUS appears twice (PokemonTower: slot 3 and slot 11) - thematic dup
# So we need 383 unique + 1 dup = 384

ASSIGNMENTS = [
 # == Route2: Early Normal/birds ==
 ("Route2","SPECIES_BULBASAUR",3),
 ("Route2","SPECIES_IVYSAUR",5),
 ("Route2","SPECIES_PIDGEY",3),
 ("Route2","SPECIES_PIDGEOTTO",6),
 ("Route2","SPECIES_RATTATA",3),
 ("Route2","SPECIES_RATICATE",6),
 ("Route2","SPECIES_SENTRET",4),
 ("Route2","SPECIES_FURRET",7),
 ("Route2","SPECIES_ZIGZAGOON",4),
 ("Route2","SPECIES_LINOONE",7),
 ("Route2","SPECIES_POOCHYENA",4),
 ("Route2","SPECIES_MIGHTYENA",7),

 # == ViridianForest: Bugs ==
 ("ViridianForest","SPECIES_CATERPIE",4),
 ("ViridianForest","SPECIES_METAPOD",5),
 ("ViridianForest","SPECIES_BUTTERFREE",8),
 ("ViridianForest","SPECIES_WEEDLE",4),
 ("ViridianForest","SPECIES_KAKUNA",5),
 ("ViridianForest","SPECIES_BEEDRILL",8),
 ("ViridianForest","SPECIES_WURMPLE",4),
 ("ViridianForest","SPECIES_SILCOON",5),
 ("ViridianForest","SPECIES_BEAUTIFLY",8),
 ("ViridianForest","SPECIES_CASCOON",5),
 ("ViridianForest","SPECIES_DUSTOX",8),
 ("ViridianForest","SPECIES_SURSKIT",6),

 # == Route3: Flying/Normal ==
 ("Route3","SPECIES_SPEAROW",4),
 ("Route3","SPECIES_FEAROW",7),
 ("Route3","SPECIES_JIGGLYPUFF",4),
 ("Route3","SPECIES_NIDORAN_F",4),
 ("Route3","SPECIES_NIDORINA",6),
 ("Route3","SPECIES_NIDORAN_M",4),
 ("Route3","SPECIES_NIDORINO",6),
 ("Route3","SPECIES_HOOTHOOT",5),
 ("Route3","SPECIES_NOCTOWL",8),
 ("Route3","SPECIES_TAILLOW",5),
 ("Route3","SPECIES_SWELLOW",8),
 ("Route3","SPECIES_SKITTY",5),

 # == MtMoon: Rock/Poison cave ==
 ("MtMoon","SPECIES_ZUBAT",8),
 ("MtMoon","SPECIES_GOLBAT",12),
 ("MtMoon","SPECIES_GEODUDE",8),
 ("MtMoon","SPECIES_GRAVELER",12),
 ("MtMoon","SPECIES_CLEFAIRY",9),
 ("MtMoon","SPECIES_CLEFABLE",13),
 ("MtMoon","SPECIES_EKANS",8),
 ("MtMoon","SPECIES_ARBOK",12),
 ("MtMoon","SPECIES_SANDSHREW",9),
 ("MtMoon","SPECIES_PARAS",9),
 ("MtMoon","SPECIES_NOSEPASS",10),
 ("MtMoon","SPECIES_ARON",10),

 # == Route4: Water starter + Psychic ==
 ("Route4","SPECIES_SQUIRTLE",8),
 ("Route4","SPECIES_WARTORTLE",12),
 ("Route4","SPECIES_PSYDUCK",9),
 ("Route4","SPECIES_GOLDUCK",13),
 ("Route4","SPECIES_SLOWPOKE",9),
 ("Route4","SPECIES_DROWZEE",9),
 ("Route4","SPECIES_HYPNO",13),
 ("Route4","SPECIES_MUDKIP",8),
 ("Route4","SPECIES_MARSHTOMP",12),
 ("Route4","SPECIES_AZURILL",8),
 ("Route4","SPECIES_WYNAUT",9),
 ("Route4","SPECIES_MARILL",9),

 # == Route22: Fire starter + Fire ==
 ("Route22","SPECIES_CHARMANDER",8),
 ("Route22","SPECIES_CHARMELEON",12),
 ("Route22","SPECIES_VULPIX",9),
 ("Route22","SPECIES_NINETALES",13),
 ("Route22","SPECIES_GROWLITHE",9),
 ("Route22","SPECIES_ARCANINE",13),
 ("Route22","SPECIES_PONYTA",9),
 ("Route22","SPECIES_RAPIDASH",13),
 ("Route22","SPECIES_SLUGMA",9),
 ("Route22","SPECIES_NUMEL",9),
 ("Route22","SPECIES_TORCHIC",9),
 ("Route22","SPECIES_PICHU",9),

 # == Route5: Grass/Poison ==
 ("Route5","SPECIES_ODDISH",12),
 ("Route5","SPECIES_GLOOM",16),
 ("Route5","SPECIES_VILEPLUME",20),
 ("Route5","SPECIES_BELLSPROUT",12),
 ("Route5","SPECIES_WEEPINBELL",16),
 ("Route5","SPECIES_VICTREEBEL",20),
 ("Route5","SPECIES_VENONAT",13),
 ("Route5","SPECIES_VENOMOTH",17),
 ("Route5","SPECIES_ROSELIA",15),
 ("Route5","SPECIES_CACNEA",14),
 ("Route5","SPECIES_CACTURNE",19),
 ("Route5","SPECIES_BELLOSSOM",18),

 # == Route6: Poison/Water (NO ghost) ==
 ("Route6","SPECIES_GRIMER",12),
 ("Route6","SPECIES_MUK",17),
 ("Route6","SPECIES_KOFFING",12),
 ("Route6","SPECIES_WEEZING",17),
 ("Route6","SPECIES_POLIWAG",12),
 ("Route6","SPECIES_POLIWHIRL",16),
 ("Route6","SPECIES_POLIWRATH",20),
 ("Route6","SPECIES_POLITOED",20),
 ("Route6","SPECIES_WOOPER",12),
 ("Route6","SPECIES_QUAGSIRE",17),
 ("Route6","SPECIES_SPINARAK",12),
 ("Route6","SPECIES_ARIADOS",17),

 # == Route7: Electric early (Voltorb here, not PowerPlant) ==
 ("Route7","SPECIES_PIKACHU",13),
 ("Route7","SPECIES_VOLTORB",13),
 ("Route7","SPECIES_MAGNEMITE",13),
 ("Route7","SPECIES_MAREEP",13),
 ("Route7","SPECIES_FLAAFFY",16),
 ("Route7","SPECIES_PLUSLE",14),
 ("Route7","SPECIES_MINUN",14),
 ("Route7","SPECIES_ELECTRIKE",13),
 ("Route7","SPECIES_ELEKID",13),
 ("Route7","SPECIES_LEDYBA",13),
 ("Route7","SPECIES_LEDIAN",17),
 ("Route7","SPECIES_MANECTRIC",17),

 # == Route8: Grass/Normal ==
 ("Route8","SPECIES_MEOWTH",13),
 ("Route8","SPECIES_PERSIAN",17),
 ("Route8","SPECIES_HOPPIP",13),
 ("Route8","SPECIES_SKIPLOOM",16),
 ("Route8","SPECIES_JUMPLUFF",20),
 ("Route8","SPECIES_LOTAD",13),
 ("Route8","SPECIES_LOMBRE",16),
 ("Route8","SPECIES_LUDICOLO",20),
 ("Route8","SPECIES_SEEDOT",13),
 ("Route8","SPECIES_NUZLEAF",16),
 ("Route8","SPECIES_SHROOMISH",14),
 ("Route8","SPECIES_BRELOOM",18),

 # == RockTunnel: Rock/Ground cave ==
 ("RockTunnel","SPECIES_ONIX",15),
 ("RockTunnel","SPECIES_MACHOP",15),
 ("RockTunnel","SPECIES_MACHOKE",19),
 ("RockTunnel","SPECIES_RHYHORN",15),
 ("RockTunnel","SPECIES_CUBONE",15),
 ("RockTunnel","SPECIES_MAROWAK",20),
 ("RockTunnel","SPECIES_LARVITAR",16),
 ("RockTunnel","SPECIES_PUPITAR",20),
 ("RockTunnel","SPECIES_BALTOY",16),
 ("RockTunnel","SPECIES_MAKUHITA",15),
 ("RockTunnel","SPECIES_NINCADA",15),
 ("RockTunnel","SPECIES_LAIRON",18),

 # == Route9: Bug/Dragon ==
 ("Route9","SPECIES_SCYTHER",20),
 ("Route9","SPECIES_PINSIR",20),
 ("Route9","SPECIES_HERACROSS",20),
 ("Route9","SPECIES_TRAPINCH",18),
 ("Route9","SPECIES_VIBRAVA",22),
 ("Route9","SPECIES_FLYGON",26),
 ("Route9","SPECIES_NINJASK",22),
 ("Route9","SPECIES_SHEDINJA",22),
 ("Route9","SPECIES_YANMA",20),
 ("Route9","SPECIES_MASQUERAIN",20),
 ("Route9","SPECIES_VOLBEAT",20),
 ("Route9","SPECIES_ILLUMISE",20),

 # == Route10: Ground/Rock/Misc ==
 ("Route10","SPECIES_DIGLETT",18),
 ("Route10","SPECIES_DUGTRIO",22),
 ("Route10","SPECIES_GOLEM",24),
 ("Route10","SPECIES_SHUCKLE",20),
 ("Route10","SPECIES_SUDOWOODO",20),
 ("Route10","SPECIES_CORSOLA",20),
 ("Route10","SPECIES_SWINUB",18),
 ("Route10","SPECIES_PILOSWINE",22),
 ("Route10","SPECIES_PHANPY",19),
 ("Route10","SPECIES_DONPHAN",24),
 ("Route10","SPECIES_SANDSLASH",21),
 ("Route10","SPECIES_CROBAT",22),

 # == Route11: Psychic ==
 ("Route11","SPECIES_ABRA",19),
 ("Route11","SPECIES_KADABRA",22),
 ("Route11","SPECIES_ALAKAZAM",26),
 ("Route11","SPECIES_RALTS",19),
 ("Route11","SPECIES_KIRLIA",22),
 ("Route11","SPECIES_GARDEVOIR",26),
 ("Route11","SPECIES_NATU",19),
 ("Route11","SPECIES_XATU",23),
 ("Route11","SPECIES_SPOINK",20),
 ("Route11","SPECIES_GRUMPIG",24),
 ("Route11","SPECIES_CHIMECHO",22),
 ("Route11","SPECIES_WOBBUFFET",21),

 # == Route12: Normal variety ==
 ("Route12","SPECIES_EXEGGCUTE",20),
 ("Route12","SPECIES_EXEGGUTOR",25),
 ("Route12","SPECIES_TANGELA",20),
 ("Route12","SPECIES_STANTLER",20),
 ("Route12","SPECIES_SMEARGLE",20),
 ("Route12","SPECIES_LICKITUNG",20),
 ("Route12","SPECIES_KANGASKHAN",22),
 ("Route12","SPECIES_TAUROS",22),
 ("Route12","SPECIES_MILTANK",22),
 ("Route12","SPECIES_GIRAFARIG",22),
 ("Route12","SPECIES_DUNSPARCE",20),
 ("Route12","SPECIES_AIPOM",20),

 # == Route13: Flying ==
 ("Route13","SPECIES_DODUO",20),
 ("Route13","SPECIES_DODRIO",25),
 ("Route13","SPECIES_FARFETCHD",20),
 ("Route13","SPECIES_PIDGEOT",25),
 ("Route13","SPECIES_WINGULL",20),
 ("Route13","SPECIES_PELIPPER",25),
 ("Route13","SPECIES_SWABLU",20),
 ("Route13","SPECIES_ALTARIA",26),
 ("Route13","SPECIES_MURKROW",21),
 ("Route13","SPECIES_SKARMORY",22),
 ("Route13","SPECIES_TOGETIC",22),
 ("Route13","SPECIES_TROPIUS",24),

 # == Route14: Poison/Dark/Bug ==
 ("Route14","SPECIES_NIDOQUEEN",24),
 ("Route14","SPECIES_NIDOKING",24),
 ("Route14","SPECIES_PARASECT",22),
 ("Route14","SPECIES_HOUNDOUR",22),
 ("Route14","SPECIES_HOUNDOOM",26),
 ("Route14","SPECIES_SABLEYE",22),
 ("Route14","SPECIES_SEVIPER",22),
 ("Route14","SPECIES_ZANGOOSE",22),
 ("Route14","SPECIES_PINECO",20),
 ("Route14","SPECIES_FORRETRESS",25),
 ("Route14","SPECIES_DELCATTY",22),
 ("Route14","SPECIES_ABSOL",25),

 # == Route15: Dark/Sound/Normal ==
 ("Route15","SPECIES_SNEASEL",23),
 ("Route15","SPECIES_TEDDIURSA",22),
 ("Route15","SPECIES_URSARING",27),
 ("Route15","SPECIES_SLAKOTH",22),
 ("Route15","SPECIES_VIGOROTH",25),
 ("Route15","SPECIES_SLAKING",30),
 ("Route15","SPECIES_SPINDA",22),
 ("Route15","SPECIES_WHISMUR",22),
 ("Route15","SPECIES_LOUDRED",25),
 ("Route15","SPECIES_EXPLOUD",30),
 ("Route15","SPECIES_GULPIN",23),
 ("Route15","SPECIES_SWALOT",27),

 # == Route16: Fighting ==
 ("Route16","SPECIES_HARIYAMA",27),
 ("Route16","SPECIES_MEDITITE",24),
 ("Route16","SPECIES_MEDICHAM",30),
 ("Route16","SPECIES_TYROGUE",24),
 ("Route16","SPECIES_HITMONLEE",30),
 ("Route16","SPECIES_HITMONCHAN",30),
 ("Route16","SPECIES_HITMONTOP",30),
 ("Route16","SPECIES_MACHAMP",32),
 ("Route16","SPECIES_PRIMEAPE",26),
 ("Route16","SPECIES_MANKEY",24),
 ("Route16","SPECIES_GRANBULL",27),
 ("Route16","SPECIES_SNUBBULL",24),

 # == Route17: Dragon/Flying + Rayquaza ==
 ("Route17","SPECIES_DRATINI",26),
 ("Route17","SPECIES_DRAGONAIR",30),
 ("Route17","SPECIES_DRAGONITE",36),
 ("Route17","SPECIES_BAGON",26),
 ("Route17","SPECIES_SHELGON",30),
 ("Route17","SPECIES_SALAMENCE",36),
 ("Route17","SPECIES_AERODACTYL",30),
 ("Route17","SPECIES_GLIGAR",27),
 ("Route17","SPECIES_HORSEA",26),
 ("Route17","SPECIES_SEADRA",30),
 ("Route17","SPECIES_RAYQUAZA",50),   # slot10 legendary
 ("Route17","SPECIES_KINGDRA",35),    # slot11

 # == Route18: Normal rare ==
 ("Route18","SPECIES_SNORLAX",28),
 ("Route18","SPECIES_IGGLYBUFF",24),
 ("Route18","SPECIES_CLEFFA",24),
 ("Route18","SPECIES_TOGEPI",24),
 ("Route18","SPECIES_CHANSEY",27),
 ("Route18","SPECIES_BLISSEY",33),
 ("Route18","SPECIES_MILOTIC",33),
 ("Route18","SPECIES_CASTFORM",26),
 ("Route18","SPECIES_KECLEON",26),
 ("Route18","SPECIES_LUVDISC",26),
 ("Route18","SPECIES_MAWILE",26),
 ("Route18","SPECIES_PORYGON",28),

 # == Route21North: Water/Shell ==
 ("Route21North","SPECIES_STARYU",26),
 ("Route21North","SPECIES_STARMIE",32),
 ("Route21North","SPECIES_SHELLDER",26),
 ("Route21North","SPECIES_CLOYSTER",32),
 ("Route21North","SPECIES_KRABBY",26),
 ("Route21North","SPECIES_KINGLER",32),
 ("Route21North","SPECIES_REMORAID",27),
 ("Route21North","SPECIES_OCTILLERY",33),
 ("Route21North","SPECIES_CLAMPERL",28),
 ("Route21North","SPECIES_HUNTAIL",33),
 ("Route21North","SPECIES_GOREBYSS",33),
 ("Route21North","SPECIES_RELICANTH",30),

 # == Route21South: Fossil/Grass ==
 ("Route21South","SPECIES_SUNKERN",26),
 ("Route21South","SPECIES_SUNFLORA",32),
 ("Route21South","SPECIES_LILEEP",27),
 ("Route21South","SPECIES_CRADILY",33),
 ("Route21South","SPECIES_ANORITH",27),
 ("Route21South","SPECIES_ARMALDO",33),
 ("Route21South","SPECIES_OMANYTE",28),
 ("Route21South","SPECIES_OMASTAR",33),
 ("Route21South","SPECIES_KABUTO",28),
 ("Route21South","SPECIES_KABUTOPS",33),
 ("Route21South","SPECIES_SHIFTRY",30),
 ("Route21South","SPECIES_WYNAUT",28),

 # == PokemonTower: Ghost ONLY + Moltres (slot10), MISDREAVUS dup (slot11) ==
 ("PokemonTower","SPECIES_GASTLY",32),
 ("PokemonTower","SPECIES_HAUNTER",36),
 ("PokemonTower","SPECIES_GENGAR",40),
 ("PokemonTower","SPECIES_MISDREAVUS",33),
 ("PokemonTower","SPECIES_DUSKULL",33),
 ("PokemonTower","SPECIES_DUSCLOPS",38),
 ("PokemonTower","SPECIES_SHUPPET",33),
 ("PokemonTower","SPECIES_BANETTE",38),
 ("PokemonTower","SPECIES_DITTO",34),
 ("PokemonTower","SPECIES_WIGGLYTUFF",36),
 ("PokemonTower","SPECIES_MOLTRES",50),    # slot10
 ("PokemonTower","SPECIES_MISDREAVUS",40), # slot11 - thematic dup

 # == PowerPlant: Electric evolved + heat (no Pikachu/Voltorb/Magnemite/Mareep - those Route7) ==
 ("PowerPlant","SPECIES_RAICHU",38),
 ("PowerPlant","SPECIES_MAGNETON",36),
 ("PowerPlant","SPECIES_ELECTRODE",38),
 ("PowerPlant","SPECIES_AMPHAROS",40),
 ("PowerPlant","SPECIES_JOLTEON",36),
 ("PowerPlant","SPECIES_ELECTABUZZ",36),
 ("PowerPlant","SPECIES_MAGMAR",36),
 ("PowerPlant","SPECIES_TORKOAL",34),
 ("PowerPlant","SPECIES_CAMERUPT",36),
 ("PowerPlant","SPECIES_MAGCARGO",36),
 ("PowerPlant","SPECIES_ZAPDOS",50),       # slot10
 ("PowerPlant","SPECIES_PORYGON2",38),     # slot11

 # == SafariZone: Hoenn/Kanto final starters + rares ==
 ("SafariZone","SPECIES_VENUSAUR",36),
 ("SafariZone","SPECIES_BLASTOISE",36),
 ("SafariZone","SPECIES_CHARIZARD",36),
 ("SafariZone","SPECIES_MEGANIUM",36),
 ("SafariZone","SPECIES_TYPHLOSION",36),
 ("SafariZone","SPECIES_FERALIGATR",36),
 ("SafariZone","SPECIES_SCEPTILE",36),
 ("SafariZone","SPECIES_BLAZIKEN",36),
 ("SafariZone","SPECIES_SWAMPERT",36),
 ("SafariZone","SPECIES_SCIZOR",34),
 ("SafariZone","SPECIES_HERACROSS",34),
 ("SafariZone","SPECIES_KANGASKHAN",34),

 # == Route23: Eeveelutions + Johto starters early ==
 ("Route23","SPECIES_EEVEE",32),
 ("Route23","SPECIES_ESPEON",36),
 ("Route23","SPECIES_UMBREON",36),
 ("Route23","SPECIES_FLAREON",36),
 ("Route23","SPECIES_VAPOREON",36),
 ("Route23","SPECIES_CHIKORITA",32),
 ("Route23","SPECIES_BAYLEEF",35),
 ("Route23","SPECIES_CYNDAQUIL",32),
 ("Route23","SPECIES_QUILAVA",35),
 ("Route23","SPECIES_TOTODILE",32),
 ("Route23","SPECIES_CROCONAW",35),
 ("Route23","SPECIES_GROVYLE",34),

 # == Route24: Ice + Regice/Latios ==
 ("Route24","SPECIES_SEEL",33),
 ("Route24","SPECIES_DEWGONG",38),
 ("Route24","SPECIES_SNORUNT",33),
 ("Route24","SPECIES_GLALIE",38),
 ("Route24","SPECIES_DELIBIRD",35),
 ("Route24","SPECIES_SMOOCHUM",33),
 ("Route24","SPECIES_SPHEAL",35),
 ("Route24","SPECIES_SEALEO",38),
 ("Route24","SPECIES_LAPRAS",38),
 ("Route24","SPECIES_JYNX",35),
 ("Route24","SPECIES_REGICE",40),    # slot10
 ("Route24","SPECIES_LATIOS",40),    # slot11

 # == Route25: Psychic/Steel + 4 legendaries ==
 ("Route25","SPECIES_LUNATONE",35),
 ("Route25","SPECIES_SOLROCK",35),
 ("Route25","SPECIES_SLOWKING",38),
 ("Route25","SPECIES_MR_MIME",34),
 ("Route25","SPECIES_CLAYDOL",36),
 ("Route25","SPECIES_BELDUM",34),
 ("Route25","SPECIES_METANG",38),
 ("Route25","SPECIES_METAGROSS",42),
 ("Route25","SPECIES_REGISTEEL",42),  # slot8 4%
 ("Route25","SPECIES_JIRACHI",42),    # slot9 4%
 ("Route25","SPECIES_CELEBI",45),     # slot10 1%
 ("Route25","SPECIES_DEOXYS",45),     # slot11 1%

 # == Seafoam: Ice/Water deep - Walrein + rare variants + Kyogre/Articuno/Lugia ==
 # Available unique cold/water species not used above:
 # Walrein (Sealeo->Walrein chain: Sealeo in R24, Walrein free)
 # Slowbro (Slowpoke in R4, Slowbro free)
 # Azumarill (Marill in R4, Azumarill free)
 # Wigglytuff -> PokemonTower has it. Use something else.
 # Let me check what's FREE here: Treecko/Combusken/Swampert-alternatives...
 # After all assignments: free species include:
 # Treecko, Combusken (Torchic R22, Blaziken SafariZone - but Combusken is the middle evo!)
 # Actually Torchic->Combusken->Blaziken: Torchic=R22, Blaziken=Safari, Combusken=FREE!
 # Same for Treecko->Grovyle->Sceptile: Grovyle=R23, Sceptile=Safari, Treecko=FREE!
 # Swampert: SafariZone has it. Mudkip/Marshtomp: Route4. So that line is covered.
 # Other free: Magby (only Magmar in PowerPlant, Elekid in Route7 - Magby not assigned!)
 # Slowbro (free!), Azumarill (free!), Wigglytuff (PokemonTower)
 # Wait - PokemonTower has Wigglytuff... let me replace that with something better
 # PokemonTower slot 9 (Wigglytuff) -> change to MISDREAVUS (but that's already slots 3,11)
 # Hmm. PokemonTower needs 10 unique non-legendary species + Moltres + Misdreavus(dup)
 # Ghost types: Gastly, Haunter, Gengar, Misdreavus, Duskull, Dusclops, Shuppet, Banette = 8
 # Slots 9,10 (non-legendary regular): Ditto, Wigglytuff -> Ditto is fine, Wigglytuff feels off
 # Replace Wigglytuff in PokemonTower with SLOWBRO (Psychic/tower theme)
 # Then Wigglytuff is FREE for Seafoam or CeruleanCave
 # Seafoam: Walrein, Slowbro->replace with WIGGLYTUFF? or just use Slowbro in Seafoam
 # Route4 has Slowpoke. Slowbro is free -> use in Seafoam or CeruleanCave
 # Let's put in Seafoam:
 ("Seafoam","SPECIES_WALREIN",48),
 ("Seafoam","SPECIES_SLOWBRO",45),
 ("Seafoam","SPECIES_AZUMARILL",48),
 ("Seafoam","SPECIES_TREECKO",44),     # rare appearance
 ("Seafoam","SPECIES_COMBUSKEN",44),   # rare appearance
 ("Seafoam","SPECIES_MAGBY",44),       # rare baby
 ("Seafoam","SPECIES_WIGGLYTUFF",44),  # Wait - PokemonTower has Wigglytuff! Fix: remove from PT
 # -> PokemonTower slot 9: change from Wigglytuff to something else
 # Let's use STEELIX in PT slot 9 (steel/ghost has synergy?) - but Steelix goes in VR
 # Or use SNUBBULL in PT slot 9 (also in Route16! No)
 # OK: PokemonTower slot 9 = MAGCARGO (fire/rock - NOT in PowerPlant... wait, Magcargo IS in PowerPlant!)
 # PokemonTower slot 9 = SLOWBRO -> then Seafoam can't use Slowbro...
 # This is getting circular. Let me just use completely different species in those slots.
 # PokemonTower slot 9: SNORLAX (also Route18! No)
 # PokemonTower slot 9: PORYGON (also Route18! No - Route18 has it)
 # PokemonTower non-ghost filler options (not used elsewhere):
 # - MISDREAVUS (already slots 3, 11 - can't add more)
 # - SLOWBRO: free, psychic, fits tower
 # - AZUMARILL: free, doesn't fit tower
 # - TREECKO: free, doesn't fit tower
 # Best: PT slot 9 = SLOWBRO (Psychic fits ghost tower), slot 10 = MOLTRES
 # Then Seafoam: loses Slowbro, use AZUMARILL + something else
 # For Seafoam, the 8 non-legendary slots:
 # 1=Walrein, 2=Azumarill, 3=Treecko, 4=Combusken, 5=Magby, 6=?, 7=?, 8-beforeKyogre=?
 # Free species not yet placed: Wigglytuff (if removed from PT), Steelix (VR has it? check)
 # VR: needs unique strong Pokemon. Currently plan: Steelix, Rhydon, Tyranitar, Aggron, Suicune, HoOh + legends
 # Let me just finalize EVERYTHING properly now.
 ("Seafoam","SPECIES_KYOGRE",50),       # slot8 4%
 ("Seafoam","SPECIES_STANTLER",46),     # Wait - Route12 has Stantler!
 ("Seafoam","SPECIES_ARTICUNO",50),     # slot10
 ("Seafoam","SPECIES_LUGIA",50),        # slot11

 # == VictoryRoad: Rock/Steel/Dragon + Regirock/Groudon ==
 # Available strong species not used: Steelix(RockTunnel has Onix but not Steelix->Steelix FREE)
 # Rhydon: RockTunnel has Rhyhorn but NOT Rhydon -> Rhydon free!
 # Tyranitar: RockTunnel has Larvitar/Pupitar but NOT Tyranitar -> free!
 # Aggron: RockTunnel has Lairon but NOT Aggron -> free!
 # Suicune, HO-OH, Onix(RockTunnel has it)
 # Machamp: Route16 has it. Dragonite/Salamence: Route17 has them.
 # Onix: RockTunnel has it. Steelix: free!
 ("VictoryRoad","SPECIES_STEELIX",47),
 ("VictoryRoad","SPECIES_RHYDON",45),
 ("VictoryRoad","SPECIES_TYRANITAR",48),
 ("VictoryRoad","SPECIES_AGGRON",46),
 ("VictoryRoad","SPECIES_SUICUNE",48),
 ("VictoryRoad","SPECIES_HO_OH",50),
 ("VictoryRoad","SPECIES_AERODACTYL",46), # Route17 has Aerodactyl! Remove from VR
 # -> VR slot 7: use NIDOKING level 45? No, Route14 has Nidoking.
 # -> Use PARASECT (Route14)? No.
 # Truly free strong species: Slowbro (if not in PT or Seafoam)
 # Let me track what's truly free:
 # Placed so far in ASSIGNMENTS (excluding the problematic ones above):
 # All 32*12 - the conflicting ones... this is getting too complex.
 # I'll use a programmatic approach below to identify free species.
 ("VictoryRoad","SPECIES_MAGMAR",46), # Wait - PowerPlant has Magmar!
 ("VictoryRoad","SPECIES_PRIMEAPE",45), # Route16 has Primeape!
 ("VictoryRoad","SPECIES_REGIROCK",45), # slot10
 ("VictoryRoad","SPECIES_GROUDON",45),  # slot11

 # == CeruleanCave: Psychic/Rare + Mew/Mewtwo ==
 ("CeruleanCave","SPECIES_DITTO",47),   # PokemonTower has Ditto!
 ("CeruleanCave","SPECIES_WOBBUFFET",47), # Route11 has Wobbuffet!
 ("CeruleanCave","SPECIES_CLEFABLE",48), # MtMoon has Clefable!
 ("CeruleanCave","SPECIES_WIGGLYTUFF",48), # PokemonTower (if kept) has it
 ("CeruleanCave","SPECIES_POLITOED",48),  # Route6 has Politoed!
 ("CeruleanCave","SPECIES_POLIWRATH",48), # Route6 has Poliwrath!
 ("CeruleanCave","SPECIES_AZUMARILL",48), # Seafoam
 ("CeruleanCave","SPECIES_QUAGSIRE",48),  # Route6!
 ("CeruleanCave","SPECIES_PORYGON2",48),  # PowerPlant!
 ("CeruleanCave","SPECIES_FORRETRESS",48),# Route14!
 ("CeruleanCave","SPECIES_MEW",50),       # slot10
 ("CeruleanCave","SPECIES_MEWTWO",70),    # slot11
]

# =====================================================================
# VALIDATE and show errors
# =====================================================================
from collections import defaultdict
area_counts = defaultdict(int)
sp_areas = defaultdict(list)
for area, sp, lv in ASSIGNMENTS:
    area_counts[area] += 1
    sp_areas[sp].append(area)

print(f"\nTotal assignments: {len(ASSIGNMENTS)}")
print("\nAreas with wrong count:")
for area, cnt in sorted(area_counts.items()):
    if cnt != 12:
        print(f"  {area}: {cnt}")

print("\nCross-area duplicates:")
dup_count = 0
for sp, areas in sp_areas.items():
    unique = list(set(areas))
    if len(unique) > 1:
        print(f"  {sp}: {unique}")
        dup_count += 1
print(f"Total cross-area dups: {dup_count}")

# Show what's UNASSIGNED from ALL
assigned_sp = set(sp for _, sp, _ in ASSIGNMENTS if sp != "SPECIES_MISDREAVUS" or _ == "PokemonTower")
# Actually just track unique assigned
assigned_unique = set()
for area, sp, lv in ASSIGNMENTS:
    assigned_unique.add(sp)
all_set = set(ALL)
missing = all_set - assigned_unique
print(f"\nUnassigned species ({len(missing)}):")
for s in sorted(missing):
    print(f"  {s}")
