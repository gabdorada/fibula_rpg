class Entity:
    # Base class defining the standard structure for any entity in the game.
    def __init__(self, name: str, hp: int, attack_power: int):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack_power = attack_power

    def is_alive(self) -> bool:
        # Checks if the entity has remaining health points.
        return self.hp > 0 

    def take_damage(self, damage: int) -> bool:
        # AApplies damage to HP and ensures it does not drop below zero.
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0
        print(f"{self.name} took {damage} damage! Remaining HP: {self.hp}/{self.max_hp}")

    def attack(self, target: 'Entity') -> None:
        # Performs a direct attack on a target entity.
        print(f"\n⚔️ {self.name} attacks {target.name}!")
        target.take_damage(self.attack_power)