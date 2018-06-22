import idaapi

def decrypt_string(data):
	#here have to set init vector init_vector = []
	list=init_vector;
	str=data
	dec_str=""
	#list_str=list(str)
	for j in xrange(len(str)):
		if ord(str[j]) == 92:
			dec_str+='\\'
		if ord(str[j]) == 37: 
			dec_str+='%'
		if ord(str[j]) == 91:
			dec_str+='['
		if ord(str[j]) == 93:
			dec_str+=']'
		if ord(str[j]) == 43:
			dec_str+='+'
		if ord(str[j]) == 46:
			dec_str+='.'
		if ord(str[j]) == 42:
			dec_str+='*'
		if ord(str[j]) == 20:
			dec_str+=' '
		if ord(str[j]) == 60:
			dec_str+='<'
		if ord(str[j]) == 62:
			dec_str+='>'
		if ord(str[j]) == 61:
			dec_str+='='
		if ord(str[j]) == 58:
			dec_str+=':'
		if ord(str[j]) == 32:
			dec_str+=' '
		if ord(str[j]) == 47:
			dec_str+='/'
		for i in list:
			if ord(str[j]) == i:
				dec_str+=chr(init_vector[((list.index(i)+6) % 64)])
	return dec_str

def func_key():
    print "Hotkey activated!"
    ea=ScreenEA()
    dec_s=decrypt_string(idc.GetManyBytes(ea, ItemSize(ea)))
    MakeComm(ea,dec_s)
	#for i in xrange(len(dec_s)):    
        #PatchByte(ea+i,ord(dec_s[i]))
        #print "%s" % hex(dec_s[i])
        #print decrypt_string(idc.GetManyBytes(ea, ItemSize(ea)))
            
  # IDA binds hotkeys to IDC functions so a trampoline IDC function
# must be created
idaapi.CompileLine('static key_2() { RunPythonStatement("func_key()"); }')
# Add the hotkey
idc.AddHotkey("2", 'key_2')
