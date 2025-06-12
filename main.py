from character import character

def create_character():
    print("Welcome to Dungeon Crawl!")
    name = input("Enter your hero's name:")

    print("Choose your class:")
    print("1. Fighter")
    print("2. Rogue")
    print("3. Wizard")

    class_choice = input("Select a Class:")
    classes = {"1:" "Fighter", "2:" "Rogue", "3:" "Wizard"}
    char_class = classes.get(class_choice, "Fighter")

    player = Character(name, char_class)
    print(f"\nCharacter Created:\n{player}\n")
    return player

def main():
    player = create_character()
    print("You stand at the mouth of a dark dungeon...")
    # Temporary: Exit after showing character
    print("More coming soon!")

if __name__ == "__main__":
    main()  # Run the main function when this script is executed