import random
from math import floor, ceil
from pyGame.game_colors import *
from pyGame.magic import *

class Person:
    def __init__(self, name, cclass, hp, mp, atk, df, magic=[], items=[]):
        self.name = name
        self.cclass = cclass
        self.maxhp = hp
        self.currhp = hp
        self.maxmp = mp
        self.currmp = mp
        self.atkh = ceil(atk * 1.1)
        self.atkl = floor(atk * 0.9)
        self.df = df
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Cast Spell", "Use Item"]
        self.arcane_spells = []
        self.divine_spells = []
        self.has_arcane_magic = False
        self.has_divine_magic = False

    def get_name(self):
        return self.name

    def get_hp(self):
        return self.currhp

    def get_maxhp(self):
        return self.maxhp

    def get_mp(self):
        return self.currmp

    def get_maxmp(self):
        return self.maxmp

    def get_enemy_stats(self):
        hp_bar =""
        bar_ticks = (self.currhp / self.maxhp) * 100 / 2 - 2
        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 48:
            hp_bar += " "

        hp_string = str(self.currhp) + "/" + str(self.maxhp)
        current_hp = ""
        if len(hp_string) < 13:
            decreased = 13 - len(hp_string)
            while decreased > 0:
                current_hp += " "
                decreased -= 1
            current_hp += hp_string
        else:
            current_hp += hp_string

        print(nformat.BOLD + self.name + "   " + current_hp +
              " |" + ncolor.RED + hp_bar + ncolor.ENDC + "|   ")

    def get_stats(self):
        hp_bar = ""
        bar_ticks = (self.currhp / self.maxhp) * 100 / 4
        mp_bar = ""
        mp_ticks = ( self.currmp / self.maxmp) * 100 / 10

        while bar_ticks > 0:
            hp_bar += "█"
            bar_ticks -= 1

        while len(hp_bar) < 25:
            hp_bar += " "

        while mp_ticks > 0:
            mp_bar += "█"
            mp_ticks -= 1

        while len(mp_bar) < 10:
            mp_bar += " "

        hp_string = str(self.currhp) + "/" + str(self.maxhp)
        current_hp = ""
        if len(hp_string) < 13:
            decreased = 13 - len(hp_string)
            while decreased > 0:
                current_hp += " "
                decreased -= 1
            current_hp += hp_string
        else:
            current_hp += hp_string
        mp_string = str(self.currmp) + "/" + str(self.maxmp)
        current_mp =""
        if len(mp_string) < 7:
            decreased = 7 - len(mp_string)
            while decreased > 0:
                current_mp += " "
                decreased -=1
            current_mp += mp_string
        else:
            current_mp += mp_string

        print(nformat.BOLD + self.name + "   " + current_hp +
              " |" + ncolor.GREEN + hp_bar + ncolor.ENDC + "|   " +
              current_mp + " |" + ncolor.BLUE + mp_bar + ncolor.ENDC + "| ")

    def calc_atk_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def take_damage(self, dmg):
        self.currhp -= dmg
        if self.currhp < 0:
            self.currhp = 0
        return self.currhp

    def heal(self, amount):
        self.currhp += amount
        if self.currhp > self.maxhp:
            self.currhp = self.maxhp

    def choose_action(self):
        choice = 1
        print(ncolor.BLUE + nformat.BOLD + "Actions:" + nformat.EBOLD + ncolor.ENDC)
        for item in self.actions:
            print(str(choice) + ":", item)
            choice+=1

    def choose_magic(self):
        choice = 1
        print(ncolor.BLUE + nformat.BOLD + "Spells:" + nformat.EBOLD + ncolor.ENDC)
        if self.has_arcane_magic:
            print(str(choice) + ": Arcane")
            choice += 1
        if self.has_divine_magic:
            print(str(choice) + ": Divine")
            choice += 1
        spell_type_choice = int(input("Enter spell type choice:"))
        # 1 - Arcane
        # 2 - Divine
        choice = 1
        if spell_type_choice == 1:
            for item in self.arcane_spells:
                print(str(choice) + ":" + item.get_spellname())
                choice += 1
            spell_choice = int(input("Enter spell choice:"))
            return self.arcane_spells[spell_choice-1]
        elif spell_type_choice == 2:
            for item in self.divine_spells:
                print(str(choice) + ":" + item.get_spellname())
                choice += 1
            spell_choice = int(input("Enter spell choice:"))
            return self.divine_spells[spell_choice-1]
        else:
            print(nformat.BOLD + ncolor.RED + "***********Way to crash the game, idiot***********" + nformat.EBOLD + ncolor.ENDC)

    def reduce_mp(self,cost):
        self.currmp -= cost

    def update_spellbook(self):
        for item in self.magic:
            spell_type = item.get_spell_type()
            if spell_type == "Arcane":
                self.arcane_spells.append(item)
                self.has_arcane_magic = True
            elif spell_type == "Divine":
                self.divine_spells.append(item)
                self.has_divine_magic = True







