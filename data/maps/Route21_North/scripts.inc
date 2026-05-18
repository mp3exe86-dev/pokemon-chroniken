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
