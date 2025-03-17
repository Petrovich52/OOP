from abc import ABC, abstractmethod

# Абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Класс меча
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

# Класс лука
class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

# Класс бойца
class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self):
        return self.weapon.attack()

# Класс монстра
class Monster:
    def defeated(self):
        return "Монстр побежден!"

# Создаем бойца и монстра
fighter = Fighter(Sword())  # Боец начинает с меча
monster = Monster()

# Бой с мечом
print("Боец выбирает меч.")
print(fighter.attack())
print(monster.defeated())

# Боец меняет оружие на лук
fighter.change_weapon(Bow())

# Бой с луком
print("\nБоец выбирает лук.")
print(fighter.attack())
print(monster.defeated())