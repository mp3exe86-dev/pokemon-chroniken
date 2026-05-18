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
	goto_if_set FLAG_GOT_POTION_ON_ROUTE_1, Route1_EventScript_AlreadyGotPotion
	msgbox Route1_Text_WorkAtPokeMartTakeSample
	textcolor NPC_TEXT_COLOR_NEUTRAL
	checkitemspace ITEM_POTION
	goto_if_eq VAR_RESULT, FALSE, EventScript_BagIsFull
	bufferitemname STR_VAR_2, ITEM_POTION
	playfanfare MUS_LEVEL_UP
	message Text_ObtainedTheX
	waitmessage
	waitfanfare
	additem ITEM_POTION
	msgbox Route1_Text_PutPotionAway
	call EventScript_RestorePrevTextColor
	setflag FLAG_GOT_POTION_ON_ROUTE_1
	release
	end

Route1_EventScript_AlreadyGotPotion::
	msgbox Route1_Text_ComeSeeUsIfYouNeedPokeBalls
	release
	end

Route1_EventScript_Boy::
	msgbox Route1_Text_CanJumpFromLedges, MSGBOX_NPC
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
	.string "...Take this.\p"
	.string "I don't need it\nanymore.$"
