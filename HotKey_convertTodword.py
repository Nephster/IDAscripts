import idaapi

def foo():
 print "Hotkey activated!"
 ea=ScreenEA()
 create_dword(ea)   
# IDA binds hotkeys to IDC functions so a trampoline IDC function
# must be created
idaapi.CompileLine('static key_2() { RunPythonStatement("foo()"); }')
# Add the hotkey
AddHotkey("2", 'key_2')
