#set address to start ea=0x0049F000
#set address to end end=0x49F2B4
for i in xrange(0, (end-ea)/4):
    set_name(ea+i*4, get_name(Dword(ea+i*4))+"_")