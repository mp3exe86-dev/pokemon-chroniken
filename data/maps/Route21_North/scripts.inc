Route21_North_MapScripts::
	.byte 0


Route21_North_EventScript_AbsolBall::
	lockall
	setflag FLAG_HIDE_ROUTE21_NORTH_ITEM_ABSOL
	givemon SPECIES_ABSOL, 15, ITEM_NONE
	goto_if_eq VAR_RESULT, 2, EventScript_NoMoreRoomForPokemon
	playfanfare MUS_OBTAIN_ITEM
	msgbox Route21_North_Text_AbsolBall, MSGBOX_DEFAULT
	waitfanfare
	releaseall
	end

Route21_North_Text_AbsolBall::
	.string "Found a POKé BALL!\nA strange Pokémon\nwas inside...$"

Route21_North_EventScript_FossilScientist::
	lock
	faceplayer
	msgbox Route21_North_House_Text_FossilScientist, MSGBOX_DEFAULT
	givemon SPECIES_ABSOL, 10, ITEM_NONE
	setflag FLAG_HIDE_ROUTE21_NORTH_SCIENTIST
	release
	end

Route21_North_House_Text_FossilScientist::
	.string "I found this one\nnear the old stones.\p"
	.string "It wouldn't leave.\p"
	.string "I think it was\nwaiting for someone.\p"
	.string "Take it.$"

Route21_North_EventScript_TestNPC::
	lock
	faceplayer
	goto_if_set FLAG_TEMP_1, Route21_North_EventScript_TestNPC_Done
	giveitem ITEM_HM02
	getpartysize
	copyvar VAR_0x8004, VAR_RESULT
	givemon SPECIES_PIDGEOT, 50, ITEM_NONE
	goto_if_eq VAR_0x8004, 0, Route21_North_EventScript_TestNPC_SetMove0
	goto_if_eq VAR_0x8004, 1, Route21_North_EventScript_TestNPC_SetMove1
	goto_if_eq VAR_0x8004, 2, Route21_North_EventScript_TestNPC_SetMove2
	goto_if_eq VAR_0x8004, 3, Route21_North_EventScript_TestNPC_SetMove3
	goto_if_eq VAR_0x8004, 4, Route21_North_EventScript_TestNPC_SetMove4
	goto Route21_North_EventScript_TestNPC_SetMove5

Route21_North_EventScript_TestNPC_SetMove0::
	setmonmove 0, 0, MOVE_FLY
	setmonmove 0, 1, MOVE_WING_ATTACK
	setmonmove 0, 2, MOVE_QUICK_ATTACK
	setmonmove 0, 3, MOVE_FEATHER_DANCE
	goto Route21_North_EventScript_TestNPC_Flags

Route21_North_EventScript_TestNPC_SetMove1::
	setmonmove 1, 0, MOVE_FLY
	setmonmove 1, 1, MOVE_WING_ATTACK
	setmonmove 1, 2, MOVE_QUICK_ATTACK
	setmonmove 1, 3, MOVE_FEATHER_DANCE
	goto Route21_North_EventScript_TestNPC_Flags

Route21_North_EventScript_TestNPC_SetMove2::
	setmonmove 2, 0, MOVE_FLY
	setmonmove 2, 1, MOVE_WING_ATTACK
	setmonmove 2, 2, MOVE_QUICK_ATTACK
	setmonmove 2, 3, MOVE_FEATHER_DANCE
	goto Route21_North_EventScript_TestNPC_Flags

Route21_North_EventScript_TestNPC_SetMove3::
	setmonmove 3, 0, MOVE_FLY
	setmonmove 3, 1, MOVE_WING_ATTACK
	setmonmove 3, 2, MOVE_QUICK_ATTACK
	setmonmove 3, 3, MOVE_FEATHER_DANCE
	goto Route21_North_EventScript_TestNPC_Flags

Route21_North_EventScript_TestNPC_SetMove4::
	setmonmove 4, 0, MOVE_FLY
	setmonmove 4, 1, MOVE_WING_ATTACK
	setmonmove 4, 2, MOVE_QUICK_ATTACK
	setmonmove 4, 3, MOVE_FEATHER_DANCE
	goto Route21_North_EventScript_TestNPC_Flags

Route21_North_EventScript_TestNPC_SetMove5::
	setmonmove 5, 0, MOVE_FLY
	setmonmove 5, 1, MOVE_WING_ATTACK
	setmonmove 5, 2, MOVE_QUICK_ATTACK
	setmonmove 5, 3, MOVE_FEATHER_DANCE

Route21_North_EventScript_TestNPC_Flags::
	giveitem ITEM_HM03
	getpartysize
	copyvar VAR_0x8004, VAR_RESULT
	givemon SPECIES_LAPRAS, 50, ITEM_NONE
	goto_if_eq VAR_0x8004, 0, Route21_North_EventScript_TestNPC_LaprasMove0
	goto_if_eq VAR_0x8004, 1, Route21_North_EventScript_TestNPC_LaprasMove1
	goto_if_eq VAR_0x8004, 2, Route21_North_EventScript_TestNPC_LaprasMove2
	goto_if_eq VAR_0x8004, 3, Route21_North_EventScript_TestNPC_LaprasMove3
	goto_if_eq VAR_0x8004, 4, Route21_North_EventScript_TestNPC_LaprasMove4
	goto Route21_North_EventScript_TestNPC_LaprasMove5

Route21_North_EventScript_TestNPC_LaprasMove0::
	setmonmove 0, 0, MOVE_SURF
	setmonmove 0, 1, MOVE_ICE_BEAM
	setmonmove 0, 2, MOVE_BODY_SLAM
	setmonmove 0, 3, MOVE_PSYCHIC
	goto Route21_North_EventScript_TestNPC_BadgeFlags

Route21_North_EventScript_TestNPC_LaprasMove1::
	setmonmove 1, 0, MOVE_SURF
	setmonmove 1, 1, MOVE_ICE_BEAM
	setmonmove 1, 2, MOVE_BODY_SLAM
	setmonmove 1, 3, MOVE_PSYCHIC
	goto Route21_North_EventScript_TestNPC_BadgeFlags

Route21_North_EventScript_TestNPC_LaprasMove2::
	setmonmove 2, 0, MOVE_SURF
	setmonmove 2, 1, MOVE_ICE_BEAM
	setmonmove 2, 2, MOVE_BODY_SLAM
	setmonmove 2, 3, MOVE_PSYCHIC
	goto Route21_North_EventScript_TestNPC_BadgeFlags

Route21_North_EventScript_TestNPC_LaprasMove3::
	setmonmove 3, 0, MOVE_SURF
	setmonmove 3, 1, MOVE_ICE_BEAM
	setmonmove 3, 2, MOVE_BODY_SLAM
	setmonmove 3, 3, MOVE_PSYCHIC
	goto Route21_North_EventScript_TestNPC_BadgeFlags

Route21_North_EventScript_TestNPC_LaprasMove4::
	setmonmove 4, 0, MOVE_SURF
	setmonmove 4, 1, MOVE_ICE_BEAM
	setmonmove 4, 2, MOVE_BODY_SLAM
	setmonmove 4, 3, MOVE_PSYCHIC
	goto Route21_North_EventScript_TestNPC_BadgeFlags

Route21_North_EventScript_TestNPC_LaprasMove5::
	setmonmove 5, 0, MOVE_SURF
	setmonmove 5, 1, MOVE_ICE_BEAM
	setmonmove 5, 2, MOVE_BODY_SLAM
	setmonmove 5, 3, MOVE_PSYCHIC

Route21_North_EventScript_TestNPC_BadgeFlags::
	setflag FLAG_BADGE01_GET
	setflag FLAG_BADGE02_GET
	setflag FLAG_BADGE03_GET
	setflag FLAG_BADGE04_GET
	setflag FLAG_BADGE05_GET
	setflag FLAG_BADGE06_GET
	setflag FLAG_BADGE07_GET
	setflag FLAG_BADGE08_GET
	setflag FLAG_WORLD_MAP_PALLET_TOWN
	setflag FLAG_WORLD_MAP_VIRIDIAN_CITY
	setflag FLAG_WORLD_MAP_PEWTER_CITY
	setflag FLAG_WORLD_MAP_CERULEAN_CITY
	setflag FLAG_WORLD_MAP_VERMILION_CITY
	setflag FLAG_WORLD_MAP_LAVENDER_TOWN
	setflag FLAG_WORLD_MAP_CELADON_CITY
	setflag FLAG_WORLD_MAP_FUCHSIA_CITY
	setflag FLAG_WORLD_MAP_SAFFRON_CITY
	setflag FLAG_WORLD_MAP_CINNABAR_ISLAND
	setflag FLAG_WORLD_MAP_INDIGO_PLATEAU_EXTERIOR
	setflag FLAG_TEMP_1
	msgbox Route21_North_Text_TestNPC, MSGBOX_DEFAULT
	release
	end

Route21_North_EventScript_TestNPC_Done::
	msgbox Route21_North_Text_TestNPC_Done, MSGBOX_DEFAULT
	release
	end

Route21_North_Text_TestNPC::
	.string "Take these.\nYou'll need them\nfor testing.$"

Route21_North_Text_TestNPC_Done::
	.string "Come back later.$"
