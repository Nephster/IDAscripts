import numpy
ea = ScreenEA()             

for i in range(0,24401):               
	b = Byte(ea+i)               
	tmp = b ^ 52
	decode=tmp ^ 255
	decode= decode ^ 176
	PatchByte(ea+i, decode)  
	
print "Finish Script"