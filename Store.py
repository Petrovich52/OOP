# Создаем класс Store
class Store:
    # Конструктор класса, который инициализирует название, адрес и пустой словарь для товаров
    def __init__(self, name, address):
        self.name = name  # Название магазина
        self.address = address  # Адрес магазина
        self.items = {}  # Словарь для хранения товаров и их цен

    # Метод для добавления товара в ассортимент
    def add_item(self, item_name, price):
        self.items[item_name] = price  # Добавляем товар и его цену в словарь

    # Метод для удаления товара из ассортимента
    def remove_item(self, item_name):
        if item_name in self.items:  # Проверяем, существует ли товар
            del self.items[item_name]  # Удаляем товар из словаря
        else:
            print(f"Товар {item_name} отсутствует в ассортименте.")

    # Метод для получения цены товара по его названию
    def get_price(self, item_name):
        return self.items.get(item_name, None)  # Возвращаем цену товара или None, если товар отсутствует

    # Метод для обновления цены товара
    def update_price(self, item_name, new_price):
        if item_name in self.items:  # Проверяем, существует ли товар
            self.items[item_name] = new_price  # Обновляем цену товара
        else:
            print(f"Товар {item_name} отсутствует в ассортименте {self.name}.")

# Создаем несколько объектов класса Store
store1 = Store("Магазин фруктов", "ул. Ленина, 10")
store2 = Store("Магазин электроники", "пр. Мира, 25")
store3 = Store("Магазин одежды", "ул. Пушкина, 15")

# Добавляем товары в каждый магазин
store1.add_item("яблоки", 0.5)
store1.add_item("бананы", 0.75)

store2.add_item("ноутбук", 50000)
store2.add_item("смартфон", 30000)

store3.add_item("футболка", 1000)
store3.add_item("джинсы", 2500)

# Тестируем методы на примере store1 и store2

# Добавляем новый товар в store1
store1.add_item("апельсины", 0.8)
print(f"Товары в {store1.name}: {store1.items}")  # Выводим текущий ассортимент

# Обновляем цену товара в store1
store1.update_price("яблоки", 0.6)
print(f"Обновленная цена яблок: {store1.get_price('яблоки')}")  # Проверяем обновленную цену

# Удаляем товар из store1
store1.remove_item("бананы")
print(f"Товары в {store1.name} после удаления бананов: {store1.items}")  # Проверяем ассортимент после удаления

# Пытаемся получить цену несуществующего товара в store2
price = store2.get_price("планшет")
if price is None:
    print("Товар планшет отсутствует в ассортименте в Магазине электроники.")  # Ожидаемо, что вернется None

# Обновляем цену несуществующего товара в store2
store2.update_price("планшет", 20000)  # Ожидаемо, что выведется сообщение об отсутствии товара