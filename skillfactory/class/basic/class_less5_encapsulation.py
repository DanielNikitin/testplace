class Human:
    age = None

    def __init__(self, age=4):
        self.age = age

    # добавляем геттер - специальный метод для получения поля
    def get_age(self):
        return self.age

    # добавляем сеттер - специальный метод для установки нового значения
    def set_age(self, age):
        if age > 0 and isinstance(age,
                                  int):  # проверяем условия, что человеку должно быть больше 0 лет и его возраст - целое число
            self.age = age


h = Human()
h.set_age(15)
print(h.get_age())

# Здесь мы уже контролируем обращение к полям класса.
# Мы добавили специальные методы: геттеры и сеттеры.
#
# Геттеры — пишется так: get_<имя поля>.
# Геттер просто возвращает значение поля и не принимает никаких аргументов.
#
# Основная задача геттера — не давать изменять
# атрибут класса вне класса. Это значит,
# что при использовании обычной переменной age
# её можно будет изменить в основном коде