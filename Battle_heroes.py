import random
import time


class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = self.attack_power
        other.health -= damage
        return damage

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name} (Здоровье: {self.health}, Атака: {self.attack_power})"


class Game:
    def __init__(self):
        player_name = input("Введите имя вашего героя: ")
        self.player = Hero(player_name)

        # Создаем героя для компьютера со случайными характеристиками
        computer_names = ["Темный рыцарь", "Злой маг", "Орк-воин", "Нежить", "Демон"]
        self.computer = Hero(
            name=random.choice(computer_names),
            health=random.randint(80, 120),
            attack_power=random.randint(15, 25)
        )

    def show_status(self):
        print("\n" + "=" * 30)
        print(f"СТАТУС:")
        print(f"{self.player}")
        print(f"{self.computer}")
        print("=" * 30 + "\n")

    def start(self):
        print("\n=== БИТВА ГЕРОЕВ ===")
        print(f"Ваш герой: {self.player.name}")
        print(f"Противник: {self.computer.name}")
        print("Да начнется битва!\n")

        round_num = 1

        while self.player.is_alive() and self.computer.is_alive():
            print(f"\n=== РАУНД {round_num} ===")

            # Ход игрока
            input("\nНажмите Enter для атаки...")
            damage = self.player.attack(self.computer)
            print(f"{self.player.name} атакует {self.computer.name} и наносит {damage} урона!")

            if not self.computer.is_alive():
                break

            self.show_status()
            time.sleep(1)

            # Ход компьютера
            print(f"\nХод {self.computer.name}...")
            time.sleep(1)
            damage = self.computer.attack(self.player)
            print(f"{self.computer.name} атакует {self.player.name} и наносит {damage} урона!")

            if not self.player.is_alive():
                break

            self.show_status()
            round_num += 1
            time.sleep(1)

        # Определение победителя
        print("\n=== БИТВА ЗАВЕРШЕНА ===")
        if self.player.is_alive():
            print(f"\nПОБЕДА! {self.player.name} одержал победу над {self.computer.name}!")
        else:
            print(f"\nПОРАЖЕНИЕ! {self.computer.name} победил {self.player.name}!")

        self.show_status()


# Запуск игры
if __name__ == "__main__":
    game = Game()
    game.start()