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
    
  def showName(self):
    print("Name:", self.name)
    
  def showHp(self):
    print("Health:", self.stats['hp'].get(), "/", self.stats['hp'].getMax())

  def showMp(self):
    print("Mana:", self.stats['mp'].get(), "/", self.stats['mp'].getMax())

  def showStam(self):
    print("Stamina:", self.stats['stam'].get(), "/", self.stats['stam'].getMax())
    
  def showThirst(self):
    print("Thirst:", self.stats['thirst'].get(), "/", self.stats['thirst'].getMax())
    
  def showPsych(self):
    print("Pysch:", self.stats['psych'].get(), "/", self.stats['psych'].getMax())

  def showStats(self):
    self.showName()
    self.showHp()
    self.showMp()
    self.showStam()
    self.showThirst()
    self.showPsych()

player = Entity("Not Steve", 101, 40, 50, 60, 70)
player.showStats()
print("")
bogMonster = Entity("Bog Monster", 250, 40, 50, 60, 70)
bogMonster.showStats()
