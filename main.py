from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


class Sword(Weapon):
    def attack(self):
        print("sword attack")


class Bow(Weapon):
    def attack(self):
        print("bow attack")


class Fighter:
    def __init__(self, name, weapon: Weapon):
        self.weapon = weapon
        self.name = name

    def change_weapon(self, new_weapon: Weapon):
        self.weapon = new_weapon
        print(f'{self.name} changed weapon to {new_weapon.__class__.__name__}')


class FighterAttack():
    def __init__(self, fighter: Fighter):
        self.fighter = fighter

    def attack(self, target):
        print(f'{self.fighter.name} initiate attack with: {self.fighter.weapon.__class__.__name__}')
        self.fighter.weapon.attack()
        print(f'{target.name} is dead!')


class Monster:
    def __init__(self, name):
        self.name = name


monster1 = Monster('Cthulhu')
sword1 = Sword()
bow1 = Bow()
fighter1 = Fighter("Bob", sword1)

attack = FighterAttack(fighter1)
attack.attack(monster1)

fighter1.change_weapon(bow1)
attack.attack(monster1)



