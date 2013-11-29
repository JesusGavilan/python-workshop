#class horse

class Horse(object):
	"""Horse represents a Horse :_"""
	species = "Equus ferus caballus"
	
	def __init__(self,color,weight,wild=False):
		self.color  = color
		self.weight = weight
		self.wild   = wild
	
	def __repr__(self):
		return "%s horse weighing %f and wild status is %b" (self.color,self,weight,self.wild)
	
	def make_sound(self):
		print("neighhhh")
	
	def movement(self):
		return "walk"

class RaceHorse(Horse):
	""" A faster horse that inherits from Horse"""
	def movement(self):
		return "run"
	def movement_slow(self):
		super(Horse,self).make_sound()
	def __repr__(self):
		return "%s race horse weighing %f and wilds status is %b" (self.color, self.weight, self.wild)

horse3 = RaceHorse("white",200)
print horse3.movement_slow()
print horse3.movement() 
