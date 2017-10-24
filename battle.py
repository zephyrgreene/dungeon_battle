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
  hunger = 3
  
  def __init__(self, name, health, endurance, mana, sanity, hunger):
    self.name = name
    self.health = health
    self.endurance = endurance
    self.mana = mana
    self.sanity = sanity
    self.hunger = hunger
    
  def display_stats(self):
    print("Name:", self.name, "\nHealth:", self.health, "\nEndurance:", self.endurance, "\nMana:", self.mana, "\nSanity:", self.sanity, "\nHunger", self.hunger, "\n")
    
  def display_actions(self):
    print("Action One:", self.action1)
    
player = Entity("Not Steve",100,50,100,1,100)
player.display_stats()

bog_monster = Entity("Bog Monster",250,50,50,100,100)
bog_monster.display_stats()
  