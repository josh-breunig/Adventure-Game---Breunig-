import time
import random


def print_pause(message):
    time.sleep(2)
    print(message)


def greeting(villain):
    print_pause("You find yourself standing in an open field,"
                " filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + villain + " is somewhere around here,"
                " and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand your hold your trusty"
                " (but not very effective) dagger.")


def first_move(items, villain):
    print_pause("")
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    while True:
        path = input("(Please enter 1 or 2) \n")
        if path == '1':
            house(items, villain)
            break
        elif path == '2':
            cave(items, villain)
            break


def house(items, villain):
    print_pause("You approach the door of the house")
    print_pause("You are about to knock when the door opens"
                " and out steps a " + villain)
    print_pause("Yikes!  This is the " + villain + "'s house!")
    print_pause("The " + villain + " attacks you!")
    while True:
        if "sword" in items:
            flee_or_not = input("Would you like to (1) fight "
                                "or (2) run away? \n")
            if flee_or_not == '1':
                print_pause("As the " + villain + " attacks,"
                            " you unsheath your new sword")
                print_pause("The Sword of Ogoroth shines brightly in your hand"
                            " as you brace yourself for the attack.")
                print_pause("But the " + villain + " takes one look at"
                            " your shiny new toy and runs away!")
                print_pause("You have ride the town of the "
                            + villain + " You are victorious!")
                end_game()
            elif flee_or_not == '2':
                print_pause("You run back into the field. "
                            "Luckily, you don't seem to have been followed.")
                first_move(items, villain)
        else:
            print_pause("You feel a bit under-prepared for this,"
                        " what with only having a tiny dagger.")
            flee_or_not = input("Would you like to (1) fight "
                                "or (2) run away? \n")
            if flee_or_not == '1':
                print_pause("You did your best...")
                print_pause("but your dagger is no match for the " + villain)
                print_pause("You have been defeated!")
                end_game()
            elif flee_or_not == '2':
                print_pause("You run back into the field. "
                            "Luckily, you don't seem to have been followed.")
                first_move(items, villain)


def cave(items, villain):
    print_pause("You peer cautiously into the cave.")
    while True:
        if "sword" in items:
            print_pause("You've already been here before, and gotten"
                        " all the good stuff.  It's just an empty cave now")
            first_move(items, villain)
        else:
            print_pause("It turns out to be only a very small cave.")
            print_pause("Your eye catches a glint of metal behind a rock.")
            print_pause("You have found the magical Sword of Ogoroth!")
            print_pause("You discard your silly old dagger"
                        " and take the sword with you.")
            print_pause("You walk back out to the field.")
            items.append("sword")
            first_move(items, villain)


def end_game():
    play_again = input("Would you like to play again? (y/n) ")
    if play_again == 'y':
        print_pause("Excellent!  Restarting... ")
        play_game()
    if play_again == 'n':
        print_pause("OK. Goodbye!")
        quit()


def play_game():
    villain_list = ["dragon", "wicked fairie",
                    "evil lizard", "wild polar bear",
                    "giant beetle"]
    villain = random.choice(villain_list)
    items = []
    greeting(villain)
    first_move(items, villain)


play_game()
