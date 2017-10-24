class Attribute:
  max = 1
  now = max
  
  def __init__(self, setMax, add):
    self.max = setMax
    self.now += add

class Entity:
  name = ""
  
  actions = []
  
  # Using a class for attributes
  # attributes = {hp: 0, mp: 1, stam: 2, thirst: 3, psych: 4}
  
  # # Max stats
  # maxHp = 100
  # maxStam = 100
  # maxMp = 100
  # maxPsych = 100
  # maxThirst = 100
  
  # # Current stats
  # hp = maxHp
  # stam = maxStam
  # mp = maxMp
  # psych = maxPsych
  # thirst = maxThirst
  
  def __init__(self, name):
    self.name = name
  
  def addHp(self, addHp):
    if(self.hp + addHp <= self.maxHp):
      self.hp += addHp
  
  def setMaxHp(self, newMax):
    self.maxHp = newMax
    self.hp = self.maxHp
  
  def displayStats(self):
    print("Name:", self.name, "\nHealth:", self.hp, "\nEndurance:", self.stam, "\nMana:", self.mp, "\nSanity:", self.psych, "\nHunger", self.thirst, "\n")

player = Entity("Not Steve")
player.displayStats()

bogMonster = Entity("Bog Monster")
bogMonster.setMaxHp(250)
bogMonster.displayStats()
