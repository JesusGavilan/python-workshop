class Horse():
	species = "Equus ferus caballus"
	
	def __init__(self,color,weight,wild=False):
		self.color = color
		self.wetight = weight
		self.wild = wild
	
	def __repr__(self):
		return "%s horse weighing %f and wild status is %b" (self.color, self.weight, self.wild)

	def make_sound(self):
		print "neighhhh"
	
	def movement(self):
		return "walk"

blanc = Horse("white", 200)

blanc.make_sound()
print blanc.movement()
		
