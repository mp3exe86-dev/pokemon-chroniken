.include "data/maps/Nebelsteg/text.inc"

Nebelsteg_MapScripts::
	.byte 0

Nebelsteg_EventScript_Fischer::
    msgbox Nebelsteg_Text_Fischer, MSGBOX_NPC
    end

Nebelsteg_EventScript_Kind::
    msgbox Nebelsteg_Text_Kind, MSGBOX_NPC
    end
