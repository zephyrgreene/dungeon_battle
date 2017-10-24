class Attribute:
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
    print(f"Name: {self.name}")
    
  def showHp(self):
    print(f"Health: {self.stats['hp'].get()}/{self.stats['hp'].getMax()}")

  def showMp(self):
    print(f"Mana: {self.stats['mp'].get()}/{self.stats['mp'].getMax()}")

  def showStam(self):
    print(f"Stamina: {self.stats['stam'].get()}/{self.stats['stam'].getMax()}")
    
  def showThirst(self):
    print(f"Thirst: {self.stats['thirst'].get()}/{self.stats['thirst'].getMax()}")
    
  def showPsych(self):
    print(f"Pysch: {self.stats['psych'].get()}/{self.stats['psych'].getMax()}")

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
