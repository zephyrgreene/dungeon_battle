class Attribute:
  max = 1
  now = max
  
  def __init__(self, setMax):
    self.setMax(setMax)

  def setMax(self, newMax):
    self.max = newMax
    self.now = self.max

  def add(self, delta):
    self.now += delta
    
  def get(self):
    return self.now
    
  def getMax(self):
    return self.max

class Entity:
  name = ""
  
  actions = []
  
  # Using a class for attributes
  stats = {}
  
  def __init__(self, name, hp, mp, stam, thirst, pysch):
    self.name = name
    self.stats = {'hp': Attribute(hp), 'mp': Attribute(mp), 'stam': Attribute(stam), 'thirst': Attribute(thirst), 'psych': Attribute(pysch)}
  
  # def displayStats(self):
  #   print("Name:", self.name, "\nHealth:", self.hp, "\nEndurance:", self.stam, "\nMana:", self.mp, "\nSanity:", self.psych, "\nHunger", self.thirst, "\n")

player = Entity("Not Steve", 101, 40, 50, 60, 70)
# player.displayStats()

bogMonster = Entity("Bog Monster", 101, 40, 50, 60, 70)
# bogMonster.displayStats()
