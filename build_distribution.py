#!/usr/bin/env python3
"""
Helper: generate the complete unique species distribution across 32 areas.
Outputs Python dict for apply_encounters.py
"""

# All 386 Gen1-3 species in National Dex order
# Excluded (roamers): RAIKOU(243), ENTEI(244), LATIAS(380)
ALL_SPECIES = [
    "SPECIES_BULBASAUR",      # 1
    "SPECIES_IVYSAUR",        # 2
    "SPECIES_VENUSAUR",       # 3
    "SPECIES_CHARMANDER",     # 4
    "SPECIES_CHARMELEON",     # 5
    "SPECIES_CHARIZARD",      # 6
    "SPECIES_SQUIRTLE",       # 7
    "SPECIES_WARTORTLE",      # 8
    "SPECIES_BLASTOISE",      # 9
    "SPECIES_CATERPIE",       # 10
    "SPECIES_METAPOD",        # 11
    "SPECIES_BUTTERFREE",     # 12
    "SPECIES_WEEDLE",         # 13
    "SPECIES_KAKUNA",         # 14
    "SPECIES_BEEDRILL",       # 15
    "SPECIES_PIDGEY",         # 16
    "SPECIES_PIDGEOTTO",      # 17
    "SPECIES_PIDGEOT",        # 18
    "SPECIES_RATTATA",        # 19
    "SPECIES_RATICATE",       # 20
    "SPECIES_SPEAROW",        # 21
    "SPECIES_FEAROW",         # 22
    "SPECIES_EKANS",          # 23
    "SPECIES_ARBOK",          # 24
    "SPECIES_PIKACHU",        # 25
    "SPECIES_RAICHU",         # 26
    "SPECIES_SANDSHREW",      # 27
    "SPECIES_SANDSLASH",      # 28
    "SPECIES_NIDORAN_F",      # 29
    "SPECIES_NIDORINA",       # 30
    "SPECIES_NIDOQUEEN",      # 31
    "SPECIES_NIDORAN_M",      # 32
    "SPECIES_NIDORINO",       # 33
    "SPECIES_NIDOKING",       # 34
    "SPECIES_CLEFAIRY",       # 35
    "SPECIES_CLEFABLE",       # 36
    "SPECIES_VULPIX",         # 37
    "SPECIES_NINETALES",      # 38
    "SPECIES_JIGGLYPUFF",     # 39
    "SPECIES_WIGGLYTUFF",     # 40
    "SPECIES_ZUBAT",          # 41
    "SPECIES_GOLBAT",         # 42
    "SPECIES_ODDISH",         # 43
    "SPECIES_GLOOM",          # 44
    "SPECIES_VILEPLUME",      # 45
    "SPECIES_PARAS",          # 46
    "SPECIES_PARASECT",       # 47
    "SPECIES_VENONAT",        # 48
    "SPECIES_VENOMOTH",       # 49
    "SPECIES_DIGLETT",        # 50
    "SPECIES_DUGTRIO",        # 51
    "SPECIES_MEOWTH",         # 52
    "SPECIES_PERSIAN",        # 53
    "SPECIES_PSYDUCK",        # 54
    "SPECIES_GOLDUCK",        # 55
    "SPECIES_MANKEY",         # 56
    "SPECIES_PRIMEAPE",       # 57
    "SPECIES_GROWLITHE",      # 58
    "SPECIES_ARCANINE",       # 59
    "SPECIES_POLIWAG",        # 60
    "SPECIES_POLIWHIRL",      # 61
    "SPECIES_POLIWRATH",      # 62
    "SPECIES_ABRA",           # 63
    "SPECIES_KADABRA",        # 64
    "SPECIES_ALAKAZAM",       # 65
    "SPECIES_MACHOP",         # 66
    "SPECIES_MACHOKE",        # 67
    "SPECIES_MACHAMP",        # 68
    "SPECIES_BELLSPROUT",     # 69
    "SPECIES_WEEPINBELL",     # 70
    "SPECIES_VICTREEBEL",     # 71
    "SPECIES_TENTACOOL",      # 72 - water
    "SPECIES_TENTACRUEL",     # 73 - water
    "SPECIES_GEODUDE",        # 74
    "SPECIES_GRAVELER",       # 75
    "SPECIES_GOLEM",          # 76
    "SPECIES_PONYTA",         # 77
    "SPECIES_RAPIDASH",       # 78
    "SPECIES_SLOWPOKE",       # 79
    "SPECIES_SLOWBRO",        # 80
    "SPECIES_MAGNEMITE",      # 81
    "SPECIES_MAGNETON",       # 82
    "SPECIES_FARFETCHD",      # 83
    "SPECIES_DODUO",          # 84
    "SPECIES_DODRIO",         # 85
    "SPECIES_SEEL",           # 86
    "SPECIES_DEWGONG",        # 87
    "SPECIES_GRIMER",         # 88
    "SPECIES_MUK",            # 89
    "SPECIES_SHELLDER",       # 90
    "SPECIES_CLOYSTER",       # 91
    "SPECIES_GASTLY",         # 92
    "SPECIES_HAUNTER",        # 93
    "SPECIES_GENGAR",         # 94
    "SPECIES_ONIX",           # 95
    "SPECIES_DROWZEE",        # 96
    "SPECIES_HYPNO",          # 97
    "SPECIES_KRABBY",         # 98
    "SPECIES_KINGLER",        # 99
    "SPECIES_VOLTORB",        # 100
    "SPECIES_ELECTRODE",      # 101
    "SPECIES_EXEGGCUTE",      # 102
    "SPECIES_EXEGGUTOR",      # 103
    "SPECIES_CUBONE",         # 104
    "SPECIES_MAROWAK",        # 105
    "SPECIES_HITMONLEE",      # 106
    "SPECIES_HITMONCHAN",     # 107
    "SPECIES_LICKITUNG",      # 108
    "SPECIES_KOFFING",        # 109
    "SPECIES_WEEZING",        # 110
    "SPECIES_RHYHORN",        # 111
    "SPECIES_RHYDON",         # 112
    "SPECIES_CHANSEY",        # 113
    "SPECIES_TANGELA",        # 114
    "SPECIES_KANGASKHAN",     # 115
    "SPECIES_HORSEA",         # 116
    "SPECIES_SEADRA",         # 117
    "SPECIES_GOLDEEN",        # 118 - water
    "SPECIES_SEAKING",        # 119 - water
    "SPECIES_STARYU",         # 120
    "SPECIES_STARMIE",        # 121
    "SPECIES_MR_MIME",        # 122
    "SPECIES_SCYTHER",        # 123
    "SPECIES_JYNX",           # 124
    "SPECIES_ELECTABUZZ",     # 125
    "SPECIES_MAGMAR",         # 126
    "SPECIES_PINSIR",         # 127
    "SPECIES_TAUROS",         # 128
    "SPECIES_MAGIKARP",       # 129 - water
    "SPECIES_GYARADOS",       # 130 - water
    "SPECIES_LAPRAS",         # 131
    "SPECIES_DITTO",          # 132
    "SPECIES_EEVEE",          # 133
    "SPECIES_VAPOREON",       # 134
    "SPECIES_JOLTEON",        # 135
    "SPECIES_FLAREON",        # 136
    "SPECIES_PORYGON",        # 137
    "SPECIES_OMANYTE",        # 138
    "SPECIES_OMASTAR",        # 139
    "SPECIES_KABUTO",         # 140
    "SPECIES_KABUTOPS",       # 141
    "SPECIES_AERODACTYL",     # 142
    "SPECIES_SNORLAX",        # 143
    "SPECIES_ARTICUNO",       # 144 - legendary Seafoam slot 10
    "SPECIES_ZAPDOS",         # 145 - legendary PowerPlant slot 10
    "SPECIES_MOLTRES",        # 146 - legendary PokemonTower slot 10
    "SPECIES_DRATINI",        # 147
    "SPECIES_DRAGONAIR",      # 148
    "SPECIES_DRAGONITE",      # 149
    "SPECIES_MEWTWO",         # 150 - legendary CeruleanCave slot 11
    "SPECIES_MEW",            # 151 - legendary CeruleanCave slot 10
    "SPECIES_CHIKORITA",      # 152
    "SPECIES_BAYLEEF",        # 153
    "SPECIES_MEGANIUM",       # 154
    "SPECIES_CYNDAQUIL",      # 155
    "SPECIES_QUILAVA",        # 156
    "SPECIES_TYPHLOSION",     # 157
    "SPECIES_TOTODILE",       # 158
    "SPECIES_CROCONAW",       # 159
    "SPECIES_FERALIGATR",     # 160
    "SPECIES_SENTRET",        # 161
    "SPECIES_FURRET",         # 162
    "SPECIES_HOOTHOOT",       # 163
    "SPECIES_NOCTOWL",        # 164
    "SPECIES_LEDYBA",         # 165
    "SPECIES_LEDIAN",         # 166
    "SPECIES_SPINARAK",       # 167
    "SPECIES_ARIADOS",        # 168
    "SPECIES_CROBAT",         # 169
    "SPECIES_CHINCHOU",       # 170 - water
    "SPECIES_LANTURN",        # 171 - water
    "SPECIES_PICHU",          # 172
    "SPECIES_CLEFFA",         # 173
    "SPECIES_IGGLYBUFF",      # 174
    "SPECIES_TOGEPI",         # 175
    "SPECIES_TOGETIC",        # 176
    "SPECIES_NATU",           # 177
    "SPECIES_XATU",           # 178
    "SPECIES_MAREEP",         # 179
    "SPECIES_FLAAFFY",        # 180
    "SPECIES_AMPHAROS",       # 181
    "SPECIES_BELLOSSOM",      # 182
    "SPECIES_MARILL",         # 183
    "SPECIES_AZUMARILL",      # 184
    "SPECIES_SUDOWOODO",      # 185
    "SPECIES_POLITOED",       # 186
    "SPECIES_HOPPIP",         # 187
    "SPECIES_SKIPLOOM",       # 188
    "SPECIES_JUMPLUFF",       # 189
    "SPECIES_AIPOM",          # 190
    "SPECIES_SUNKERN",        # 191
    "SPECIES_SUNFLORA",       # 192
    "SPECIES_YANMA",          # 193
    "SPECIES_WOOPER",         # 194
    "SPECIES_QUAGSIRE",       # 195
    "SPECIES_ESPEON",         # 196
    "SPECIES_UMBREON",        # 197
    "SPECIES_MURKROW",        # 198
    "SPECIES_SLOWKING",       # 199
    "SPECIES_MISDREAVUS",     # 200
    "SPECIES_UNOWN",          # 201 - kept in Tanoby Ruins only, skip here
    "SPECIES_WOBBUFFET",      # 202
    "SPECIES_GIRAFARIG",      # 203
    "SPECIES_PINECO",         # 204
    "SPECIES_FORRETRESS",     # 205
    "SPECIES_DUNSPARCE",      # 206
    "SPECIES_GLIGAR",         # 207
    "SPECIES_STEELIX",        # 208
    "SPECIES_SNUBBULL",       # 209
    "SPECIES_GRANBULL",       # 210
    "SPECIES_QWILFISH",       # 211 - water
    "SPECIES_SCIZOR",         # 212
    "SPECIES_SHUCKLE",        # 213
    "SPECIES_HERACROSS",      # 214
    "SPECIES_SNEASEL",        # 215
    "SPECIES_TEDDIURSA",      # 216
    "SPECIES_URSARING",       # 217
    "SPECIES_SLUGMA",         # 218
    "SPECIES_MAGCARGO",       # 219
    "SPECIES_SWINUB",         # 220
    "SPECIES_PILOSWINE",      # 221
    "SPECIES_CORSOLA",        # 222
    "SPECIES_REMORAID",       # 223
    "SPECIES_OCTILLERY",      # 224
    "SPECIES_DELIBIRD",       # 225
    "SPECIES_MANTINE",        # 226 - water
    "SPECIES_SKARMORY",       # 227
    "SPECIES_HOUNDOUR",       # 228
    "SPECIES_HOUNDOOM",       # 229
    "SPECIES_KINGDRA",        # 230
    "SPECIES_PHANPY",         # 231
    "SPECIES_DONPHAN",        # 232
    "SPECIES_PORYGON2",       # 233
    "SPECIES_STANTLER",       # 234
    "SPECIES_SMEARGLE",       # 235
    "SPECIES_TYROGUE",        # 236
    "SPECIES_HITMONTOP",      # 237
    "SPECIES_SMOOCHUM",       # 238
    "SPECIES_ELEKID",         # 239
    "SPECIES_MAGBY",          # 240
    "SPECIES_MILTANK",        # 241
    "SPECIES_BLISSEY",        # 242
    # 243 RAIKOU - excluded
    # 244 ENTEI - excluded
    "SPECIES_SUICUNE",        # 245
    "SPECIES_LARVITAR",       # 246
    "SPECIES_PUPITAR",        # 247
    "SPECIES_TYRANITAR",      # 248
    "SPECIES_LUGIA",          # 249 - legendary Seafoam slot 11
    "SPECIES_HO_OH",          # 250
    "SPECIES_CELEBI",         # 251 - legendary Route25 slot 10
    "SPECIES_TREECKO",        # 252
    "SPECIES_GROVYLE",        # 253
    "SPECIES_SCEPTILE",       # 254
    "SPECIES_TORCHIC",        # 255
    "SPECIES_COMBUSKEN",      # 256
    "SPECIES_BLAZIKEN",       # 257
    "SPECIES_MUDKIP",         # 258
    "SPECIES_MARSHTOMP",      # 259
    "SPECIES_SWAMPERT",       # 260
    "SPECIES_POOCHYENA",      # 261
    "SPECIES_MIGHTYENA",      # 262
    "SPECIES_ZIGZAGOON",      # 263
    "SPECIES_LINOONE",        # 264
    "SPECIES_WURMPLE",        # 265
    "SPECIES_SILCOON",        # 266
    "SPECIES_BEAUTIFLY",      # 267
    "SPECIES_CASCOON",        # 268
    "SPECIES_DUSTOX",         # 269
    "SPECIES_LOTAD",          # 270
    "SPECIES_LOMBRE",         # 271
    "SPECIES_LUDICOLO",       # 272
    "SPECIES_SEEDOT",         # 273
    "SPECIES_NUZLEAF",        # 274
    "SPECIES_SHIFTRY",        # 275
    "SPECIES_TAILLOW",        # 276
    "SPECIES_SWELLOW",        # 277
    "SPECIES_WINGULL",        # 278
    "SPECIES_PELIPPER",       # 279
    "SPECIES_RALTS",          # 280
    "SPECIES_KIRLIA",         # 281
    "SPECIES_GARDEVOIR",      # 282
    "SPECIES_SURSKIT",        # 283
    "SPECIES_MASQUERAIN",     # 284
    "SPECIES_SHROOMISH",      # 285
    "SPECIES_BRELOOM",        # 286
    "SPECIES_SLAKOTH",        # 287
    "SPECIES_VIGOROTH",       # 288
    "SPECIES_SLAKING",        # 289
    "SPECIES_NINCADA",        # 290
    "SPECIES_NINJASK",        # 291
    "SPECIES_SHEDINJA",       # 292
    "SPECIES_WHISMUR",        # 293
    "SPECIES_LOUDRED",        # 294
    "SPECIES_EXPLOUD",        # 295
    "SPECIES_MAKUHITA",       # 296
    "SPECIES_HARIYAMA",       # 297
    "SPECIES_AZURILL",        # 298
    "SPECIES_NOSEPASS",       # 299
    "SPECIES_SKITTY",         # 300
    "SPECIES_DELCATTY",       # 301
    "SPECIES_SABLEYE",        # 302
    "SPECIES_MAWILE",         # 303
    "SPECIES_ARON",           # 304
    "SPECIES_LAIRON",         # 305
    "SPECIES_AGGRON",         # 306
    "SPECIES_MEDITITE",       # 307
    "SPECIES_MEDICHAM",       # 308
    "SPECIES_ELECTRIKE",      # 309
    "SPECIES_MANECTRIC",      # 310
    "SPECIES_PLUSLE",         # 311
    "SPECIES_MINUN",          # 312
    "SPECIES_VOLBEAT",        # 313
    "SPECIES_ILLUMISE",       # 314
    "SPECIES_ROSELIA",        # 315
    "SPECIES_GULPIN",         # 316
    "SPECIES_SWALOT",         # 317
    "SPECIES_CARVANHA",       # 318 - water
    "SPECIES_SHARPEDO",       # 319 - water
    "SPECIES_WAILMER",        # 320 - water
    "SPECIES_WAILORD",        # 321 - water
    "SPECIES_NUMEL",          # 322
    "SPECIES_CAMERUPT",       # 323
    "SPECIES_TORKOAL",        # 324
    "SPECIES_SPINDA",         # 325
    "SPECIES_TRAPINCH",       # 326
    "SPECIES_VIBRAVA",        # 327
    "SPECIES_FLYGON",         # 328
    "SPECIES_CACNEA",         # 329
    "SPECIES_CACTURNE",       # 330
    "SPECIES_SWABLU",         # 331
    "SPECIES_ALTARIA",        # 332
    "SPECIES_ZANGOOSE",       # 333
    "SPECIES_SEVIPER",        # 334
    "SPECIES_LUNATONE",       # 335
    "SPECIES_SOLROCK",        # 336
    "SPECIES_BARBOACH",       # 337 - water
    "SPECIES_WHISCASH",       # 338 - water
    "SPECIES_CORPHISH",       # 339 - water
    "SPECIES_CRAWDAUNT",      # 340 - water
    "SPECIES_BALTOY",         # 341
    "SPECIES_CLAYDOL",        # 342
    "SPECIES_LILEEP",         # 343
    "SPECIES_CRADILY",        # 344
    "SPECIES_ANORITH",        # 345
    "SPECIES_ARMALDO",        # 346
    "SPECIES_FEEBAS",         # 347 - water
    "SPECIES_MILOTIC",        # 348
    "SPECIES_CASTFORM",       # 349
    "SPECIES_KECLEON",        # 350
    "SPECIES_SHUPPET",        # 351
    "SPECIES_BANETTE",        # 352
    "SPECIES_DUSKULL",        # 353
    "SPECIES_DUSCLOPS",       # 354
    "SPECIES_TROPIUS",        # 355
    "SPECIES_CHIMECHO",       # 356
    "SPECIES_ABSOL",          # 357
    "SPECIES_WYNAUT",         # 358
    "SPECIES_SNORUNT",        # 359
    "SPECIES_GLALIE",         # 360
    "SPECIES_SPHEAL",         # 361
    "SPECIES_SEALEO",         # 362
    "SPECIES_WALREIN",        # 363
    "SPECIES_CLAMPERL",       # 364
    "SPECIES_HUNTAIL",        # 365
    "SPECIES_GOREBYSS",       # 366
    "SPECIES_RELICANTH",      # 367
    "SPECIES_LUVDISC",        # 368
    "SPECIES_BAGON",          # 369
    "SPECIES_SHELGON",        # 370
    "SPECIES_SALAMENCE",      # 371
    "SPECIES_BELDUM",         # 372
    "SPECIES_METANG",         # 373
    "SPECIES_METAGROSS",      # 374
    "SPECIES_REGIROCK",       # 375 - legendary VictoryRoad slot 10
    "SPECIES_REGICE",         # 376 - legendary Route24 slot 10
    "SPECIES_REGISTEEL",      # 377 - legendary Route25 slot 8
    "SPECIES_LATIOS",         # 378 - legendary Route24 slot 11
    # 380 LATIAS - excluded
    "SPECIES_KYOGRE",         # 382 - legendary Seafoam slot 8
    "SPECIES_GROUDON",        # 383 - legendary VictoryRoad slot 11
    "SPECIES_RAYQUAZA",       # 384 - legendary Route17 slot 10
    "SPECIES_JIRACHI",        # 385 - legendary Route25 slot 9
    "SPECIES_DEOXYS",         # 386 - legendary Route25 slot 11
    # 379 REGISTEEL already added as 377 (keep original numbering)
    # 381 LATIOS already added as 378
]

# Now manually assign - let me print a clean dict
# I'll organize them thematically into 32 buckets of 12

areas = {
    "Route2": [],
    "ViridianForest": [],
    "Route3": [],
    "MtMoon": [],
    "Route4": [],
    "Route22": [],
    "Route5": [],
    "Route6": [],
    "Route7": [],
    "Route8": [],
    "RockTunnel": [],
    "Route9": [],
    "Route10": [],
    "Route11": [],
    "Route12": [],
    "Route13": [],
    "Route14": [],
    "Route15": [],
    "Route16": [],
    "Route17": [],
    "Route18": [],
    "Route21North": [],
    "Route21South": [],
    "PokemonTower": [],
    "PowerPlant": [],
    "SafariZone": [],
    "Route23": [],
    "Route24": [],
    "Route25": [],
    "Seafoam": [],
    "VictoryRoad": [],
    "CeruleanCave": [],
}

# Manually curated - thematic + unique assignment
# Format: (area, species, level)
# Total non-UNOWN assignable: 383 (excluding RAIKOU, ENTEI, LATIAS, UNOWN)
# But the 32 areas have 32*12=384 slots.
# One slot is filled by a thematic duplicate.

assignments = [
# ========== Route2: Starter evolution lines + early Normal (lv 3-8) ==========
("Route2", "SPECIES_BULBASAUR",   3),
("Route2", "SPECIES_IVYSAUR",     5),
("Route2", "SPECIES_PIDGEY",      3),
("Route2", "SPECIES_PIDGEOTTO",   6),
("Route2", "SPECIES_RATTATA",     3),
("Route2", "SPECIES_RATICATE",    6),
("Route2", "SPECIES_SENTRET",     4),
("Route2", "SPECIES_FURRET",      7),
("Route2", "SPECIES_ZIGZAGOON",   4),
("Route2", "SPECIES_LINOONE",     7),
("Route2", "SPECIES_POOCHYENA",   4),
("Route2", "SPECIES_MIGHTYENA",   7),

# ========== ViridianForest: Bug types (lv 4-8) ==========
("ViridianForest", "SPECIES_CATERPIE",    4),
("ViridianForest", "SPECIES_METAPOD",     5),
("ViridianForest", "SPECIES_BUTTERFREE",  8),
("ViridianForest", "SPECIES_WEEDLE",      4),
("ViridianForest", "SPECIES_KAKUNA",      5),
("ViridianForest", "SPECIES_BEEDRILL",    8),
("ViridianForest", "SPECIES_WURMPLE",     4),
("ViridianForest", "SPECIES_SILCOON",     5),
("ViridianForest", "SPECIES_BEAUTIFLY",   8),
("ViridianForest", "SPECIES_CASCOON",     5),
("ViridianForest", "SPECIES_DUSTOX",      8),
("ViridianForest", "SPECIES_SURSKIT",     6),

# ========== Route3: Flying + Normal early (lv 4-8) ==========
("Route3", "SPECIES_SPEAROW",     4),
("Route3", "SPECIES_FEAROW",      7),
("Route3", "SPECIES_JIGGLYPUFF",  4),
("Route3", "SPECIES_WIGGLYTUFF",  7),
("Route3", "SPECIES_NIDORAN_F",   4),
("Route3", "SPECIES_NIDORINA",    6),
("Route3", "SPECIES_NIDORAN_M",   4),
("Route3", "SPECIES_NIDORINO",    6),
("Route3", "SPECIES_HOOTHOOT",    5),
("Route3", "SPECIES_NOCTOWL",     8),
("Route3", "SPECIES_TAILLOW",     5),
("Route3", "SPECIES_SWELLOW",     8),

# ========== MtMoon: Rock/Poison/Cave (lv 8-14) ==========
("MtMoon", "SPECIES_ZUBAT",       8),
("MtMoon", "SPECIES_GOLBAT",     12),
("MtMoon", "SPECIES_GEODUDE",     8),
("MtMoon", "SPECIES_GRAVELER",   12),
("MtMoon", "SPECIES_CLEFAIRY",    9),
("MtMoon", "SPECIES_CLEFABLE",   13),
("MtMoon", "SPECIES_EKANS",       8),
("MtMoon", "SPECIES_ARBOK",      12),
("MtMoon", "SPECIES_SANDSHREW",   9),
("MtMoon", "SPECIES_PARAS",       9),
("MtMoon", "SPECIES_NOSEPASS",   10),
("MtMoon", "SPECIES_ARON",       10),

# ========== Route4: Water starter + Psychic/Water (lv 8-14) ==========
("Route4", "SPECIES_SQUIRTLE",    8),
("Route4", "SPECIES_WARTORTLE",  12),
("Route4", "SPECIES_PSYDUCK",     9),
("Route4", "SPECIES_GOLDUCK",    13),
("Route4", "SPECIES_SLOWPOKE",    9),
("Route4", "SPECIES_SLOWBRO",    13),
("Route4", "SPECIES_DROWZEE",     9),
("Route4", "SPECIES_HYPNO",      13),
("Route4", "SPECIES_WOOPER",      9),
("Route4", "SPECIES_MARILL",      9),
("Route4", "SPECIES_AZURILL",     8),
("Route4", "SPECIES_WYNAUT",      9),

# ========== Route22: Fire starter + Fire types (lv 8-14) ==========
("Route22", "SPECIES_CHARMANDER",  8),
("Route22", "SPECIES_CHARMELEON", 12),
("Route22", "SPECIES_VULPIX",      9),
("Route22", "SPECIES_NINETALES",  13),
("Route22", "SPECIES_GROWLITHE",   9),
("Route22", "SPECIES_ARCANINE",   13),
("Route22", "SPECIES_PONYTA",      9),
("Route22", "SPECIES_RAPIDASH",   13),
("Route22", "SPECIES_SLUGMA",      9),
("Route22", "SPECIES_NUMEL",       9),
("Route22", "SPECIES_TORCHIC",     9),
("Route22", "SPECIES_PICHU",       9),

# ========== Route5: Grass/Poison (lv 12-20) ==========
("Route5", "SPECIES_ODDISH",     12),
("Route5", "SPECIES_GLOOM",      16),
("Route5", "SPECIES_VILEPLUME",  20),
("Route5", "SPECIES_BELLSPROUT", 12),
("Route5", "SPECIES_WEEPINBELL", 16),
("Route5", "SPECIES_VICTREEBEL", 20),
("Route5", "SPECIES_VENONAT",    13),
("Route5", "SPECIES_VENOMOTH",   17),
("Route5", "SPECIES_ROSELIA",    15),
("Route5", "SPECIES_CACNEA",     14),
("Route5", "SPECIES_CACTURNE",   19),
("Route5", "SPECIES_TROPIUS",    18),

# ========== Route6: Ghost/Poison (lv 12-20) ==========
("Route6", "SPECIES_GASTLY",     12),
("Route6", "SPECIES_HAUNTER",    16),
("Route6", "SPECIES_GENGAR",     20),
("Route6", "SPECIES_GRIMER",     12),
("Route6", "SPECIES_MUK",        17),
("Route6", "SPECIES_KOFFING",    12),
("Route6", "SPECIES_WEEZING",    17),
("Route6", "SPECIES_MISDREAVUS", 14),
("Route6", "SPECIES_SHUPPET",    14),
("Route6", "SPECIES_BANETTE",    18),
("Route6", "SPECIES_DUSKULL",    14),
("Route6", "SPECIES_DUSCLOPS",   19),

# ========== Route7: Electric (lv 13-20) ==========
("Route7", "SPECIES_PIKACHU",    13),
("Route7", "SPECIES_RAICHU",     18),
("Route7", "SPECIES_MAGNEMITE",  13),
("Route7", "SPECIES_MAGNETON",   17),
("Route7", "SPECIES_VOLTORB",    13),
("Route7", "SPECIES_ELECTRODE",  18),
("Route7", "SPECIES_ELECTRIKE",  13),
("Route7", "SPECIES_MANECTRIC",  18),
("Route7", "SPECIES_MAREEP",     13),
("Route7", "SPECIES_FLAAFFY",    16),
("Route7", "SPECIES_AMPHAROS",   20),
("Route7", "SPECIES_PLUSLE",     14),

# ========== Route8: Grass/Normal (lv 13-20) ==========
("Route8", "SPECIES_MINUN",      14),
("Route8", "SPECIES_MEOWTH",     13),
("Route8", "SPECIES_PERSIAN",    17),
("Route8", "SPECIES_HOPPIP",     13),
("Route8", "SPECIES_SKIPLOOM",   16),
("Route8", "SPECIES_JUMPLUFF",   20),
("Route8", "SPECIES_LOTAD",      13),
("Route8", "SPECIES_LOMBRE",     16),
("Route8", "SPECIES_SEEDOT",     13),
("Route8", "SPECIES_NUZLEAF",    16),
("Route8", "SPECIES_SHROOMISH",  14),
("Route8", "SPECIES_BRELOOM",    18),

# ========== RockTunnel: Rock/Ground/Fighting (lv 15-22) ==========
("RockTunnel", "SPECIES_ONIX",      15),
("RockTunnel", "SPECIES_MACHOP",    15),
("RockTunnel", "SPECIES_MACHOKE",   19),
("RockTunnel", "SPECIES_RHYHORN",   15),
("RockTunnel", "SPECIES_CUBONE",    15),
("RockTunnel", "SPECIES_MAROWAK",   20),
("RockTunnel", "SPECIES_LARVITAR",  16),
("RockTunnel", "SPECIES_PUPITAR",   20),
("RockTunnel", "SPECIES_LAIRON",    18),
("RockTunnel", "SPECIES_BALTOY",    16),
("RockTunnel", "SPECIES_MAKUHITA",  15),
("RockTunnel", "SPECIES_NINCADA",   15),

# ========== Route9: Bug/Ground/Dragon early (lv 18-26) ==========
("Route9", "SPECIES_SCYTHER",    20),
("Route9", "SPECIES_PINSIR",     20),
("Route9", "SPECIES_HERACROSS",  20),
("Route9", "SPECIES_TRAPINCH",   18),
("Route9", "SPECIES_VIBRAVA",    22),
("Route9", "SPECIES_FLYGON",     26),
("Route9", "SPECIES_NINJASK",    22),
("Route9", "SPECIES_SHEDINJA",   22),
("Route9", "SPECIES_YANMA",      20),
("Route9", "SPECIES_ARIADOS",    20),
("Route9", "SPECIES_VOLBEAT",    20),
("Route9", "SPECIES_ILLUMISE",   20),

# ========== Route10: Rock/Ground/Electric (lv 18-26) ==========
("Route10", "SPECIES_DIGLETT",   18),
("Route10", "SPECIES_DUGTRIO",   22),
("Route10", "SPECIES_GOLEM",     24),
("Route10", "SPECIES_SHUCKLE",   20),
("Route10", "SPECIES_SUDOWOODO", 20),
("Route10", "SPECIES_CORSOLA",   20),
("Route10", "SPECIES_SWINUB",    18),
("Route10", "SPECIES_PILOSWINE", 22),
("Route10", "SPECIES_PHANPY",    19),
("Route10", "SPECIES_DONPHAN",   24),
("Route10", "SPECIES_SANDSLASH", 21),
("Route10", "SPECIES_CROBAT",    22),

# ========== Route11: Psychic/Normal (lv 19-27) ==========
("Route11", "SPECIES_ABRA",      19),
("Route11", "SPECIES_KADABRA",   22),
("Route11", "SPECIES_ALAKAZAM",  26),
("Route11", "SPECIES_RALTS",     19),
("Route11", "SPECIES_KIRLIA",    22),
("Route11", "SPECIES_GARDEVOIR", 26),
("Route11", "SPECIES_NATU",      19),
("Route11", "SPECIES_XATU",      23),
("Route11", "SPECIES_SPOINK",    20),
("Route11", "SPECIES_GRUMPIG",   24),
("Route11", "SPECIES_CHIMECHO",  22),
("Route11", "SPECIES_WOBBUFFET", 21),

# ========== Route12: Normal variety (lv 19-27) ==========
("Route12", "SPECIES_EXEGGCUTE", 20),
("Route12", "SPECIES_EXEGGUTOR", 25),
("Route12", "SPECIES_TANGELA",   20),
("Route12", "SPECIES_STANTLER",  20),
("Route12", "SPECIES_SMEARGLE",  20),
("Route12", "SPECIES_LICKITUNG", 20),
("Route12", "SPECIES_KANGASKHAN",22),
("Route12", "SPECIES_TAUROS",    22),
("Route12", "SPECIES_MILTANK",   22),
("Route12", "SPECIES_GIRAFARIG", 22),
("Route12", "SPECIES_DUNSPARCE", 20),
("Route12", "SPECIES_AIPOM",     20),

# ========== Route13: Flying (lv 20-28) ==========
("Route13", "SPECIES_DODUO",     20),
("Route13", "SPECIES_DODRIO",    25),
("Route13", "SPECIES_FARFETCHD", 20),
("Route13", "SPECIES_PIDGEOT",   25),
("Route13", "SPECIES_WINGULL",   20),
("Route13", "SPECIES_PELIPPER",  25),
("Route13", "SPECIES_SWABLU",    20),
("Route13", "SPECIES_ALTARIA",   26),
("Route13", "SPECIES_MURKROW",   21),
("Route13", "SPECIES_SKARMORY",  22),
("Route13", "SPECIES_TOGETIC",   22),
("Route13", "SPECIES_LUDICOLO",  24),

# ========== Route14: Poison/Dark/Bug (lv 20-28) ==========
("Route14", "SPECIES_SPINARAK",  20),
("Route14", "SPECIES_LEDYBA",    20),
("Route14", "SPECIES_LEDIAN",    24),
("Route14", "SPECIES_NIDOQUEEN", 26),
("Route14", "SPECIES_NIDOKING",  26),
("Route14", "SPECIES_PARASECT",  22),
("Route14", "SPECIES_HOUNDOUR",  22),
("Route14", "SPECIES_HOUNDOOM",  26),
("Route14", "SPECIES_ABSOL",     24),
("Route14", "SPECIES_SABLEYE",   22),
("Route14", "SPECIES_SEVIPER",   22),
("Route14", "SPECIES_ZANGOOSE",  22),

# ========== Route15: Dark/Normal (lv 22-30) ==========
("Route15", "SPECIES_SNEASEL",   23),
("Route15", "SPECIES_TEDDIURSA", 22),
("Route15", "SPECIES_URSARING",  27),
("Route15", "SPECIES_SLAKOTH",   22),
("Route15", "SPECIES_VIGOROTH",  25),
("Route15", "SPECIES_SLAKING",   30),
("Route15", "SPECIES_SPINDA",    22),
("Route15", "SPECIES_LOUDRED",   25),
("Route15", "SPECIES_EXPLOUD",   30),
("Route15", "SPECIES_WHISMUR",   22),
("Route15", "SPECIES_GULPIN",    23),
("Route15", "SPECIES_SWALOT",    27),

# ========== Route16: Fighting/Ground (lv 24-34) ==========
("Route16", "SPECIES_HARIYAMA",  27),
("Route16", "SPECIES_MEDITITE",  24),
("Route16", "SPECIES_MEDICHAM",  30),
("Route16", "SPECIES_TYROGUE",   24),
("Route16", "SPECIES_HITMONLEE", 30),
("Route16", "SPECIES_HITMONCHAN",30),
("Route16", "SPECIES_HITMONTOP", 30),
("Route16", "SPECIES_MACHAMP",   32),
("Route16", "SPECIES_PRIMEAPE",  26),
("Route16", "SPECIES_MANKEY",    24),
("Route16", "SPECIES_GRANBULL",  27),
("Route16", "SPECIES_SNUBBULL",  24),

# ========== Route17: Dragon/Flying + Rayquaza (lv 26-36) ==========
("Route17", "SPECIES_DRATINI",   26),
("Route17", "SPECIES_DRAGONAIR", 30),
("Route17", "SPECIES_DRAGONITE", 36),
("Route17", "SPECIES_BAGON",     26),
("Route17", "SPECIES_SHELGON",   30),
("Route17", "SPECIES_SALAMENCE", 36),
("Route17", "SPECIES_AERODACTYL",30),
("Route17", "SPECIES_GLIGAR",    27),
("Route17", "SPECIES_HORSEA",    26),
("Route17", "SPECIES_SEADRA",    30),
("Route17", "SPECIES_RAYQUAZA",  50),  # slot 10 - legendary
("Route17", "SPECIES_KINGDRA",   35),  # slot 11

# ========== Route18: Normal/Misc (lv 24-33) ==========
("Route18", "SPECIES_SNORLAX",   28),
("Route18", "SPECIES_IGGLYBUFF", 24),
("Route18", "SPECIES_CLEFFA",    24),
("Route18", "SPECIES_TOGEPI",    24),
("Route18", "SPECIES_CHANSEY",   27),
("Route18", "SPECIES_BLISSEY",   33),
("Route18", "SPECIES_MILOTIC",   33),
("Route18", "SPECIES_CASTFORM",  26),
("Route18", "SPECIES_KECLEON",   26),
("Route18", "SPECIES_LUVDISC",   26),
("Route18", "SPECIES_MAWILE",    26),
("Route18", "SPECIES_PORYGON",   28),

# ========== Route21North: Water/Shell (lv 26-35) ==========
("Route21North", "SPECIES_STARYU",    26),
("Route21North", "SPECIES_STARMIE",   32),
("Route21North", "SPECIES_SHELLDER",  26),
("Route21North", "SPECIES_CLOYSTER",  32),
("Route21North", "SPECIES_KRABBY",    26),
("Route21North", "SPECIES_KINGLER",   32),
("Route21North", "SPECIES_REMORAID",  27),
("Route21North", "SPECIES_OCTILLERY", 33),
("Route21North", "SPECIES_CLAMPERL",  28),
("Route21North", "SPECIES_HUNTAIL",   33),
("Route21North", "SPECIES_GOREBYSS",  33),
("Route21North", "SPECIES_RELICANTH", 30),

# ========== Route21South: Fossil/Grass (lv 26-35) ==========
("Route21South", "SPECIES_SUNKERN",   26),
("Route21South", "SPECIES_SUNFLORA",  32),
("Route21South", "SPECIES_BELLOSSOM", 30),
("Route21South", "SPECIES_LILEEP",    27),
("Route21South", "SPECIES_CRADILY",   33),
("Route21South", "SPECIES_ANORITH",   27),
("Route21South", "SPECIES_ARMALDO",   33),
("Route21South", "SPECIES_OMANYTE",   28),
("Route21South", "SPECIES_OMASTAR",   33),
("Route21South", "SPECIES_KABUTO",    28),
("Route21South", "SPECIES_KABUTOPS",  33),
("Route21South", "SPECIES_TROPIUS",   30),  # duplicate thematic - used instead of UNOWN

# ========== PokemonTower: Ghost only + Moltres (lv 32-42) ==========
("PokemonTower", "SPECIES_GASTLY",    32),
("PokemonTower", "SPECIES_HAUNTER",   36),
("PokemonTower", "SPECIES_GENGAR",    40),
("PokemonTower", "SPECIES_MISDREAVUS",33),
("PokemonTower", "SPECIES_DUSKULL",   33),
("PokemonTower", "SPECIES_DUSCLOPS",  38),
("PokemonTower", "SPECIES_SHUPPET",   33),
("PokemonTower", "SPECIES_BANETTE",   38),
("PokemonTower", "SPECIES_SABLEYE",   34),
("PokemonTower", "SPECIES_ABSOL",     36),
("PokemonTower", "SPECIES_MOLTRES",   50),  # slot 10 - legendary
("PokemonTower", "SPECIES_MISDREAVUS",40),  # slot 11 - thematic duplicate (ghost only in tower)

# ========== PowerPlant: Electric only + Zapdos (lv 32-42) ==========
("PowerPlant", "SPECIES_MAGNEMITE",  32),
("PowerPlant", "SPECIES_MAGNETON",   36),
("PowerPlant", "SPECIES_VOLTORB",    32),
("PowerPlant", "SPECIES_ELECTRODE",  38),
("PowerPlant", "SPECIES_PIKACHU",    32),
("PowerPlant", "SPECIES_RAICHU",     38),
("PowerPlant", "SPECIES_ELECTRIKE",  33),
("PowerPlant", "SPECIES_MANECTRIC",  38),
("PowerPlant", "SPECIES_JOLTEON",    36),
("PowerPlant", "SPECIES_ELECTABUZZ", 36),
("PowerPlant", "SPECIES_ZAPDOS",     50),  # slot 10 - legendary
("PowerPlant", "SPECIES_AMPHAROS",   40),  # slot 11 - regular

# ========== SafariZone: Rare exotic mix (lv 30-42) ==========
("SafariZone", "SPECIES_SCIZOR",     32),
("SafariZone", "SPECIES_VENUSAUR",   36),
("SafariZone", "SPECIES_BLASTOISE",  36),
("SafariZone", "SPECIES_CHARIZARD",  36),
("SafariZone", "SPECIES_MEGANIUM",   36),
("SafariZone", "SPECIES_TYPHLOSION", 36),
("SafariZone", "SPECIES_FERALIGATR", 36),
("SafariZone", "SPECIES_SCEPTILE",   36),
("SafariZone", "SPECIES_BLAZIKEN",   36),
("SafariZone", "SPECIES_SWAMPERT",   36),
("SafariZone", "SPECIES_MAGCARGO",   33),
("SafariZone", "SPECIES_TORKOAL",    33),

# ========== Route23: Eeveelutions + Johto starters (lv 32-40) ==========
("Route23", "SPECIES_EEVEE",      32),
("Route23", "SPECIES_ESPEON",     36),
("Route23", "SPECIES_UMBREON",    36),
("Route23", "SPECIES_FLAREON",    36),
("Route23", "SPECIES_VAPOREON",   36),
("Route23", "SPECIES_CHIKORITA",  32),
("Route23", "SPECIES_BAYLEEF",    35),
("Route23", "SPECIES_CYNDAQUIL",  32),
("Route23", "SPECIES_QUILAVA",    35),
("Route23", "SPECIES_TOTODILE",   32),
("Route23", "SPECIES_CROCONAW",   35),
("Route23", "SPECIES_GROVYLE",    34),

# ========== Route24: Ice/Water + Regice/Latios (lv 33-43) ==========
("Route24", "SPECIES_SEEL",       33),
("Route24", "SPECIES_DEWGONG",    38),
("Route24", "SPECIES_SNORUNT",    33),
("Route24", "SPECIES_GLALIE",     38),
("Route24", "SPECIES_DELIBIRD",   35),
("Route24", "SPECIES_LAPRAS",     38),
("Route24", "SPECIES_JYNX",       35),
("Route24", "SPECIES_SMOOCHUM",   33),
("Route24", "SPECIES_SPHEAL",     35),
("Route24", "SPECIES_SEALEO",     38),
("Route24", "SPECIES_REGICE",     40),  # slot 10 - legendary
("Route24", "SPECIES_LATIOS",     40),  # slot 11 - legendary

# ========== Route25: Psychic rare + 4 event legendaries (lv 33-45) ==========
("Route25", "SPECIES_LUNATONE",   35),
("Route25", "SPECIES_SOLROCK",    35),
("Route25", "SPECIES_SLOWKING",   38),
("Route25", "SPECIES_MR_MIME",    34),
("Route25", "SPECIES_PORYGON2",   36),
("Route25", "SPECIES_CLAYDOL",    36),
("Route25", "SPECIES_BELDUM",     34),
("Route25", "SPECIES_METANG",     38),
("Route25", "SPECIES_REGISTEEL",  42),  # slot 8 - 4%
("Route25", "SPECIES_JIRACHI",    42),  # slot 9 - 4%
("Route25", "SPECIES_CELEBI",     45),  # slot 10 - 1%
("Route25", "SPECIES_DEOXYS",     45),  # slot 11 - 1%

# ========== Seafoam: Ice/Water caves + Articuno/Lugia (lv 42-52) ==========
("Seafoam", "SPECIES_WALREIN",    48),
("Seafoam", "SPECIES_CLOYSTER",   45),
("Seafoam", "SPECIES_LAPRAS",     45),
("Seafoam", "SPECIES_DEWGONG",    45),
("Seafoam", "SPECIES_SEEL",       42),
("Seafoam", "SPECIES_GLALIE",     45),
("Seafoam", "SPECIES_SNEASEL",    44),
("Seafoam", "SPECIES_PILOSWINE",  46),
("Seafoam", "SPECIES_KYOGRE",     50),  # slot 8 - 4%
("Seafoam", "SPECIES_JYNX",       44),  # slot 9
("Seafoam", "SPECIES_ARTICUNO",   50),  # slot 10 - 1%
("Seafoam", "SPECIES_LUGIA",      50),  # slot 11 - 1%

# ========== VictoryRoad: Dragon/Rock/Fighting + Regirock/Groudon (lv 42-52) ==========
("VictoryRoad", "SPECIES_MACHAMP",    44),
("VictoryRoad", "SPECIES_ONIX",       43),
("VictoryRoad", "SPECIES_STEELIX",    47),
("VictoryRoad", "SPECIES_RHYDON",     45),
("VictoryRoad", "SPECIES_DRAGONITE",  48),
("VictoryRoad", "SPECIES_SALAMENCE",  48),
("VictoryRoad", "SPECIES_TYRANITAR",  48),
("VictoryRoad", "SPECIES_AGGRON",     46),
("VictoryRoad", "SPECIES_METAGROSS",  48),
("VictoryRoad", "SPECIES_SUICUNE",    48),
("VictoryRoad", "SPECIES_REGIROCK",   45),  # slot 10 - legendary
("VictoryRoad", "SPECIES_GROUDON",    45),  # slot 11 - legendary

# ========== CeruleanCave: Psychic/Rare + Mew/Mewtwo (lv 45-55) ==========
("CeruleanCave", "SPECIES_DITTO",      47),
("CeruleanCave", "SPECIES_WOBBUFFET",  47),
("CeruleanCave", "SPECIES_CLEFABLE",   48),
("CeruleanCave", "SPECIES_WIGGLYTUFF", 48),
("CeruleanCave", "SPECIES_POLITOED",   48),
("CeruleanCave", "SPECIES_POLIWRATH",  48),
("CeruleanCave", "SPECIES_AZUMARILL",  48),
("CeruleanCave", "SPECIES_QUAGSIRE",   48),
("CeruleanCave", "SPECIES_HO_OH",      50),
("CeruleanCave", "SPECIES_FORRETRESS", 48),
("CeruleanCave", "SPECIES_MEW",        50),  # slot 10 - legendary
("CeruleanCave", "SPECIES_MEWTWO",     70),  # slot 11 - legendary
]

def validate_assignments(assignments):
    from collections import defaultdict
    area_mons = defaultdict(list)
    species_areas = defaultdict(list)
    errors = []

    for area, sp, lv in assignments:
        area_mons[area].append(sp)
        species_areas[sp].append(area)

    # Check each area has 12
    for area, mons in area_mons.items():
        if len(mons) != 12:
            errors.append(f"  ERROR: {area} has {len(mons)} mons (expected 12)")

    # Check cross-area duplicates (allow within-area for PokemonTower/PowerPlant ONLY)
    allowed_intra = {"PokemonTower", "PowerPlant"}
    for sp, areas_list in species_areas.items():
        unique_areas = list(set(areas_list))
        if len(unique_areas) > 1:
            # Check if it's the Seafoam reuse (allowed thematic)
            errors.append(f"  DUP ACROSS AREAS: {sp} in {unique_areas}")

    # Check total
    total = sum(len(v) for v in area_mons.values())
    print(f"Total slots: {total} (expected 384)")
    print(f"Unique species assigned: {len(species_areas)}")

    # Find species not assigned (excluding UNOWN, RAIKOU, ENTEI, LATIAS, and water-only)
    water_only = {
        "SPECIES_TENTACOOL", "SPECIES_TENTACRUEL", "SPECIES_GOLDEEN", "SPECIES_SEAKING",
        "SPECIES_MAGIKARP", "SPECIES_GYARADOS", "SPECIES_CHINCHOU", "SPECIES_LANTURN",
        "SPECIES_QWILFISH", "SPECIES_MANTINE", "SPECIES_CARVANHA", "SPECIES_SHARPEDO",
        "SPECIES_WAILMER", "SPECIES_WAILORD", "SPECIES_BARBOACH", "SPECIES_WHISCASH",
        "SPECIES_CORPHISH", "SPECIES_CRAWDAUNT", "SPECIES_FEEBAS",
    }
    excluded = {"SPECIES_UNOWN", "SPECIES_RAIKOU", "SPECIES_ENTEI", "SPECIES_LATIAS"}
    all_sp = set(ALL_SPECIES) - excluded - water_only

    assigned = set(species_areas.keys())
    missing = all_sp - assigned
    if missing:
        print(f"\nMissing species ({len(missing)}):")
        for s in sorted(missing):
            print(f"  {s}")

    extra = assigned - set(ALL_SPECIES)
    if extra:
        print(f"\nUnknown species: {extra}")

    return errors, area_mons

errors, area_mons = validate_assignments(assignments)
if errors:
    print("\nERRORS:")
    for e in errors:
        print(e)
else:
    print("\nValidation PASSED!")

# Print the dict for copy-paste into apply_encounters.py
print("\n\n# ===== AREA_MONS DICT =====")
for area, mons_list in area_mons.items():
    print(f'"{area}": [')
    # Get levels too
    for a, sp, lv in assignments:
        if a == area:
            print(f'    ("{sp}", {lv}),')
    print('],')
