class entity:
  name = ""
  
  action1 = ""
  action2 = ""
  action3 = ""
  action4 = ""
  action5 = ""
  
  health = 0
  endurance = 0
  mana = 0
  sanity = 0
  hunger = 0
  
  def __init__(self, health, endurance, mana, sanity, hunger):
    self.health = health
    self.endurance = endurance
    self.mana = mana
    self.sanity = sanity
    self.hunger = hunger
  