#Reading a file
fobj = open("lorem.txt", "r")
#Printing the content
for line in fobj:
	print line.rstrip()
fobj.close()
