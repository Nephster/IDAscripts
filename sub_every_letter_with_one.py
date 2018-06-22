ea = ScreenEA()             

for i in range(0,100):               
    #print "%d" % i
	
    b = Byte(ea+i)               
    decoded_byte = b - 1    
    PatchByte(ea+i, decoded_byte)  
	#print "%s" % decoded_byte
	
print "Finish Script"