ea = ScreenEA()             
max_bits = 8

ror = lambda val, r_bits, max_bits: \
    ((val & (2**max_bits-1)) >> r_bits%max_bits) | \
    (val << (max_bits-(r_bits%max_bits)) & (2**max_bits-1))
    
rol = lambda val, r_bits, max_bits: \
    (val << r_bits%max_bits) & (2**max_bits-1) | \
    ((val & (2**max_bits-1)) >> (max_bits-(r_bits%max_bits)))


for i in range(0,100):               
    #print "%d" % i
	
    b = Byte(ea+i)               
    b=rol(b,6,max_bits)
    decoded_byte = b ^ 0x1D    
    PatchByte(ea+i, decoded_byte)  
print "Finish Script"