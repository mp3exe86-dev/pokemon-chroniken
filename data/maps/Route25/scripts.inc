Route25_MapScripts::
	map_script MAP_SCRIPT_ON_RESUME, Route25_OnResume
	.byte 0

Route25_OnResume::
	call_if_set FLAG_SYS_SPECIAL_WILD_BATTLE, Route25_EventScript_SuicuneOnResume
	end

Route25_EventScript_SuicuneOnResume::
	clearflag FLAG_SYS_SPECIAL_WILD_BATTLE
	setflag FLAG_SUICUNE_ENCOUNTERED
	return

Route25_EventScript_Suicune::
	goto_if_set FLAG_SUICUNE_ENCOUNTERED, Route25_EventScript_SuicuneGone
	lockall
	message Route25_Text_SuicuneApproach
	waitmessage
	waitbuttonpress
	closemessage
	applymovement LOCALID_ROUTE25_SUICUNE, Route25_Movement_SuicuneApproach
	waitmovement 0
	waitse
	playmoncry SPECIES_SUICUNE, CRY_MODE_ENCOUNTER
	waitmoncry
	delay 20
	setwildbattle SPECIES_SUICUNE, 50
	setflag FLAG_SYS_SPECIAL_WILD_BATTLE
	special StartLegendaryBattle
	waitstate
	clearflag FLAG_SYS_SPECIAL_WILD_BATTLE
	setflag FLAG_SUICUNE_ENCOUNTERED
	releaseall
	end

Route25_EventScript_SuicuneGone::
	msgbox Route25_Text_SuicuneGone, MSGBOX_SIGN
	end

Route25_Movement_SuicuneApproach::
	walk_left
	walk_left
	step_end

Route25_Text_SuicuneApproach:
	.string "The water is perfectly still.\pSomething is watching\nfrom the other side.\p...$"

Route25_Text_SuicuneGone:
	.string "The water is still.\pNothing remains.$"

Route25_EventScript_SeaCottageSign::
	msgbox Route25_Text_SeaCottageSign, MSGBOX_SIGN
	end

Route25_EventScript_Man::
	msgbox Route25_Text_AreYouHereAlone, MSGBOX_NPC
	end
