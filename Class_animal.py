# 1. Базовый класс Animal
class Animal:
    def __init__(self, name, age):
        self.name = name  # Инициализируем атрибут name (имя животного)
        self.age = age    # Инициализируем атрибут age (возраст животного)

    def make_sound(self):
        raise NotImplementedError("Subclasses must implement this method")  # Абстрактный метод, должен быть переопределен в подклассах

    def eat(self):
        print(f"{self.name} is eating.")  # Метод для приема пищи, выводит сообщение


# 2. Подклассы Bird, Mammal, Reptile
class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)  # Вызов конструктора родительского класса Animal
        self.wingspan = wingspan    # Уникальный атрибут для птиц (размах крыльев)

    def make_sound(self):
        print(f"{self.name} says Chirp!")  # Переопределение метода make_sound для птиц


class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)  # Вызов конструктора родительского класса Animal
        self.fur_color = fur_color   # Уникальный атрибут для млекопитающих (цвет шерсти)

    def make_sound(self):
        print(f"{self.name} says Growl!")  # Переопределение метода make_sound для млекопитающих


class Reptile(Animal):
    def __init__(self, name, age, scale_type):
        super().__init__(name, age)  # Вызов конструктора родительского класса Animal
        self.scale_type = scale_type  # Уникальный атрибут для рептилий (тип чешуи)

    def make_sound(self):
        print(f"{self.name} says Hiss!")  # Переопределение метода make_sound для рептилий


# 3. Функция для демонстрации полиморфизма
def animal_sound(animals):
    for animal in animals:  # Итерируемся по списку животных
        animal.make_sound()  # Вызываем метод make_sound для каждого животного


# 4. Класс Zoo с композицией
class Zoo:
    def __init__(self):
        self.animals = []  # Список для хранения животных
        self.staff = []    # Список для хранения сотрудников

    def add_animal(self, animal):
        self.animals.append(animal)  # Добавляем животное в список

    def add_staff(self, staff_member):
        self.staff.append(staff_member)  # Добавляем сотрудника в список


# 5. Классы для сотрудников
class Staff:
    def __init__(self, name):
        self.name = name  # Инициализируем атрибут name (имя сотрудника)


class ZooKeeper(Staff):
    def feed_animal(self, animal):
        print(f"{self.name} is feeding {animal.name}.")  # Метод для кормления животного


class Veterinarian(Staff):
    def heal_animal(self, animal):
        print(f"{self.name} is healing {animal.name}.")  # Метод для лечения животного


# 6. Функции для сохранения и загрузки состояния зоопарка (без json)
def save_zoo(zoo, filename):
    with open(filename, "w") as file:
        # Сохраняем информацию о животных
        for animal in zoo.animals:
            file.write(f"Animal,{type(animal).__name__},{animal.name},{animal.age}\n")
        # Сохраняем информацию о сотрудниках
        for staff in zoo.staff:
            file.write(f"Staff,{type(staff).__name__},{staff.name}\n")


def load_zoo(filename):
    zoo = Zoo()  # Создаем новый объект Zoo
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")  # Разделяем строку по запятым
            if parts[0] == "Animal":
                animal_type, name, age = parts[1], parts[2], int(parts[3])
                if animal_type == "Bird":
                    zoo.add_animal(Bird(name, age, 2.0))  # Создаем объект Bird
                elif animal_type == "Mammal":
                    zoo.add_animal(Mammal(name, age, "Unknown"))  # Создаем объект Mammal
                elif animal_type == "Reptile":
                    zoo.add_animal(Reptile(name, age, "Unknown"))  # Создаем объект Reptile
            elif parts[0] == "Staff":
                staff_type, name = parts[1], parts[2]
                if staff_type == "ZooKeeper":
                    zoo.add_staff(ZooKeeper(name))  # Создаем объект ZooKeeper
                elif staff_type == "Veterinarian":
                    zoo.add_staff(Veterinarian(name))  # Создаем объект Veterinarian
    return zoo  # Возвращаем восстановленный зоопарк


# Пример использования
if __name__ == "__main__":
    # Создаем зоопарк
    zoo = Zoo()

    # Добавляем животных
    zoo.add_animal(Bird("Eagle", 5, 2.0))  # Добавляем птицу
    zoo.add_animal(Mammal("Lion", 10, "Golden"))  # Добавляем млекопитающее
    zoo.add_animal(Reptile("Snake", 3, "Smooth"))  # Добавляем рептилию

    # Добавляем сотрудников
    zoo.add_staff(ZooKeeper("John"))  # Добавляем смотрителя
    zoo.add_staff(Veterinarian("Alice"))  # Добавляем ветеринара

    # Сохраняем зоопарк в файл
    save_zoo(zoo, "zoo_state.txt")

    # Загружаем зоопарк из файла
    loaded_zoo = load_zoo("zoo_state.txt")

    # Демонстрируем полиморфизм
    print("Animal sounds:")
    animal_sound(loaded_zoo.animals)  # Вызываем метод make_sound для каждого животного

    # Демонстрируем методы сотрудников
    print("\nStaff actions:")
    for staff in loaded_zoo.staff:
        if isinstance(staff, ZooKeeper):
            staff.feed_animal(loaded_zoo.animals[0])  # Смотритель кормит животное
        elif isinstance(staff, Veterinarian):
            staff.heal_animal(loaded_zoo.animals[1])  # Ветеринар лечит животное