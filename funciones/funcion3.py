def suma(a,b):
	return a+b

def resta(a,b):
	return a-b

def multi(a,b):
	return a*b

def power(a,b):
	return a**b

def operacion(op,a,b):
	print "El tipo de funcion a aplicar " + str(op)
	if op=="suma":
		print "El resultado de la " + op + " es: %d" % suma(a,b)
	elif op=="resta":
		print "El resultado de la " + op + " es: %d" % resta(a,b)
	elif op=="multi":
		print "El resultado de la " + op + " es: %d" % multi(a,b)
	elif op=="power":
		print "El resultado de la " + op + " es: %d" % power(a,b)
	
tipo = raw_input("Operacion a realizar: ")
a = input("Primer valor: ")
b = input("Segundo valor: ")
operacion(tipo,a,b)	
