from math import ceil, floor
import random

class Spell:
    def __init__(self, name, cost, dmg, type):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.type = type

    def get_spellname(self):
        return self.name

    def get_cost(self):
        return self.cost

    def generate_damage(self):
        low = floor(self.dmg * 0.8)
        high = ceil(self.dmg * 1.2)
        return random.randrange(low, high)

    def get_spell_type(self):
        return self.type

burn = Spell("Burn", cost=10, dmg=20, type="Arcane")
shock = Spell("Shock", cost=10, dmg=20, type="Arcane")
freeze = Spell("Freeze", cost=10, dmg=20, type="Arcane")
fireball = Spell("Fireball", cost=20, dmg=50, type="Arcane")
lightning_bolt = Spell("Lightning Bolt", cost=25, dmg=70, type="Arcane")
blizzard = Spell("Blizzard", cost=350, dmg=1500, type="Arcane")
cure = Spell("Cure", cost=5, dmg=30, type="Divine")
heal = Spell("Heal", cost=300, dmg=1500, type="Divine")

magic = [burn, shock, freeze, fireball, lightning_bolt, blizzard, cure, heal]