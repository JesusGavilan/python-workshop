edad = input("Cual es la edad de un perro?: ")
if   edad<0:
	print "Esto no puede ser verdad"
elif edad ==1:
	print "Alrededor de 14 anys humanos"
elif edad ==2:
	print "Alrededor de 22 anys humanos"
elif edad > 2:
	human = 22 + (edad - 2)*5
	print "Anys humanos: ", human

raw_input('press Return>')
