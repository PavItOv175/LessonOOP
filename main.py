#Создайте класс машина, и несколько экземпляров данного класса с разными атрибутами. Код разметите в гит репозитории и ссылочку мне на него.
class Car:
    emp_count = 0

    def __init__(self, my_type, wheel, color, doors):
        self.my_type = my_type
        self.wheel = wheel
        self.color = color
        self.doors = doors
        Car.emp_count += 1

    def display_count(self):
        print('Всего машин: %d' % Car.empCount)

    def display_employee(self):
        print('Тип кузова: {}. Кол-во колес: {}. Цвет машины: {}. Кол-во дверей: {}'.format(self.my_type, self.wheel, self.color, self.doors))

Peugeot = Car('Седан', 4, 'Зелёный', 3)
Peugeot.display_employee()

Lexus = Car('Кросссовер', 4, 'Чёрный', 5)
Lexus.display_employee()

BMW = Car('Универсал', 4, 'Серебристый металлик', 5)
BMW.display_employee()

print(Car.emp_count)
