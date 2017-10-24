class Entity:
  name = ""
  
  actions = []
  
  # Max stats
  maxHp = 100
  maxStam = 100
  maxMp = 100
  maxPsych = 100
  maxThirst = 100
  
  # Current stats
  hp = maxHp
  stam = maxStam
  mp = maxMp
  psych = maxPsych
  thirst = maxThirst
  
  def __init__(self, name):
    self.name = name
  
  def addHp(self, addHp):
    if(self.hp + addHp <= self.maxHp):
      self.hp += addHp
  
  def setMaxHp(self, newMax):
    self.maxHp = newMax
    self.hp = self.maxHp
    
  def addMp(self, addMp):
    if(self.mp + addMp <= self.maxMp):
      self.mp += addMp
  
  def setMaxMp(self, newMax):
    self.maxMp = newMax
    self.mp = self.maxMp
    
  def addStam(self, addStam):
    if(self.stam + addStam <= self.maxStam):
      self.stam += addStam
  
  def setMaxStam(self, newMax):
    self.stam = newMax
    self.stam = self.maxStam
  
  def displayStats(self):
    print("Name:", self.name, "\nHealth:", self.hp, "\nEndurance:", self.stam, "\nMana:", self.mp, "\nSanity:", self.psych, "\nHunger", self.thirst, "\n")

player = Entity("Not Steve")
player.displayStats()

bogMonster = Entity("Bog Monster")
bogMonster.setMaxHp(250)
bogMonster.displayStats()
  