class Horse(object):
    """Horse represents a Horse"""
    species = "Equus ferus caballus"
    def __init__(self,color,weight,wild=False):
        self.color = color
        self.weight = weight
        self.wild = wild
    def __repr__(self):
        return "%s horse weighing %f and wild status is %b" (self.color,self.weight,self.wild)
    
    def make_sound(self):
        print("neighhhh")
    
    def movement(self):
        print "walk"

class RaceHorse(Horse):
    """A faster horse that inherits from Horse"""
    def movement(self):
        return "run"
    def movement_slow(self):
        super(RaceHorse,self).movement()
    def __repr__(self):
        return "%s race horse weighing %f and wild status is %b" (self.color,self.weight,self.wild)

horse3 = RaceHorse("white",200)
horse3.movement_slow()

print horse3.movement()
