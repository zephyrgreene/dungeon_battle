class Entity:
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
  
  def _init(self, health, endurance, mana, sanity, hunger):
    self.health = health
    self.endurance = endurance
    self.mana = mana
    self.sanity = sanity
    self.hunger = hunger
    
  def display_stats(self):
    print("Health:", self.health, "\nEndurance:", self.endurance)
    
  def display_actions(self):
    print("Action One:", self.action1)
    
def make_entity(health, endurance, mana, sanity, hunger):
  entity = Entity(health, endurance, mana, sanity, hunger)
  return entity
  