from entities.player import Player
from entities.monster import Monster
from utils.combat import start_combat

def show_logo():
    logo = r"""
         \ _^ /   ,^,
         \>@@</   ((
Art by    (..)    );)
 Charles   vv\^^^^ /
 Caffrey /==   ))) )
         ( ==/ )=< \
         {{{)=(}}}(_}}}
"""
    print(logo)

def main():
    show_logo()

    print("=" * 45)
    print("   WELCOME TO FIBULA RPG (OOP EDITION)   ")
    print("=" * 45)

    hero_name = input("\nEnter your hero's name: ").strip()
    if not hero_name:
        hero_name = "Shadow Knight"

    # Instantiate player
    player = Player(name=hero_name, hp=100, attack_power=18)

    # Dungeon monsters sequence
    dungeon = [
        Monster(name="Goblin", hp=30, attack_power=8, xp_reward=30),
        Monster(name="Orc", hp=60, attack_power=14, xp_reward=60),
        Monster(name="Dragon", hp=120, attack_power=22, xp_reward=150)
    ]

    # Main gameplay loop 
    for monster in dungeon:
        victory = start_combat(player, monster)
        if not victory:
            break 
        print("\nYou venture deeper into the dungeon...")

        if player.is_alive():
            print("\n🎉 CONGRATULATIONS! You cleared the dungeon and became a legend!")

if __name__ == "__main__":
    main()

