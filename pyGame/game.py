from pyGame.game_colors import *
from pyGame.character import *
from pyGame.magic import magic

# Person(name, class, hitpoints, manapoints, attackpower, defense, spellbook[], inventory[]):
player = Person("Matt", "Sorceror", 1500, 5000, 50, 10, magic)
bad_guy = Person("BBEG", "Demon", hp=15000, mp=0, atk=150, df=40)


print("==============================================\n"
      + nformat.BOLD + ncolor.GREEN + player.get_name() + ncolor.ENDC + nformat.EBOLD +
      " begins his battle with "
      + nformat.BOLD + ncolor.RED + bad_guy.get_name() + ncolor.ENDC + nformat.EBOLD + "\n")
running = True
players = [player]
enemies = [bad_guy]
for player in players:
    player.update_spellbook()

while running:

    print("Name                   HP                           MP")
    for player in players:
        print("                      _________________________               __________")
        player.get_stats()
    print("")
    print("Enemy                 HP")
    for enemy in enemies:
        print("                      ________________________________________________")
        enemy.get_enemy_stats()

    player.choose_action()
    choice = int(input("Enter choice: "))
    if choice == 1:
        dmg = player.calc_atk_damage()
        bad_guy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage!")
    elif choice == 2:
        spell = player.choose_magic()
        cost = spell.get_cost()
        magic_dmg = spell.generate_damage()
        current_mp = player.get_mp()
        if cost > current_mp:
            print(ncolor.RED + "\nNot enough mana!\n" + ncolor.ENDC)
            continue
        if spell.get_spell_type() == "Arcane":
            player.reduce_mp(cost)
            bad_guy.take_damage(magic_dmg)
            print(ncolor.BLUE + "\n" + spell.get_spellname() + " deals", str(magic_dmg),
                  "points of damage!\n" + ncolor.ENDC)
        elif spell.get_spell_type() == "Divine":
            player.reduce_mp(cost)
            player.heal(magic_dmg)
            print(ncolor.BLUE + "\n" + spell.get_spellname() + " heals", str(magic_dmg),
                  "points of health!\n" + ncolor.ENDC)

    if bad_guy.get_hp() == 0:
        print(nformat.BOLD + ncolor.GREEN + "You won!" + ncolor.ENDC + nformat.EBOLD)
        running = False

    dmg = bad_guy.calc_atk_damage()
    player.take_damage(dmg)

    if player.get_hp() == 0:
        print(ncolor.RED + nformat.BOLD + bad_guy.get_name() + ncolor.ENDC + nformat.EBOLD + " deals", str(dmg),
              "points of damage, killing " + ncolor.GREEN + nformat.BOLD + player.get_name() + ncolor.ENDC + nformat.EBOLD + "!\n")
        print(nformat.BOLD + ncolor.RED + "You lost!" + ncolor.ENDC + nformat.EBOLD)
        running = False
    else:
        print(ncolor.RED + nformat.BOLD + bad_guy.get_name() + ncolor.ENDC + nformat.EBOLD + " deals", str(dmg),
              "points of damage!\n")
