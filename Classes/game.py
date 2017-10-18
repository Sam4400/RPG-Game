import random


class bcolors:
    HEADER = '\033[95M'
    OKBLUE = '\033[94M'
    OKGREEN = '\033[92M'
    WARNING = '\033[93M'
    FAIL = '\033[91M'
    ENDC = '\033[0M'
    BOLD = '\033[1M'
    UNDERLINE = '\033[4M'


class Person:
    def __init__(self, hp, mp, atk, df, magic, items):
        self.maxhp = hp
        self.hp = hp
        self.maxmp = mp
        self.mp = mp
        self.atkh = atk + 10
        self.atkl = atk - 10
        self.df = df
        self.magic = magic
        self.action = ["Attack", "Magic", "Items"]
        self.items = items

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.maxhp:
            self.hp = self.maxhp

    def generate_damage(self, disad=1):
        return random.randrange(self.atkl, self.atkh) / disad

    def take_damage(self, dmg):
        self.hp -= dmg
        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.maxhp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.maxmp

    def reduce_mp(self, cost):
        self.mp -= cost

    def choose_magic(self):
        i = 1
        print("Magic:")
        for spell in self.magic:
            print(str(i) +":", spell.name, "(Cost", str(spell.cost) +")")
            i += 1

    def choose_items(self):
        i = 1
        print("Items:")
        for item in self.items:
            print(str(i) + ":", item.name, "QTY: 5", "\n  ", item.description)
            i += 1

    def choose_action(self):
        i = 1
        print("Actions:")
        for item in self.action:
            print(str(i) + ":", item)
            i += 1
            2
'''
    def get_spell_name(self, i):
        return self.magic[i]["name"]

    def get_spell_mp_cost(self, i):
        return self.magic[i]["cost"]
                  
    def generate_spell_damage(self, i):
        mgl = self.magic[i]["dmg"] - 5
        mgh = self.magic[i]["dmg"] + 5
        return random.randrange(mgl, mgh)
'''