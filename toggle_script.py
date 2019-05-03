def msg(msg):
    RPR_ShowConsoleMsg(msg)
    return

state = str(RPR_GetProjExtState(0, "DummyToggleAction", "toggle_state", "", 123123)[4])
msg("what in the hell is the toggle state: \n")
msg(str(state) + "\n")

def toggleFunc():
    # test infinate loop
    cmd = RPR_NamedCommandLookup("_RScd217e59dc8a590480810d4acb0d6eda4810a706")
    # test script
    # cmd = RPR_NamedCommandLookup("_RS16ed897990f130f368a1db0c17c067801b1517a5")
    RPR_Main_OnCommand(cmd, 0)

if state == "0":
    RPR_SetProjExtState(0, "DummyToggleAction", "toggle_state", "1")
    RPR_defer("toggleFunc()")
else:
    RPR_SetProjExtState(0, "DummyToggleAction", "toggle_state", "0")
