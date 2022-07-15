from abc import ABC, abstractmethod

class WeaponBehavior(ABC):
    """The Weapon Behavior"""
    @abstractmethod
    def use_weapon():
        raise NotImplementedError

class SwordBehavior(WeaponBehavior):
    def use_weapon(self):
        print("Implementing swing a Sword")

class BowAndArrowBehavior(WeaponBehavior):
    def use_weapon(self):
        print("Implementing shot with an Arrow")

class KnifeBehavior(WeaponBehavior):
    def use_weapon(self):
        print("Implementing cutting with a Knife")

class AxeBehavior(WeaponBehavior):
    def use_weapon(self):
        print("Implementing chopping with an Axe")


class Character:
    def __init__(self, weapon: WeaponBehavior) -> None:
        self.weapon = weapon

    def use_weapon(self):
        self.weapon.use_weapon()

    def fighting(self):
        pass


class King(Character):
    def __init__(self, weapon: WeaponBehavior) -> None:
        super().__init__(weapon)

    def fighting(self):
        print("The King")


class Queen(Character):
    def __init__(self, weapon: WeaponBehavior) -> None:
        super().__init__(weapon)

    def fighting(self):
        print("The Queen")



def main():
    king = King(KnifeBehavior)
    king.fighting()
    king.use_weapon()
    print("-"*80)
    queen = Queen(BowAndArrowBehavior)
    queen.fighting()
    queen.use_weapon()

if __name__ == "__main__":
    main()
        
