from entities.entity import Entity

class Player(Entity):
    # Player class that inherits from Entity and manages leveling and consumables.

    def __init__(self, name: str, hp: int = 100, attack_power: int = 15):
        super().__init__(name, hp, attack_power) 

    # Player-specific attributes.
        self.level = 1
        self.xp = 0 
        self.xp_to_next_level = 50
        self.potions = 2

    def use_potion(self) -> bool:
        # Consumes a potion to restore player HP.
        if self.potions > 0:
            heal_amount = 30
            self.hp = min(self.max_hp, self.hp + heal_amount)
            self.potions -= 1
            print(f"🧪 {self.name} used a potion and healed {heal_amount} HP! Current HP: {self.hp}/{self.max_hp}")
            print(f"Potions left: {self.potions}")
        else:
            print("❌ You are out of potions!")

    def gain_potion(self, amount: int = 1) -> None:
        # Adds potions to the player's inventory.
        self.potions += amount
        print(f"🎒 {self.name} found {amount} potion(s)! Total: {self.potions}")

    def gain_xp(self, amount: int) -> None:
        # Adds XP and automatically triggers level recalculation.
        self.xp += amount
        print(f"✨ {self.name} earned {amount} XP! (Total: {self.xp}/{self.xp_to_next_level})")
        self.calculate_level()

    def calculate_level(self) -> None:
        # Handles level-up progression and stat increments.
        while self.xp >= self.xp_to_next_level:
            self.xp -= self.xp_to_next_level
            self.level += 1
            self.xp_to_next_level = int(self.xp_to_next_level * 1.5)

            # Stat progression on level up
            self.max_hp += 20
            self.hp = self.max_hp
            self.attack_power += 5

            print(f"\n🎉 CONGRATULATIONS! {self.name} reached Level {self.level}!")
            print(f"Stats increased: Max HP = {self.max_hp} | Attack Power = {self.attack_power}")
