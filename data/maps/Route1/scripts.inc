Route1_MapScripts::
	.byte 0

Route1_EventScript_NorthGate::
	goto_if_set FLAG_STARTER_CHOSEN, Route1_EventScript_NorthGate_Pass
	lockall
	applymovement LOCALID_PLAYER, Route1_Movement_PushBack
	waitmovement 0
	msgbox Route1_Text_NoPassWithoutPokemon, MSGBOX_DEFAULT
	releaseall
	end

Route1_EventScript_NorthGate_Pass::
	end

Route1_Movement_PushBack:
	walk_down
	walk_down
	walk_down
	step_end

Route1_EventScript_MartClerk::
	lock
	faceplayer
	goto_if_set FLAG_GOT_ROUTE1_BERRY_1, Route1_EventScript_MartClerkDone
	msgbox Route1_Text_MartClerk, MSGBOX_DEFAULT
	giveitem ITEM_ORAN_BERRY
	setflag FLAG_GOT_ROUTE1_BERRY_1
	release
	end

Route1_EventScript_MartClerkDone::
	release
	end

Route1_EventScript_Boy::
	lock
	faceplayer
	goto_if_set FLAG_GOT_ROUTE1_BERRY_2, Route1_EventScript_BoyDone
	msgbox Route1_Text_Boy, MSGBOX_DEFAULT
	giveitem ITEM_PECHA_BERRY
	setflag FLAG_GOT_ROUTE1_BERRY_2
	release
	end

Route1_EventScript_BoyDone::
	release
	end

Route1_EventScript_RouteSign::
	msgbox Route1_Text_RouteSign, MSGBOX_SIGN
	end

Route1_EventScript_NorthBlockade::
	specialvar VAR_RESULT, GetPlayerFacingDirection
	goto_if_eq VAR_RESULT, DIR_SOUTH, Route1_EventScript_NorthBlockadePass
	goto_if_set FLAG_STARTER_CHOSEN, Route1_EventScript_NorthBlockadePass
	lock
	msgbox Route1_Text_NorthBlockade
	release
	end

Route1_EventScript_NorthBlockadePass::
	end

Route1_EventScript_StoneHouseMan::
	lock
	faceplayer
	msgbox Route1_Text_StoneHouseMan, MSGBOX_DEFAULT
	giveitem ITEM_ENIGMA_BERRY
	release
	end

Route1_Text_StoneHouseMan::
	.string "I've been waiting here\nfor seventeen years.\p"
	.string "I'm not sure what for.\p"
	.string "Take this.\p"
	.string "I don't need it\nanymore.$"

Route1_Text_MartClerk:
	.string "I've been walking\nthis route every day.\p"
	.string "I always find these\nnear the tall grass.\p"
	.string "Take one.$"

Route1_Text_Boy:
	.string "My mom said I could\ngo as far as Erynval.\p"
	.string "I found this on\nthe ground.\p"
	.string "You can have it.$"
