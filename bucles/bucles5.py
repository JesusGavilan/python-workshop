n=100
count = 0
i = 0
suma = 0
while count<=100:
	if i%2==0:
		suma = suma + i
		count = count + 1
		print str(count)
	i = i + 1

print "Suma de los primeros 100 numeros pares %d " %(suma)
  
