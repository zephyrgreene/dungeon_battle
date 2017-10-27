class Pool:
  base = 50

  def __init__(self, val = 1):
    if (val > 0):
      self.setMax(val)
    else:
      self.valError()
 
  def valError(self):
    raise ValueError("Pool.max cannot be less than 1.")
     
  def setMax(self, val):
    self.max = val + Pool.base
    self.val = self.max

  def addMax(self, delta):
    self.max += delta
    self.add(delta)
  
  def add(self, delta):
    if (self.val + delta <= self.max):
      self.val += delta
    else:
      self.val = self.max

class Attribute:
  def __init__(self, val = 1, multiplier = 1):
    self.setVal(val)

  def valError(self):
    raise ValueError("Attributes.val cannot be less than 1.")

  def setVal(self, val):
    if (val > 0):
      self.val = val
    else:
      self.valError()
      
  def add(self, delta):
    if (self.val + delta > 0):
      self.val += delta
    else:
      self.valError()

class Entity:
  def __init__(self, name, strength = 1, psych = 1, vitality = 1, sustenance = 1, intelligence = 1):
    self.isAlive = True
    self.name = name
    
    self.strength = Attribute(strength)
    self.psych = Attribute(psych)
    self.vitality = Attribute(vitality)
    self.intelligence = Attribute(intelligence)
    self.sustenance = Attribute(sustenance)
    
    self.health = Pool(self.vitality.val * 10)
    self.stamina = Pool(self.strength.val * 11)
    self.sanity = Pool(self.psych.val * 8)
    self.mana = Pool(self.intelligence.val * 9)
    self.hunger = Pool(self.sustenance.val * 7)
    
  def aliveCheck(self):
    if (self.health.val <= 0 or self.stamina.val <= 0 or self.sanity.val <= 0 or self.mana.val <= 0 or self.hunger.val <= 0):
      print(f"{self.name} is dead")
      self.isAlive = False
    else:
      self.isAlive = True
      
  def showStats(self):
    print({
      'strength':self.strength.val,
      'psych':self.psych.val,
      'vitality':self.vitality.val,
      'intelligence' :self.intelligence.val,
      'sustenance' :self.sustenance.val,
      
      'health':self.health.val,
      'stamina':self.stamina.val,
      'sanity':self.sanity.val,
      'mana' :self.mana.val,
      'hunger' :self.hunger.val
    })

class Question:
  def __init__(self, text, options, outcomes):
    self.text = text
    self.options = options
    self.outcomes = outcomes

def playerPrompt():
  name = input("What is your name?")
  answerKey = ['a','b','c','d','e']
  
  color = Question("What is your favorite color?", 
    {"a":"Purple",
    "b":"Blue",
    "c":"Yellow",
    "d":"Red",
    "e":"Brown"},
    
    {"a":lambda: player.psych.add(10),
    "b":lambda: player.intelligence.add(10),
    "c":lambda: player.strength.add(10),
    "d":lambda: player.vitality.add(10),
    "e":lambda: player.sustenance.add(10)})
    
  action = Question("What would you rather be?", 
    {"a":"Acrobat",
    "b":"Dancer",
    "c":"Singer",
    "d":"Talker",
    "e":"Weight lifter"},
    
    {"a":"player.action.append('acrobat')",
    "b":"player.action.append('dancer')",
    "c":"player.action.append('sing')",
    "d":"player.action.append('talk')",
    "e":"player.action.append('strong')"})
  
  ans = ''
  while (ans not in answerKey):
    ans = input(f"{color.text}\nA) {color.options['a']}\nB) {color.options['b']}\nC) {color.options['c']}\nD) {color.options['d']}\nE) {color.options['e']}\n").lower()
  colorAns = ans
  
  ans = ''
  while(ans not in answerKey):
    ans = input(f"{action.text}\nA) {action.options['a']}\nB) {action.options['b']}\nC) {action.options['c']}\nD) {action.options['d']}\nE) {action.options['e']}\n").lower()

  actionAns = ans
  player = Entity(name)
  color.outcomes[colorAns]()
  return player

def gameLoop():
  player = playerPrompt()
  monster = Entity("Eldritch Horror", vitality = 15, sustenance = 8)
  print(f"{player.name}, you are in a winding and dangerous dungeon.","\nYou are unaware how you got here, but you must journey forward to escape.")
  
  while(True):
    ans = input(f"Will you journey forward?\nA) Yes\nB) No\n").lower()
    if (ans == 'a' or ans == 'b'):
      break
  
  if (ans == 'a'):
    print(f"You have encountered a {monster.name}.")
    while(player.isAlive and monster.isAlive):
      ans = input("What action will you take?\nA) Fight\nB) Pick it up\nC) Dance").lower()
      if (ans == 'a'):
        print(f"You attack the monster with your sword dealing 73 damage.",
        "\nIt lashes back with its tentacles, dealing 25 damage.\n")
        
        monster.health.add(-73)
        monster.aliveCheck()
        if(monster.isAlive != True):
          break
        
        player.health.add(-25)
        player.aliveCheck()
        if(player.isAlive != True):
          break

      elif (ans == 'b'):
        print(f"You strain to pick up the {monster.name}, dealing 85 damage but losing 35 stamina.",
        f"\nThe {monster.name} struggles to get back up.\n")

        monster.health.add(-85)
        monster.aliveCheck()
        if(monster.isAlive != True):
          break

        player.stamina.add(-35)
        player.aliveCheck()
        if(player.isAlive != True):
          break

      elif (ans == 'c'):
        print(f"You dance your heart out, reducing {monster.name}'s spirit by  41.",
        f"\nThe {monster.name} belts out an undescribable cry, reducing your sanity by 25.\n")

        monster.mana.add(-41)
        monster.aliveCheck()
        if(monster.isAlive != True):
          break

        player.sanity.add(-25)
        player.aliveCheck()
        if(player.isAlive != True):
          break

      else:
        pass
  elif (ans == 'b'):
    print("You commit ritual sudoku and die.\n")
    player.isAlive = False
  else:
    pass
  return player, monster

(player, monster)= gameLoop()
