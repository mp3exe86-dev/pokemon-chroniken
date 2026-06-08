VermilionCity_ArchivarHouse_MapScripts::
	.byte 0


VermilionCity_ArchivarHouse_EventScript_Archivar::
	lock
	faceplayer
	msgbox VermilionCity_ArchivarHouse_Text_Challenge, MSGBOX_YESNO
	goto_if_eq VAR_RESULT, YES, VermilionCity_ArchivarHouse_EventScript_ArchivarBattle
	goto_if_set FLAG_ARCHIVAR_MORLOND_ITEM_GIVEN, VermilionCity_ArchivarHouse_EventScript_ArchivarEnd
	msgbox VermilionCity_ArchivarHouse_Text_NoChoice, MSGBOX_DEFAULT
	checkitemspace ITEM_BLUE_SHARD
	goto_if_eq VAR_RESULT, FALSE, VermilionCity_ArchivarHouse_EventScript_ArchivarBagFull
	giveitem_msg VermilionCity_ArchivarHouse_Text_ObtainedBlueShard, ITEM_BLUE_SHARD
	setflag FLAG_ARCHIVAR_MORLOND_ITEM_GIVEN
	release
	end

VermilionCity_ArchivarHouse_EventScript_ArchivarBattle::
	trainerbattle_no_intro TRAINER_ARCHIVAR_MORLOND, VermilionCity_ArchivarHouse_Text_Lose
	removeobject LOCALID_ARCHIVAR_MORLOND
	setflag FLAG_ARCHIVAR_MORLOND_DEFEATED
	msgbox VermilionCity_ArchivarHouse_Text_Victory, MSGBOX_DEFAULT
	release
	end

VermilionCity_ArchivarHouse_EventScript_ArchivarEnd::
	release
	end

VermilionCity_ArchivarHouse_EventScript_ArchivarBagFull::
	msgbox VermilionCity_ArchivarHouse_Text_BagFull, MSGBOX_DEFAULT
	release
	end

VermilionCity_ArchivarHouse_Text_Challenge::
	.string "The harbor brought\nyou here.\pI keep records\nof what crosses\nthe water.\pAeralith has been\nseen above Morlond.\pThree times this\nmonth.\nAlways at dawn.\pDo you seek\nthe record or\nthe crossing?$"

VermilionCity_ArchivarHouse_Text_NoChoice::
	.string "The sea remembers\neverything.\pTake this.\pIt came from\nbelow the surface.\pVery deep below.$"

VermilionCity_ArchivarHouse_Text_ObtainedBlueShard::
	.string "You received a\nBLUE SHARD!$"

VermilionCity_ArchivarHouse_Text_Lose::
	.string "The water is\nnot ready for you.\pCome back.$"

VermilionCity_ArchivarHouse_Text_Victory::
	.string "You crossed it.\nThe record is yours.$"

VermilionCity_ArchivarHouse_Text_BagFull::
	.string "Your bag is full.\nReturn when you\lhave made room.$"
