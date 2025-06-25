locations = ["Entrance Hall", "Library", "Kitchen", "Garden"]
descriptions = [
    "A grand foyer with a crystal chandelier.",
    "Dusty bookshelves stretch from floor to ceiling.",
    "Copper pots hang above an old stone hearth.",
    "Overgrown vines twist around marble statues."
]
commands = ["N", "S", "E", "W", "quit", "help"]

current_location = 0

player_name = input("Enter your name: ")
print("Welcome to the Mystery Mansion,", player_name + "!")
print("Type N, S, E, or W to move. Type 'help' for help or 'quit' to leave.\n")
running = True
while running:
    print("You are in the", locations[current_location] + ".")
    print(descriptions[current_location])
    user_input = input("Which direction do you want to go? ").strip().lower()

    if user_input == "n":
        print("You move north.\n")
        current_location = (current_location + 1) % 4
    elif user_input == "s":
        print("You move south.\n")
        current_location = (current_location - 1) % 4
    elif user_input == "e":
        print("You move east.\n")
    elif user_input == "w":
        print("You move west.\n")
    elif user_input == "help":
        print("Valid commands: N, S, E, W, help, quit\n")
    elif user_input == "quit":
        print("Goodbye,", player_name + "!")
        running = False
    else:
        print("Invalid command. Please enter N, S, E, W, help, or quit.\n")