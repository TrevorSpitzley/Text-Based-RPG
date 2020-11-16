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
    print("Welcome to The Neighborhood! The Game is simple... \n" +
          "Enter houses and defeat all of the monsters while not dying!\n")
    print("To see what options you have, type the word \'commands\' and press enter. Then go from there!\n")

    commands = [
        "\nwalk: This command will allow you to walk in any direction, after inputting a valid direction when being prompted. Valid directions include north/south/east/west.\n",
        "show monsters: When inside of a house, you can use this command to print the stats of the monsters within the house.\n",
        "attack: When inside of a house, you can use this command to initiate a battle of you versus the house's monsters.\n",
        "show map: This command will print an updated grid showing you the location of all houses and yourself\n",
        "number of houses left: This command will allow you to see the number of houses with monsters left in The Neighborhood.\n",
        "commands: This will print off the list of available commands that you have at your disposal.\n",
        "quit: This is self explanatory.\n"
    ]

    def print_commands():
        for cmd in commands:
            print(cmd)

    # Test print grid
    N.print_grid()

    def print_space():
        print('\n***********************************************************************************************')
        print('*************************************************************************************************')
        print('*************************************************************************************************')
        print('***********************************************************************************************\n')

    while (game_on):
        cmd = input("What would you like to do?\n").lower()
        cmd = cmd.strip()
        if cmd == "walk":
            dir = input("Which direction would you like to walk? north/south/east/west are valid options\n").strip()
            dir = dir.lower()
            N.walk(dir)
        elif cmd == "show monsters" and N.check_player_loc():
            # Get current house
            # curr_house = N.player_loc
            # if curr_house in N.house_locs:
            # Check for proper syntax

            # Potentially uncomment and use the above lines. If any errors arise.    
            house_index = N.house_locs.index(N.player_loc)
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
                    choice = input("Which of your weapons would you like to use? Please input a number. \n" +
                                       "If you would like to see the status of the monsters, input 10!\n" +
                                       "If you would like to see your own status, input 11!\n")
                    if choice == "quit":
                        game_on == False
                        sys.exit(1)
                    choice = int(choice)
                    if choice == 11:
                        print_space()
                        P.print_stats()
                        continue
                    if choice == 10:
                        print_space()
                        h.show_monsters()
                        continue
                    if choice >= len(P.weapons_list):
                        print_space()
                        print("Please choose a valid weapon option.\n")
                        continue
                    else:
                        weapon = P.weapons_list[choice]
                    for mon in h.monsters:
                        mon.get_hit(weapon, P)
                    # Update weapons list/weapon uses after attack
                    P.update_weapons(weapon)
                    m = h.monsters[random.randint(0, (len(h.monsters) - 1))]
                    # Print monster that attack and resulting player hp
                    P.get_hit(m)
                    if P.health_points > 0 and m.name != "Person":
                        print('Oh no! A wild {} has attacked you! You now have {} health points left!\n'.format(m.name,
                                                                                                                P.health_points))
                        print_space()
                    if P.health_points <= 0:
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
            print('{} houses are left'.format(N.mon_houses))
        elif cmd == "commands":
            print_commands()
        elif cmd == "quit":
            game_on == False
            sys.exit(1)
        else:
            print("That is not a valid command (yet). Please try another one!\n")


main()
