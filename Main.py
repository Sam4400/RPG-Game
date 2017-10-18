from Classes.game import Person, bcolors
from Classes.magic import Spell
from Classes.Inventory import Item


#Create offensive magic
spell_fire = Spell("Fire", 10, 100, "Earth")
spell_thunder = Spell("Thunder", 10, 120, "Weather")
spell_blizzard = Spell("Blizzard", 15, 140, "Weather")
spell_meteor = Spell("Meteor", 20, 220, "Black")
spell_quake = Spell("Quake", 20, 220, "Earth")

#Create def magic
spell_cure = Spell("Cure", 10, 120, "Life")
spell_cura = Spell("Cura", 15, 250, "Life")

# Create items
item_potion = Item("Potion", "Potion", "Heals for 50 HP", 50)
item_hipotion = Item("Hi-Potion", "Potion", "Heals for 150 HP", 150)
item_superpotion = Item("Super-Potion", "Potion", "Heals for 250 HP", 250)
item_elixer = Item("Elixer", "Elixer", "Fully restores HP/MP of target", 0)
item_megaelixer = Item("Mega-Elixer", "Elixer", "Fully restores HP/MP of party", 0)
item_fraggrenade = Item("Frag Grenade", "Thrown Weapon", "Short fuse grenade", 150)
item_hegrenade = Item("HE Grenade", "Thrown Weapon", "High Explosive grenade", 500)

#Initialise characters
player_spells = [spell_cure, spell_fire, spell_blizzard]
player_items = [item_fraggrenade, item_potion, item_superpotion, item_elixer]

player = Person(460, 65, 60, 34, player_spells,player_items)
enemy = Person(1200, 65, 45, 25, [spell_cure, spell_thunder, spell_meteor],[item_hegrenade])

running = True

print("AN ENEMY ATTACKS!")

round_count = 1
while running:
    print("\n*********************************************************************************************************"
          "*\nRound #", round_count,"\n")

    # Choose action to take
    player.choose_action()
    choice = input("Choose action:")

    if choice == "quit":
        break

    index = int(choice) - 1

    # Attack physically
    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "damage.\nEnemy HP:", enemy.get_hp())
    # Attack with magic
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic:")) - 1

        if magic_choice == -1:
            continue

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            dmg = player.generate_damage(disad=2)
            enemy.take_damage(dmg)
            print("Not enough MP!\nYou attack at a disadvantage doing half melee damage\n"
                  "You inflict", dmg, "damage. Enemy HP is now", enemy.get_hp())

        elif spell.cost <= current_mp:
            if spell.type == "Life":
                player.heal(magic_dmg)
                print("You have healed yourself with", spell.name, "for", magic_dmg, "HP")
            else:
                enemy.take_damage(magic_dmg)
                player.reduce_mp(spell.cost)
                print("You attack with", spell.name, "for", magic_dmg, "damage.\nYou have", player.get_mp(),
                  "MP remaining.\nThe enemy has", enemy.get_hp(), "HP remaining.")
    elif index == 2:
        player.choose_items()
        item_choice = int(input("Choose item:")) - 1

        if item_choice == -1:
            continue

        item = player.items[item_choice]

        if item.type == "Potion":
            player.heal(item.prop)
            print("You have used the", item.name, "to heal for", item.prop, "HP")
        elif item.type == "Thrown Weapon":
            enemy.take_damage(item.prop)
            print("Enemy takes", item.prop, "damage from your", item.name,"\nEnemy HP is now", enemy.get_hp())

    enemy_choice = 0

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg, "\nPlayer HP", player.get_hp())

    if player.get_hp() == 0:
        print("You have died after", round_count,"rounds, your corpse was transported to the nearest graveyard.")
        running = False

    if enemy.get_hp() == 0:
        print("You defeated the enemey after", round_count, "rounds!")
        running = False

    print("Player HP is", player.get_hp(), "and Enemy HP is", enemy.get_hp())

    round_count += 1


