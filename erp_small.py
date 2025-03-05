# Напиши код на python для описания системы управления учетными записями пользователей
# для небольшой компании. Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа
# и могут добавлять или удалять пользователя из системы.
# Требования:
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе:
# ID, имя и уровень доступа ('user' для обычных сотрудников).
# 2.Класс `Admin`: Этот класс должен наследоваться от класса `User`.
# Добавь дополнительный атрибут уровня доступа, специфичный для администраторов ('admin').
# Класс должен также содержать методы `add_user` и `remove_user`, которые позволяют добавлять и удалять
# пользователей из списка (представь, что это просто список экземпляров `User`).

# Определяем базовый класс User для представления обычного пользователя
class User:
    # Конструктор класса, который инициализирует атрибуты пользователя
    def __init__(self, user_id, name):
        self._user_id = user_id  # Защищенный атрибут: двухфакторный ID (уровень доступа-уникальный номер)
        self._name = name        # Защищенный атрибут: имя пользователя
        self._access_level = self._parse_access_level(user_id)  # Уровень доступа извлекается из ID

    # Метод для извлечения уровня доступа из двухфакторного ID
    def _parse_access_level(self, user_id):
        return user_id.split('-')[0]  # Разделяем ID по дефису и берем первую часть

    # Геттер для получения полного ID пользователя
    def get_user_id(self):
        return self._user_id

    # Геттер для получения уникального номера сотрудника
    def get_employee_number(self):
        return self._user_id.split('-')[1]  # Разделяем ID по дефису и берем вторую часть

    # Геттер для получения имени пользователя
    def get_name(self):
        return self._name

    # Геттер для получения уровня доступа пользователя
    def get_access_level(self):
        return self._access_level

    # Сеттер для изменения имени пользователя
    def set_name(self, name):
        self._name = name

    # Сеттер для изменения уровня доступа пользователя
    def set_access_level(self, access_level):
        if access_level in ['user', 'admin']:  # Проверяем, что уровень доступа допустим
            # Формируем новый двухфакторный ID с новым уровнем доступа и старым уникальным номером
            new_user_id = f"{access_level}-{self.get_employee_number()}"
            self._user_id = new_user_id  # Обновляем ID
            self._access_level = access_level  # Обновляем уровень доступа
            print(f"Access level changed to {access_level}. New ID: {new_user_id}")
        else:
            print("Invalid access level. Allowed values are 'user' and 'admin'.")

    # Метод для строкового представления объекта (удобно для вывода информации)
    def __str__(self):
        return f"User(ID: {self._user_id}, Name: {self._name}, Access Level: {self._access_level})"


# Определяем класс Admin, который наследует от класса User
class Admin(User):
    # Конструктор класса, который инициализирует атрибуты администратора
    def __init__(self, user_id, name):
        super().__init__(user_id, name)  # Вызываем конструктор родительского класса
        self._access_level = 'admin'  # Переопределяем уровень доступа на 'admin'

    # Метод для добавления пользователя в список
    def add_user(self, user_list, user):
        if isinstance(user, User):  # Проверяем, что переданный объект является экземпляром класса User
            user_list.append(user)  # Добавляем пользователя в список
            print(f"User {user.get_name()} added successfully.")  # Выводим сообщение об успешном добавлении
        else:
            print("Invalid user object.")  # Выводим сообщение об ошибке, если объект не является пользователем

    # Метод для удаления пользователя из списка по его ID
    def remove_user(self, user_list, user_id):
        for user in user_list:  # Проходим по всем пользователям в списке
            if user.get_user_id() == user_id:  # Проверяем, совпадает ли ID
                user_list.remove(user)  # Удаляем пользователя из списка
                print(f"User with ID {user_id} removed successfully.")  # Выводим сообщение об успешном удалении
                return
        print(f"User with ID {user_id} not found.")  # Выводим сообщение, если пользователь не найден

    # Метод для строкового представления объекта (удобно для вывода информации)
    def __str__(self):
        return f"Admin(ID: {self._user_id}, Name: {self._name}, Access Level: {self._access_level})"


# Пример использования классов
if __name__ == "__main__":
    # Создаем пустой список для хранения пользователей
    users = []

    # Создаем обычного пользователя с двухфакторным ID "user-101" и именем "John Doe"
    user1 = User("user-101", "John Doe")
    print(user1)  # Выводим информацию о пользователе

    # Создаем администратора с двухфакторным ID "admin-001" и именем "Jane Smith"
    admin = Admin("admin-001", "Jane Smith")
    print(admin)  # Выводим информацию об администраторе

    # Администратор добавляет пользователя user1 в список users
    admin.add_user(users, user1)

    # Пытаемся изменить уровень доступа пользователя user1 на 'admin'
    user1.set_access_level('admin')  # Уровень доступа изменен, ID обновлен
    print(user1)  # Выводим обновленную информацию о пользователе

    # Пытаемся установить недопустимый уровень доступа
    user1.set_access_level('manager')  # Выведет сообщение об ошибке

    # Администратор удаляет пользователя с ID "admin-101" из списка users
    admin.remove_user(users, "admin-101")