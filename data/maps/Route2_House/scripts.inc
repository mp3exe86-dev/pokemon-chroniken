Route2_House_MapScripts::
	.byte 0

Route2_House_EventScript_FossilScientist::
	lock
	faceplayer
	msgbox Route2_House_Text_FossilScientist, MSGBOX_DEFAULT
	givemon SPECIES_ABSOL, 10, ITEM_NONE
	setflag FLAG_HIDE_ROUTE21_NORTH_SCIENTIST
	release
	end

Route2_House_Text_FossilScientist::
	.string "I found this one\nnear the old stones.\p"
	.string "It wouldn't leave.\p"
	.string "I think it was\nwaiting for someone.\p"
	.string "Take it.$"

Route2_House_EventScript_Researcher::
	goto_if_set FLAG_ROUTE2_HOUSE_RESEARCHER_DONE, Route2_House_EventScript_Researcher_After
	lock
	faceplayer
	msgbox Route2_House_Text_Researcher, MSGBOX_DEFAULT
	giveitem ITEM_ENIGMA_BERRY
	setflag FLAG_ROUTE2_HOUSE_RESEARCHER_DONE
	release
	end

Route2_House_EventScript_Researcher_After::
	lock
	faceplayer
	msgbox Route2_House_Text_Researcher_After, MSGBOX_DEFAULT
	release
	end

Route2_House_Text_Researcher::
	.string "I've been mapping\nthese routes for years.\p"
	.string "Something changed\nthree winters ago.\p"
	.string "The Pokemon started\nmoving differently.\p"
	.string "Like they knew\nsomething was coming.\p"
	.string "Take this. You'll\nneed it out there.$"

Route2_House_Text_Researcher_After::
	.string "Don't ask me what\nit does.\p"
	.string "I'm not sure\nanyone knows.$"

Route2_House_EventScript_Scientist::
	msgbox Route2_House_Text_FaintedMonsCanUseFieldMoves, MSGBOX_NPC
	end

Route2_House_EventScript_Reyley::
	lock
	faceplayer
	setvar VAR_0x8008, INGAME_TRADE_MR_MIME
	call EventScript_GetInGameTradeSpeciesInfo
	goto_if_set FLAG_DID_MIMIEN_TRADE, Route2_House_EventScript_AlreadyTraded
	msgbox Trade_Text_LookingForMonWannaTradeForMon, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, NO, Route2_House_EventScript_DeclineTrade
	call EventScript_ChooseMonForInGameTrade
	goto_if_ge VAR_0x8004, PARTY_SIZE, Route2_House_EventScript_DeclineTrade
	call EventScript_GetInGameTradeSpecies
	goto_if_ne VAR_RESULT, VAR_0x8009, Route2_House_EventScript_NotRequestedMon
	call EventScript_DoInGameTrade
	msgbox Trade_Text_HeyThanks
	setflag FLAG_DID_MIMIEN_TRADE
	release
	end

Route2_House_EventScript_DeclineTrade::
	msgbox Trade_Text_AwwOhWell
	release
	end

Route2_House_EventScript_NotRequestedMon::
	bufferspeciesname STR_VAR_1, VAR_0x8009
	msgbox Trade_Text_WhatThatsNoMon
	release
	end

Route2_House_EventScript_AlreadyTraded::
	msgbox Trade_Text_IsntMyOldMonGreat
	release
	end

