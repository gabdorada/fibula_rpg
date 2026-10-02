import random
from entities.player import Player
from entities.monster import Monster

def start_combat(player: Player, monster: Monster) -> bool:
    # Handles turn-based combat between the player and a monster.
    print("\n========================================")
    print(f"⚠️ A WILD {monster.name.upper()} APPEARED! ⚠️")
    print("========================================")

    while player.is_alive() and monster.is_alive():
        print("\n--- YOUR TURN ---")
        print(f"{player.name} Status: HP {player.hp}/{player.max_hp} | Potions: {player.potions}")
        print(f"{monster.name} Status: HP {monster.hp}/{monster.max_hp}")
        print("1. Attack")
        print("2. Use Potion")

        choice = input("Choose your action (1 or 2): ").strip()

        if choice == "1":
            player.attack(monster)
        elif choice == "2":
            player.use_potion()
        else:
            print("Invalid choice. Turn skipped.")

        # Monster turn (if still alive)
        if monster.is_alive():
            monster.attack(player)

    # Combat Resolution 
    if player.is_alive():
        print(f"🏆 You defeated the {monster.name}!")
        player.gain_xp(monster.xp_reward)

        # 30% chance for a potion drop
        if random.random() < 0.3:
            player.gain_potion(1)

        return True 
    else:
        print(f"\n☠️ {player.name} was defeated... Game Over!")
        return False