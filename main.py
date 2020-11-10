from random import randint
import sys
import Neighborhood
from Neighborhood import Neighborhood


def main():
    # Condition for psuedo game-loop to keep running
    game_on = True
    # Neighborhood object
    N = Neighborhood()
    print("Welcome to the Neighborhood! When prompted for a " +  
            "command please type them in using ALL LOWER-CASE " +
            "letters please!\n")
    # Test print grid
    N.print_grid()

    while(game_on):
        cmd = input("What would you like to do?\n")
        if cmd == "walk":
            dir = input("Which direction would you like to walk? north/south/east/west are valid options")
            N.__walk(dir)      
        elif cmd == "attack" and N.check_player_loc():
            # Get current house
            curr_house = N.player_loc
            if curr_house in N.houses:
                # Check for proper syntax
                house_index = N.houses_locations.index(curr_house)
                h = N.houses[house_index]
            while h.num_mons > 0:
                # Create player.py
                if P.health_points > 0:
                    weapon = input("Which weapon?")
                    # Implement attack
                    P.attack(weapon)
                    # h is current house
                    for mons in h.mons_list:
                        # Every monster class needs a get hit function
                        mons.get_hit(weapon)
                    # get random int in range of len(h.mons_list)
                    # Choose random mon to attack
                    m = h.mons_list[randint]
                    # pass mon to player, inside player check m.name, decrement health based on name
                    P.get_hit(m)
                    
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
