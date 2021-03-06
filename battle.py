from enum import Enum
from random import randint

# pools
class PoolType(Enum):
  HEALTH = 1
  MANA = 2
  STAMINA = 3
  SANITY = 4
  HUNGER = 5

class ItemType(Enum):
  WEAP = 1
  ARMOR = 2
  ACCESS = 3
  CONSUME = 4

class Item:
  def __init__(self, name = "Empty", healthDamage = 0, manaDamage = 0, staminaDamage = 0, sanityDamage = 0, hungerDamage = 0, hitrange = 0, critchance = 0, healthRestore = 0, manaRestore = 0, staminaRestore = 0, sanityRestore = 0, hungerRestore = 0, healthMax= 0, manaMax = 0, staminaMax = 0, sanityMax = 0, hungerMax = 0, count = 0, itemtype = ItemType.CONSUME):
    
    self.name = name
    
    self.healthDamage = healthDamage
    self.manaDamage = manaDamage
    self.staminaDamage = staminaDamage
    self.sanityDamage = sanityDamage
    self.hungerDamage = hungerDamage
    
    # meant for weapons only
    self.hitrange = hitrange
    self.critchance = critchance
    
    # meant for consumables
    self.healthRestore = healthRestore
    self.manaRestore = manaRestore
    self.staminaRestore = manaRestore
    self.sanityRestore = sanityRestore
    self.hungerRestore = sanityRestore
    
    # bonus stats!
    self.healthMax = healthMax
    self.manaMax = manaMax
    self.staminaMax = staminaMax
    self.sanityMax = sanityMax
    self.hungerMax = hungerMax
    
    self.itemtype = itemtype
    
    if(self.itemtype == ItemType.CONSUME):
      self.count = count
    else:
      self.count = 1
    
  def varianceRoll(self, value):
    r = randint(0, self.hitrange)
    return value * (100 - r)/100
    
  def criticalRoll(self, chance):
    r = randint(0, 100)
    return r <= chance

# Planning: Items come in many types, primarily Equippable items and Usable/Consumable items
# Player has Equipped, Equipped grants Stats, Player Uses items, Items [Do things]

class Action:
  def __init__(self, name = 'default_action'):
    self.name = name
  
  # Use weapon?
  # Use Stats of Weapon + Player
  # Do damage? 
  # Action = Skill?
  
  # Planning: Actions represent Fighting, Skills, Specials, and Accessing Inventory/items
  # Player Has Actions, Player Has Skills
    
class Pool:
  base = 100

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
  # PM = Pool Multiplier
  BASE_P = 100
  HEALTH_PM = 10
  MANA_PM = 8
  STAM_PM = 9
  SANITY_PM = 7
  HUNGER_PM = 11
  
  def __init__(self, name, strength = 1, psych = 1, vitality = 1, sustenance = 1, intelligence = 1, player = False):
    self.isAlive = True
    self.isPlayer = player
    self.name = name
    self.actions = ['Fight']
    self.bag = []
    
    self.weapon = Item(itemtype = ItemType.WEAP)
    self.armor = Item(itemtype = ItemType.ARMOR)
    self.access = Item(itemtype = ItemType.ACCESS)
    
    self.vitality = vitality + Entity.BASE_P
    self.intelligence = intelligence + Entity.BASE_P
    self.strength = strength  + Entity.BASE_P
    self.psych = psych + Entity.BASE_P
    self.sustenance = sustenance + Entity.BASE_P
    
    self.health = self.vitality * Entity.HEALTH_PM
    self.mana = self.intelligence * Entity.MANA_PM
    self.stamina = self.strength * Entity.STAM_PM
    self.sanity = self.psych * Entity.SANITY_PM
    self.hunger = self.sustenance * Entity.HUNGER_PM
    
    self.healthDamage = 5
    self.manaDamage = 5
    self.staminaDamage = 5
    self.sanityDamage = 5
    self.hungerDamage = 5
    
    self.healthDamageBonus = 0
    self.manaDamageBonus = 0
    self.staminaDamageBonus = 0
    self.sanityDamageBonus = 0
    self.hungerDamgeBonus = 0 
    
  def aliveCheck(self):
    if (self.health.val <= 0 or self.stamina.val <= 0 or self.sanity.val <= 0 or self.mana.val <= 0 or self.hunger.val <= 0):
      self.isAlive = False
      if (self.isPlayer):
        print(f"{self.name} is dead.\nGame Over")
      else:
        print(f"The {self.name} is dead.\nYou Win!")
    else:
      self.isAlive = True
  
  def intoBag(self, *items):
    for item in items:
      if (isinstance(item, Item)):
        self.bag.append(item)
      else:
        raise Exception("You picked up a non-item somehow.")
      
  # Should add Item objects to Inventory aka 'bag'
    
  def fromBag(self, *items):
    for item in items:
      if (isinstance(item, Item)):
        self.bag.remove(item)
      else:
        raise Exception("No item to remove")
        
  # Should remove Item objects from Inventory
  
  def equip(self, *items):
    for item in items:
      if item in self.bag or item.name == "Empty":
        if (item.itemtype == ItemType.WEAP):
          self.weapon = item
          self.statsBonusUpdate()
        elif (item.itemtype == ItemType.ARMOR):
          self.armor = item
          self.statsBonusUpdate()
        elif (item.itemtype == ItemType.ACCESS):
          self.access = item
          self.statsBonusUpdate()
        else:
          print("Item cannot be equipped.")
      else:
          raise Exception("Item not found in inventory.")

  # Checks item in bag, then...
  # This method should Equip an Item to the Entity -- check?
  # Then it should call the update method to add the Item stats to the Entity
  
  def use(self, consumable):
    # use a Consumable
    if (consumable.itemtype == ItemType.CONSUME):
      if consumable in self.bag:
        self.health += consumable.healthRestore
        consumable.count -= 1
        if consumable.count < 1:
          self.fromBag(consumable)

    else:
      print("You cannot use this item that way!")
  
  def statsBonusUpdate(self):
    self.healthDamageBonus = self.weapon.healthDamage + self.armor.healthDamage + self.access.healthDamage
    self.manaDamageBonus = self.weapon.manaDamage + self.armor.manaDamage + self.access.manaDamage
    self.staminaDamageBonus = self.weapon.staminaDamage + self.armor.staminaDamage + self.access.staminaDamage
    self.sanityDamageBonus = self.weapon.sanityDamage + self.armor.sanityDamage + self.access.sanityDamage
    self.hungerDamgeBonus = self.weapon.hungerDamage + self.armor.hungerDamage + self.access.hungerDamage
  
  def attack(self):
    if (self.weapon.name != "Empty"):
      healthDamage = self.weapon.varianceRoll(self.healthDamageBonus)
      if (self.weapon.criticalRoll(self.weapon.critchance)):
        healthDamage = (175 * healthDamage / 100)
        print("Critical Hit!")
      healthDamage = "%.0f" % healthDamage
      staminaCost = 8
      print(f"You attack with your {self.weapon.name} dealing {healthDamage} damage, costing {staminaCost} stamina.")
      # self.stamina.add(-staminaCost)
      # self.hunger.add(-4)
      # self.aliveCheck()
    else:
      print("Requires equipped weapon")

class Question:
  def __init__(self, text, options, outcomes):
    self.text = text
    self.options = options
    self.outcomes = outcomes

def playerPrompt():
  name = input("\nWhat is your name?")
  answerKey = ['a','b','c','d','e']
  
  color = Question("\nWhat is your favorite color?", 
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
    
  action = Question("\nWhat would you rather be?", 
    {"a":"Acrobat",
    "b":"Dancer",
    "c":"Singer",
    "d":"Talker",
    "e":"Weight lifter"},
    
    {"a":lambda: player.actions.append('Flip over'),
    "b":lambda: player.actions.append('Dance with'),
    "c":lambda: player.actions.append('Sing at'),
    "d":lambda: player.actions.append('Converse with'),
    "e":lambda: player.actions.append('Lift')})
    
  weapon = Question("\nWhat's your weapon of choice?", 
    {"a":"Rubber Chicken",
    "b":"Baseball Bat",
    "c":"Crossbow",
    "d":"Chainsaw",
    "e":"Magic Wand"},
    
    {"a":lambda: player.inventory.append('rubber chicken'),
    "b":lambda: player.inventory.append('baseball bat'),
    "c":lambda: player.inventory.append('crossbow'),
    "d":lambda: player.inventory.append('chainsaw'),
    "e":lambda: player.inventory.append('magic wand')})
  
  ans = ''
  while (ans not in answerKey):
    ans = input(f"{color.text}\nA) {color.options['a']}\nB) {color.options['b']}\nC) {color.options['c']}\nD) {color.options['d']}\nE) {color.options['e']}\n").lower()
  colorAns = ans
  
  ans = ''
  while(ans not in answerKey):
    ans = input(f"{action.text}\nA) {action.options['a']}\nB) {action.options['b']}\nC) {action.options['c']}\nD) {action.options['d']}\nE) {action.options['e']}\n").lower()
  actionAns = ans
  
  ans = ''
  while(ans not in answerKey):
    ans = input(f"{weapon.text}\nA) {weapon.options['a']}\nB) {weapon.options['b']}\nC) {weapon.options['c']}\nD) {weapon.options['d']}\nE) {weapon.options['e']}\n").lower()
  weaponAns = ans

  player = Entity(name, player = True)
  color.outcomes[colorAns]()
  action.outcomes[actionAns]()
  weapon.outcomes[weaponAns]()
  
  return player

def gameLoop():
  print(f"You are in a winding and dangerous dungeon.","\nYou are unaware how you got here, but you must journey forward to escape.")
  while(True):
    ans = input(f"\nWill you journey forward?\nA) Yes\nB) No\n").lower()
    if (ans == 'a' or ans == 'b'):
      break
  if(ans == 'b'):
    print("You commit ritual sudoku and die.\nGame Over.")
    
  if (ans == 'a'):
    player = playerPrompt()
    monster = Entity("Eldritch Horror", vitality = 15, sustenance = 8)

    print(f"\nYou have encountered a {monster.name}.")
    while(player.isAlive and monster.isAlive):
      ans = input(f"\nWhat action will you take?\nA) {player.actions[0]} with {player.inventory[0]}\nB) {player.actions[1]} it\nC) Something else\n").lower()
      if (ans == 'a'):
        print(f"You attack the monster with your {player.inventory[0]} dealing 73 damage.",
        "\nIt lashes back with its tentacles, dealing 25 damage.\n")
        
        monster.health.add(-73)
        monster.aliveCheck()
        if not(monster.isAlive):
          break
        
        player.health.add(-25)
        player.aliveCheck()
        if not(player.isAlive):
          break

      elif (ans == 'b'):
        print(f"You {player.actions[1]} it, dealing 85 damage but losing 35 stamina.",
        f"\nThe {monster.name} struggles to get back up.\n")

        monster.health.add(-85)
        monster.aliveCheck()
        if not(monster.isAlive):
          break

        player.stamina.add(-35)
        player.aliveCheck()
        if not(player.isAlive):
          break

      elif (ans == 'c'):
        print(f"You stare blankly at it, reducing the {monster.name}'s spirit by  41.",
        f"\nThe {monster.name} belts out an undescribable cry, reducing your sanity by 25.\n")

        monster.mana.add(-41)
        monster.aliveCheck()
        if not(monster.isAlive):
          break

        player.sanity.add(-25)
        player.aliveCheck()
        if not(player.isAlive):
          break
      else:
        pass
  else:
    pass

player = Entity("Joe", player = True)
hammer = Item(name = "hammer", itemtype = ItemType.WEAP, healthDamage = 80, hitrange = 15, critchance = 8)
dagger = Item("dagger", 50, itemtype = ItemType.WEAP, critchance = 16)
flute = Item("flute", manaDamage = 50, itemtype = ItemType.WEAP, critchance = 23)
potion = Item("healing potion", healthRestore = 25, itemtype = ItemType.CONSUME)
player.intoBag(hammer, dagger, flute, potion)
player.equip(hammer)

# stab = Action(name = "stab", descript = "stab at", damage = 15, damageType = "health", cost = 10, costType = "stamina", )
# stab.showStats()
