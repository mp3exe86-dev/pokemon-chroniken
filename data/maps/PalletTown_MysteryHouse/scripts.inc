PalletTown_MysteryHouse_MapScripts::
	.byte 0

PalletTown_MysteryHouse_EventScript_OldWoman::
	goto_if_set FLAG_MYSTERY_HOUSE_WOMAN_DONE, PalletTown_MysteryHouse_EventScript_OldWoman_After
	lock
	faceplayer
	msgbox PalletTown_MysteryHouse_Text_OldWoman1, MSGBOX_DEFAULT
	msgbox PalletTown_MysteryHouse_Text_OldWoman2, MSGBOX_DEFAULT
	msgbox PalletTown_MysteryHouse_Text_OldWoman3, MSGBOX_DEFAULT
	msgbox PalletTown_MysteryHouse_Text_OldWoman4, MSGBOX_DEFAULT
	msgbox PalletTown_MysteryHouse_Text_OldWoman5, MSGBOX_DEFAULT
	msgbox PalletTown_MysteryHouse_Text_OldWoman6, MSGBOX_DEFAULT
	giveitem ITEM_OLD_AMBER
	setflag FLAG_MYSTERY_HOUSE_WOMAN_DONE
	release
	end

PalletTown_MysteryHouse_EventScript_OldWoman_After::
	lock
	faceplayer
	msgbox PalletTown_MysteryHouse_Text_OldWoman_After, MSGBOX_NPC
	release
	end

PalletTown_MysteryHouse_Text_OldWoman1::
	.string "I knew you'd come.\p"
	.string "I've been waiting\n"
	.string "since before you\p"
	.string "were born.$"

PalletTown_MysteryHouse_Text_OldWoman2::
	.string "...The stones remember\n"
	.string "everything.\p"
	.string "They were here\n"
	.string "before the POKéMON.\p"
	.string "Before the people.$"

PalletTown_MysteryHouse_Text_OldWoman3::
	.string "Something woke up\n"
	.string "three years ago.\p"
	.string "Not a POKéMON.\n"
	.string "Not a person.\p"
	.string "Something older.$"

PalletTown_MysteryHouse_Text_OldWoman4::
	.string "It doesn't have\n"
	.string "a name yet.\p"
	.string "Names come later.\n"
	.string "After the knowing.$"

PalletTown_MysteryHouse_Text_OldWoman5::
	.string "You carry something\n"
	.string "with you.\p"
	.string "You don't know\n"
	.string "what it is yet.$"

PalletTown_MysteryHouse_Text_OldWoman6::
	.string "Take this.\p"
	.string "It belonged to\n"
	.string "someone who also\p"
	.string "didn't know.\p"
	.string "They found out.\p"
	.string "I hope you\n"
	.string "do too.$"

PalletTown_MysteryHouse_Text_OldWoman_After::
	.string "You already know\n"
	.string "more than you think.\p"
	.string "The rest will\n"
	.string "come on its own.$"
