import random
import sys
from Neighborhood import Neighborhood
from Player import Player

def main():
    # Condition for psuedo game-loop to keep running
    game_on = True
    # Neighborhood object
    N = Neighborhood()
    # Player object
    P = Player()
    print("Welcome to the Neighborhood! When prompted for a " +  
            "command please type them in using ALL LOWER-CASE " +
            "letters please!\n")
    # Test print grid
    N.print_grid()

    def print_space():
        print('\n***********************************************************************************************')
        print('***********************************************************************************************')
        print('***********************************************************************************************')
        print('***********************************************************************************************\n')

    while(game_on):
        cmd = input("What would you like to do?\n").lower()
        cmd = cmd.strip()
        if cmd == "walk":
            dir = input("Which direction would you like to walk? north/south/east/west are valid options\n").strip()
            dir = dir.lower()
            N.walk(dir)
        elif cmd == "show monsters" and N.check_player_loc():
            # Get current house
            curr_house = N.player_loc
            if curr_house in N.house_locs:
                # Check for proper syntax
                house_index = N.house_locs.index(curr_house)
                h = N.houses[house_index]
                h.show_monsters()
        elif cmd == "attack" and N.check_player_loc():
            # Get current house
            curr_house = N.player_loc
            if curr_house in N.house_locs:
                # Check for proper syntax
                house_index = N.house_locs.index(curr_house)
                h = N.houses[house_index]
            while h.num_monsters > 0:
                if P.health_points > 0:
                    P.print_weapons()
                    choice = int(input("Which of your weapons would you like to use? Please input a number. \n" +
                    "If you would like to see the status of the monsters, input 10!\n" +
                    "If you would like to see your own status, input 11!\n"))
                    if choice == 11:
                        print_space()
                        P.print_stats()
                        continue
                    if choice == 10:
                        print_space()
                        h.show_monsters()
                        continue
                    weapon = P.weapons_list[choice]
                    for mon in h.monsters:
                        mon.get_hit(weapon, P)
                        if mon.health_points > 0:
                            print('You have hit a {}! It now has {} health points left!'.format(mon.name, mon.health_points))
                        if mon.health_points <= 0:
                            print('Congratulations, you have killed a {}!'.format(mon.name))
                            #h.monsters.remove(mon)
                            #h.num_monsters -= 1
                    if h.num_monsters == 0:
                        ##### TODO How should I break out of the while loop here if i kill all the monsters? Currently, if I kill all monsters i still get hit by one
                        break
                    # Update weapons list/weapon uses after attack
                    P.update_weapons(weapon)
                    m = h.monsters[random.randint(0, (len(h.monsters) - 1) )]
                    # Print monster that attack and resulting player hp
                    P.get_hit(m)
                    if P.health_points > 0:
                        print('Oh no! A wild {} has attacked you! You now have {} health points left!'.format(m.name, P.health_points))
                        print_space()
                    else:
                        print("Oh no! The player has died. You have lost The Game :)\n")
                        print("Goodbye for now, but if you would like to play again, " + 
                                "The Neighborhood is always waiting for you... :)\n")
                        game_on == False
                        sys.exit(1)
                # If player is dead
                else:
                    print("Oh no! The player has died. You have lost The Game :)\n")
                    print("Goodbye for now, but if you would like to play again, " + 
                            "The Neighborhood is always waiting for you... :)\n")
                    game_on == False
                    sys.exit(1)
        elif cmd == "show map":
            N.print_grid()
        elif cmd == "number of houses left":
            print('{} houses are left'.format(N.num_houses))
        elif cmd == "command list":
            # Make a dictionary with commands and short explanations
            # Print options line by line
            break;
        elif cmd == "quit":
            game_on == False
            sys.exit(1)
        else:
            print("That is not a valid command (yet). Please try another one!\n")

main()
