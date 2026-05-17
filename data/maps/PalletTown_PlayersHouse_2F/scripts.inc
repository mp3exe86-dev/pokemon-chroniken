PalletTown_PlayersHouse_2F_MapScripts::
	map_script MAP_SCRIPT_ON_TRANSITION, PalletTown_PlayersHouse_2F_OnTransition
	map_script MAP_SCRIPT_ON_WARP_INTO_MAP_TABLE, PalletTown_PlayersHouse_2F_OnWarp
	.byte 0

PalletTown_PlayersHouse_2F_OnTransition::
	call_if_eq VAR_MAP_SCENE_PALLET_TOWN_PLAYERS_HOUSE_2F, 0, PalletTown_PlayersHouse_2F_EventScript_SetRespawn
	end

PalletTown_PlayersHouse_2F_EventScript_SetRespawn::
	setrespawn HEAL_LOCATION_PALLET_TOWN
	return

PalletTown_PlayersHouse_2F_OnWarp::
	map_script_2 VAR_MAP_SCENE_PALLET_TOWN_PLAYERS_HOUSE_2F, 0, PalletTown_PlayersHouse_2F_FirstWarpIn
	.2byte 0

PalletTown_PlayersHouse_2F_FirstWarpIn::
	turnobject LOCALID_PLAYER, DIR_NORTH
	setvar VAR_MAP_SCENE_PALLET_TOWN_PLAYERS_HOUSE_2F, 1
	end

PalletTown_PlayersHouse_2F_EventScript_NES::
	msgbox PalletTown_PlayersHouse_2F_Text_PlayedWithNES, MSGBOX_SIGN
	end

PalletTown_PlayersHouse_2F_EventScript_Sign::
	msgbox PalletTown_PlayersHouse_2F_Text_PressLRForHelp, MSGBOX_SIGN
	end

PalletTown_PlayersHouse_2F_EventScript_PC::
	goto_if_questlog EventScript_ReleaseEnd
	lockall
	setvar VAR_0x8004, HELPCONTEXT_BEDROOM_PC
	special Script_SetHelpContext
	setvar VAR_0x8004, 1
	special AnimatePcTurnOn
	playse SE_PC_ON
	msgbox Text_PlayerBootedUpPC
	special BedroomPC
	waitstate
	special SetHelpContextForMap
	releaseall
	end

EventScript_PalletTown_PlayersHouse_2F_ShutDownPC::
	setvar VAR_0x8004, 1
	playse SE_PC_OFF
	special AnimatePcTurnOff
	special SetHelpContextForMap
	releaseall
	end
PalletTown_PlayersHouse_2F_EventScript_BurntFeather::
        lock
        goto_if_set FLAG_STARTER_CHOSEN, PalletTown_PlayersHouse_2F_EventScript_AlreadyChosen
        msgbox PalletTown_PlayersHouse_2F_Text_BurntFeather, MSGBOX_YESNO
        goto_if_eq VAR_RESULT, YES, PalletTown_PlayersHouse_2F_EventScript_ChooseHoundour
        release
        end

PalletTown_PlayersHouse_2F_EventScript_BlackStone::
        lock
        goto_if_set FLAG_STARTER_CHOSEN, PalletTown_PlayersHouse_2F_EventScript_AlreadyChosen
        msgbox PalletTown_PlayersHouse_2F_Text_BlackStone, MSGBOX_YESNO
        goto_if_eq VAR_RESULT, YES, PalletTown_PlayersHouse_2F_EventScript_ChooseSneasel
        release
        end

PalletTown_PlayersHouse_2F_EventScript_EmptyMirror::
        lock
        goto_if_set FLAG_STARTER_CHOSEN, PalletTown_PlayersHouse_2F_EventScript_AlreadyChosen
        msgbox PalletTown_PlayersHouse_2F_Text_EmptyMirror, MSGBOX_YESNO
        goto_if_eq VAR_RESULT, YES, PalletTown_PlayersHouse_2F_EventScript_ChooseMisdreavus
        release
        end

PalletTown_PlayersHouse_2F_EventScript_ChooseHoundour::
        setflag FLAG_STARTER_CHOSEN
        setflag FLAG_SYS_POKEMON_GET
        setflag FLAG_SYS_POKEDEX_GET
        special EnableNationalPokedex
        setflag FLAG_PALLET_LADY_NOT_BLOCKING_SIGN
        setvar VAR_MAP_SCENE_VIRIDIAN_CITY_MART, 2
        setvar VAR_MAP_SCENE_VIRIDIAN_CITY_OLD_MAN, 2
        setvar VAR_MAP_SCENE_PALLET_TOWN_RIVALS_HOUSE, 1
        setvar VAR_MAP_SCENE_ROUTE22, 1
        setvar VAR_MAP_SCENE_POKEMON_CENTER_TEALA, 1
        setvar VAR_MAP_SCENE_PALLET_TOWN_PROFESSOR_OAKS_LAB, 3
        givemon SPECIES_HOUNDOUR, 5, ITEM_NONE
        playfanfare MUS_OBTAIN_ITEM
        msgbox PalletTown_PlayersHouse_2F_Text_StarterAppears, MSGBOX_DEFAULT
        waitfanfare
        release
        end

PalletTown_PlayersHouse_2F_EventScript_ChooseSneasel::
        setflag FLAG_STARTER_CHOSEN
        setflag FLAG_SYS_POKEMON_GET
        setflag FLAG_SYS_POKEDEX_GET
        special EnableNationalPokedex
        setflag FLAG_PALLET_LADY_NOT_BLOCKING_SIGN
        setvar VAR_MAP_SCENE_VIRIDIAN_CITY_MART, 2
        setvar VAR_MAP_SCENE_VIRIDIAN_CITY_OLD_MAN, 2
        setvar VAR_MAP_SCENE_PALLET_TOWN_RIVALS_HOUSE, 1
        setvar VAR_MAP_SCENE_ROUTE22, 1
        setvar VAR_MAP_SCENE_POKEMON_CENTER_TEALA, 1
        setvar VAR_MAP_SCENE_PALLET_TOWN_PROFESSOR_OAKS_LAB, 3
        givemon SPECIES_SNEASEL, 5, ITEM_NONE
        playfanfare MUS_OBTAIN_ITEM
        msgbox PalletTown_PlayersHouse_2F_Text_StarterAppears, MSGBOX_DEFAULT
        waitfanfare
        release
        end

PalletTown_PlayersHouse_2F_EventScript_ChooseMisdreavus::
        setflag FLAG_STARTER_CHOSEN
        setflag FLAG_SYS_POKEMON_GET
        setflag FLAG_SYS_POKEDEX_GET
        special EnableNationalPokedex
        setflag FLAG_PALLET_LADY_NOT_BLOCKING_SIGN
        setvar VAR_MAP_SCENE_VIRIDIAN_CITY_MART, 2
        setvar VAR_MAP_SCENE_VIRIDIAN_CITY_OLD_MAN, 2
        setvar VAR_MAP_SCENE_PALLET_TOWN_RIVALS_HOUSE, 1
        setvar VAR_MAP_SCENE_ROUTE22, 1
        setvar VAR_MAP_SCENE_POKEMON_CENTER_TEALA, 1
        setvar VAR_MAP_SCENE_PALLET_TOWN_PROFESSOR_OAKS_LAB, 3
        givemon SPECIES_MISDREAVUS, 5, ITEM_NONE
        playfanfare MUS_OBTAIN_ITEM
        msgbox PalletTown_PlayersHouse_2F_Text_StarterAppears, MSGBOX_DEFAULT
        waitfanfare
        release
        end

PalletTown_PlayersHouse_2F_EventScript_AlreadyChosen::
        msgbox PalletTown_PlayersHouse_2F_Text_AlreadyChosen, MSGBOX_DEFAULT
        release
        end
