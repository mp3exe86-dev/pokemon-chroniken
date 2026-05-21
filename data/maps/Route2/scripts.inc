Route2_MapScripts::
	.byte 0

Route2_EventScript_RouteSign::
	msgbox Route2_Text_RouteSign, MSGBOX_SIGN
	end

Route2_EventScript_DiglettsCaveSign::
	msgbox Route2_Text_DiglettsCave, MSGBOX_SIGN
	end

Route2_EventScript_LugiaSign::
	msgbox Route2_Text_LugiaSign, MSGBOX_SIGN
	setflag FLAG_LUGIA_AWAKENED
	end

Route2_Text_LugiaSign:
	.string "The cold water\nremembers everything.\pListen carefully.$"
