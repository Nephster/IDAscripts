import idaapi

#set address ea=0x0049F000
#set end of address end=0x49F2B4
for i in xrange(0, (end-ea)/4):
	create_dword(ea+i*4)   
