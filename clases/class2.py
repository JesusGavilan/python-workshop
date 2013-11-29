#Ejemplo 1
class VMname:
	def createVM(self, name):
		self.name = name
	def stateVM(self):
		print('Printing from the 1st Class example ' + self.name)
		print " "

#Inicializando la clase
example1 = VMname()
example1.createVM('jesus.i2cat.net')
example1.stateVM()

#Ejemplo 2
class VMname1:
	def __init__(self, name):
		self.name = name
	def stateVM1(self):
		print('Printing from the 2nd class example ' + self.name)
		print " "

#Inicializando la clase
example2 = VMname1('pepe.i2cat.net')
example2.stateVM1()

#Example 3
class VMname2:
	def __init__(self, name='vicent.i2cat.net'):
		self.name = name
	def stateVM2(self):
		print('Printing from the 3rd class example ' + self.name)
#Init initilizes the class
example3 = VMname2()
example3.stateVM2()

