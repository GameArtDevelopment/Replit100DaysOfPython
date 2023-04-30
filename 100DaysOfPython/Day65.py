import random

# Day 65 - Object Oriented Programming (OOP) - Inheritance
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
RESET = "\033[0m"


class Character:
    def __init__(self, name, health, magic_points):
        self.name = name
        self.health = health
        self.magic_points = magic_points

    def output_data(self):
        print(
            f"Name: {self.name:<10}Health: {self.health:<10}Magic Points: {self.magic_points:<10}")


class Player(Character):
    def __init__(self, name, health, magic_points, lives):
        super().__init__(name, health, magic_points)
        self.lives = lives

    def am_i_alive(self):
        if self.health > 0:
            print("Yes")
        else:
            print("No")


class Enemy(Character):
    def __init__(self, name, health, magic_points, enemy_type, strength):
        super().__init__(name, health, magic_points)
        self.enemy_type = enemy_type
        self.strength = strength


class Orc(Enemy):
    def __init__(self, name, health, magic_points, strength, speed):
        super().__init__(name, health, magic_points, enemy_type="Orc", strength=strength)
        self.speed = speed


class Vampire(Enemy):
    def __init__(self, name, health, magic_points, strength, is_day=True):
        super().__init__(name, health, magic_points,
                         enemy_type="Vampire", strength=strength)
        self.is_day = is_day


# Instantiate characters
player1 = Player("Alice", 100, 50, lives=3)
orc1 = Orc("Grom", 50, 0, strength=5, speed=2)
orc2 = Orc("Drog", 60, 0, strength=4, speed=3)
vampire1 = Vampire("Dracula", 80, 100, strength=8, is_day=True)
vampire2 = Vampire("Lestat", 90, 120, strength=9, is_day=False)

enemies = [orc1, orc2, vampire1, vampire2]


def print_header(text):
    print(f"\n{YELLOW}{text}{RESET}\n")


def print_character(text):
    print(f"\n{BLUE}{text}{RESET}\n")


def print_enemy(text):
    print(f"\n{GREEN}{text}{RESET}\n")


def print_error(text):
    print(f"{RED}Error: {text}{RESET}")


def print_success(text):
    print(f"{RED}{text}{RESET}")


def generate_player():
    print_character("Generating player information...")
    print(f"{'Name':<10}{'Health':<10}{'Magic Points':<10}")
    player1.output_data()
    print(f"Lives: {player1.lives}")
    player1.am_i_alive()


def generate_enemies():
    print_enemy("Generating enemy information...")
    print(f"{'Name':<10}{'Health':<10}{'Magic Points':<10}{'Type':<10}{'Strength':<10}{'Speed/Is Day':<10}")
    for enemy in enemies:
        enemy.output_data()
        print(f"{enemy.enemy_type:<10}{enemy.strength:<10}", end="")
        if isinstance(enemy, Orc):
            print(f"{enemy.speed:<10}")
        elif isinstance(enemy, Vampire):
            print(f"{enemy.is_day:<10}")
        else:
            print()


def main():
    print_header("="*24)
    print_header("* Welcome to the game! *")
    print_header("="*24)
    while True:
        print("\nPlease choose an option:")
        print("1. Generate player information")
        print("2. Generate enemy information")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            generate_player()
        elif choice == "2":
            generate_enemies()
        elif choice == "3":
            print()
            print_success("Exiting the game...")
            break
        else:
            print_error("Invalid choice. Please try again.")
            continue


if __name__ == "__main__":
    main()

print()
print("Program terminated.")
print()
print("Thank you for using my program.")
print()
