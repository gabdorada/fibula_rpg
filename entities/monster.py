from entities.entity import Entity

class Monster(Entity):
    # Monster class representing enemies in the game.

    def __init__(self, name: str, hp: int, attack_power: int, xp_reward: int):
        super().__init__(name, hp, attack_power)
        self.xp_reward = xp_reward