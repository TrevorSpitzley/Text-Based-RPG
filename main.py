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
                    choice = int(input("Which of your weapons would you like to use? Please input a number.\n"))
                    weapon = P.weapons_list[choice]
                    ##### TODO Decrement weapon uses
                    # If uses == 0 then remove from list
                    for mon in h.monsters:
                        mon.get_hit(weapon, P)
                        ###### TODO
                        if mon.health_points > 0:
                            print('You have hit a {}! It now has {} health points left!'.format(mon.name, mon.health_points))
                        else:
                            print('Congratulations, you have killed a {}!'.format(mon.name))
                            h.monsters.remove(mon)
                        # if statement for 'You hit X monster'
                        # else statement for if the hp fell below 0
                        # remove monster
                        if mon.health_points < 0:
                            h.monsters.remove(mons)
                            h.num_mons -= 1
                    m = h.monsters[random.randint(0, (len(h.monsters) - 1) )]
                    # Print monster that attack and resulting player hp
                    P.get_hit(m)
                    ##### TODO
                    # Print statement 'oh no you were hit by m and lost whatever health points'
                    # You now have whatever health points left
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
