from dice import roll_d20, roll_d6
import random

def enemy_encounter():
    """Create a basic enemy with randomized stats."""
    enemy_types = ["Goblin", "Skeleton", "Bandit"]
    enemy_type = random.choice(enemy_types)
    return {
        "name": enemy_type,
        "hp": random.randint(10, 20),
        "attack": random.randint(3, 6),
        "defense": random.randint(1, 3)
    }

def player_attack(player, enemy):
    attack_roll = roll_d20()
    if attack_roll >= 10:
        damage = roll_d6() + player.attack
        enemy["hp"] -= damage
        print(f"You hit the {enemy['name']} for {damage} damage!")
    else:
        print("You missed!")

def enemy_attack(player, enemy):
    """Handle enemy's attack turn."""
    attack_roll = roll_d20()
    if attack_roll >= 10:
        damage = roll_d6() + enemy["attack"]
        player.hp -= damage
        print(f"The {enemy['name']} hits you for {damage} damage!")
    else:
        print(f"The {enemy['name']} misses!")

def run_combat(player):
    """Run a single round of combat with one enemy."""
    enemy = enemy_encounter()
    print(f"\nA {enemy['name']} appears!")
    print(f"Enemy HP: {enemy['hp']} | ATK: {enemy['attack']} | DEF: {enemy['defense']}\n")

    while enemy["hp"] > 0 and player.hp > 0:
        input("\nPress ENTER to attack!")
        player_attack(player, enemy)

        if enemy["hp"] <= 0:
            print(f"You defeated the {enemy['name']}!")
            break

        enemy_attack(player, enemy)

        if player.hp <= 0:
            print("\nYou have fallen...")
            break

    print(f"\nYour remaining HP: {player.hp}")
