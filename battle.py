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
  # attributes = {hp: 0, mp: 1, stam: 2, thirst: 3, psych: 4}
  
  def __init__(self, name):
    self.name = name
  
  # def displayStats(self):
  #   print("Name:", self.name, "\nHealth:", self.hp, "\nEndurance:", self.stam, "\nMana:", self.mp, "\nSanity:", self.psych, "\nHunger", self.thirst, "\n")

player = Entity("Not Steve")
# player.displayStats()

bogMonster = Entity("Bog Monster")
# bogMonster.displayStats()
