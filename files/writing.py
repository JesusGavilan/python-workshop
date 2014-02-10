fobj_in = open("lorem.txt")
fobj_out = open("lorem2.txt","w")
i=1
for line in fobj_in:
	print line.rstrip()
	fobj_out.write(str(i) + ": "+line)
	i = i + 1
fobj_in.close()
fobj_out.close() 
