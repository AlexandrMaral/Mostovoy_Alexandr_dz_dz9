# Задача 1

from time import sleep


class TrafficLight:
    __color = "Черный"

    def running(self):
        while True:
            print("TrafficLight is red now")
            sleep(7)
            print("TrafficLight is yellow now")
            sleep(2)
            print("TrafficLight is green now")
            sleep(7)
            print("TrafficLight is yellow now")
            sleep(2)


TrafficLight = TrafficLight()
TrafficLight.running()

# Задача 2


class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_full_profit(self, weight=25, thickness=5):
        return f"{self._length} м * {self._width} м * {weight} кг * {thickness} см =" \
               f"{(self._length * self._width * weight * thickness) / 1000} т"


road_1 = Road(5000, 20)
print(road_1.get_full_profit())

# Задача 3


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = {"profit": wage, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_full_profit(self):
        return f"{sum(self._income.values())}"


meneger = Position("Dorian", "Grey", "CEO", 500000, 125000)
print(meneger.get_full_name())
print(meneger.position)
print(meneger.get_full_profit())

# Задача 4


class Car:
    """" Автомобиль """

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'Новая машина: {self.name} (цвет {self.color}) машина полицейская - {self.is_police}')

    def go(self):
        print(f'{self.name}: Машина поехала.')

    def stop(self):
        print(f'{self.name}: Машина остановилась.')

    def turn(self, direction):
        print(f'{self.name}: Машина повернула {"налево" if direction == 0 else "направо"}.')

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}.'


class TownCar(Car):
    """"Городской автомобиль"""

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 60 else f"{self.name}: Скорость автомобиля {self.speed}"


class WorkCar(Car):
    """"Грузовой автомобиль"""

    def show_speed(self):
        return f'{self.name}: Скорость автомобиля: {self.speed}. Превышение скорости!' \
            if self.speed > 40 else f"{self.name}: Скорость автомобиля {self.speed}"


class PoliceCar(Car):
    """"Полицейский автомобиль"""

    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


police_car = PoliceCar('"Полицайка"', 'белый', 80)
police_car.go()
print(police_car.show_speed())
police_car.turn(0)
police_car.stop()
print()

work_car = WorkCar('"Грузовик"', 'хаки', 40)
work_car.go()
work_car.turn(1)
print(work_car.show_speed())
work_car.turn(0)
work_car.stop()
print()

town_car = TownCar('"Мелкая"', 'желтый', 50)
town_car.go()
town_car.turn(1)
town_car.turn(8)
print(town_car.show_speed())
town_car.stop()

print(f'\nМашина {town_car.name} (цвет {town_car.color})')
print(f'Машина {police_car.name} (цвет {police_car.color})')


# Задача 5


class Stationery:
    def __init__(self, title="Something that can draw"):
        self.title = title

    def draw(self):
        print(f"Just start drawing! {self.title}")

class Pen(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} pen!")


class Pencil(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} pencil!")


class Marker(Stationery):
    def draw(self):
        print(f"Start drawing with {self.title} marker!")


stat = Stationery()
stat.draw()
pen = Pen("Parker")
pen.draw()
pencil = Pencil("Faber-Castell")
pencil.draw()
marker = Marker("COPIC")
marker.draw()
