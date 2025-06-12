def __init__(self, name, char_class):
        # Set up basic character info
        self.name = name
        self.char_class = char_class

        # Base stats shared by all classes
        self.hp = 20
        self.attack = 5
        self.defense = 2

        # Adjust stats based on chosen class
        if char_class == "Fighter":
            self.hp += 10
            self.attack += 2
        elif char_class == "Rogue":
            self.attack += 4 

        elif char_class == "Wizard":
            self.hp -= 5
            self.attack += 5


    def __str__(self):
        return (
            f"{self.name} the {self.char_class} | "
            f"HP: {self.hp} | ATK: {self.attack} | DEF: {self.defense}"
        )
