# models.py
"""Классы автобусов, реализующие интерфейсы Printable, Comparable, PriceCalculable."""

from abc import ABC
from interfaces4 import Printable, Comparable, PriceCalculable

# ---------- Базовый класс Bus ----------
class Bus(Printable, Comparable, PriceCalculable, ABC):
    """Базовый класс автобуса. Реализует все три интерфейса."""
    
    total_buses = 0
    VALID_STATUSES = ('parked', 'on_route')

    def __init__(self, route, capacity, passengers=0, status='parked'):
        self._validate_route(route)
        self._validate_capacity(capacity)
        self._validate_passengers(passengers, capacity)
        self._validate_status(status)

        self._route = route
        self._capacity = capacity
        self._passengers = passengers
        self._status = status
        Bus.total_buses += 1

    # ---------- Валидация ----------
    def _validate_route(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Номер маршрута должен быть непустой строкой")

    def _validate_capacity(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Вместимость должна быть положительным целым числом")

    def _validate_passengers(self, value, capacity=None):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Число пассажиров должно быть целым и ≥ 0")
        if capacity is not None and value > capacity:
            raise ValueError(f"Пассажиров не может быть больше вместимости ({capacity})")

    def _validate_status(self, value):
        if value not in Bus.VALID_STATUSES:
            raise ValueError(f"Статус должен быть одним из {Bus.VALID_STATUSES}")

    # ---------- Свойства ----------
    @property
    def route(self):
        return self._route

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._validate_capacity(value)
        self._capacity = value

    @property
    def passengers(self):
        return self._passengers

    @passengers.setter
    def passengers(self, value):
        self._validate_passengers(value, self._capacity)
        self._passengers = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._validate_status(value)
        self._status = value

    # ---------- Бизнес-методы ----------
    def board(self, num):
        if self.status != 'on_route':
            raise ValueError("Посадка возможна только на маршруте")
        if num <= 0:
            raise ValueError("Число входящих должно быть положительным")
        if self.passengers + num > self.capacity:
            raise ValueError(f"Не хватает мест, свободно {self.capacity - self.passengers}")
        self._passengers += num

    def alight(self, num):
        if num <= 0:
            raise ValueError("Число выходящих должно быть положительным")
        if self.passengers < num:
            raise ValueError(f"В автобусе только {self.passengers} пассажиров")
        self._passengers -= num

    def start_route(self):
        if self.status != 'parked':
            raise ValueError("Автобус уже не в парке")
        self._status = 'on_route'

    def park(self):
        if self.status != 'on_route':
            raise ValueError("Автобус не на маршруте")
        if self.passengers != 0:
            raise ValueError("Нельзя парковаться с пассажирами")
        self._status = 'parked'

    # ---------- Реализация интерфейса Printable ----------
    def to_string(self):
        """Возвращает строковое представление автобуса."""
        return f"Автобус {self.route}: {self.passengers}/{self.capacity} пасс., статус: {self.status}"

    # ---------- Реализация интерфейса Comparable ----------
    def compare_to(self, other):
        """
        Сравнивает автобусы по номеру маршрута.
        Возвращает отрицательное, 0 или положительное число.
        """
        if not isinstance(other, Bus):
            raise TypeError("Можно сравнивать только с объектами Bus")
        if self.route < other.route:
            return -1
        elif self.route == other.route:
            return 0
        else:
            return 1

    # ---------- Реализация интерфейса PriceCalculable ----------
    def calculate_price(self, distance_km):
        """Базовая стоимость: 20 руб/км."""
        return distance_km * 20

    # ---------- Магические методы ----------
    def __str__(self):
        return self.to_string()

    def __repr__(self):
        return f"Bus('{self.route}', {self.capacity}, {self.passengers}, '{self.status}')"

    def __eq__(self, other):
        if not isinstance(other, Bus):
            return NotImplemented
        return self.route == other.route


# ---------- Дочерний класс CityBus ----------
class CityBus(Bus):
    """Городской автобус. Переопределяет методы интерфейсов."""

    def __init__(self, route, capacity, passengers, status, route_type, has_air_conditioning):
        super().__init__(route, capacity, passengers, status)
        self._route_type = route_type
        self._has_air_conditioning = has_air_conditioning

    def get_route_type(self):
        return self._route_type

    def has_ac(self):
        return self._has_air_conditioning

    # ---------- Переопределение методов интерфейсов ----------
    def to_string(self):
        ac_str = "с кондиционером" if self._has_air_conditioning else "без кондиционера"
        return (f"Городской автобус {self.route}: {self.passengers}/{self.capacity} пасс., "
                f"статус: {self.status}, тип маршрута: {self._route_type}, {ac_str}")

    def calculate_price(self, distance_km):
        """Городской автобус дешевле: 15 руб/км."""
        return distance_km * 15

    def __str__(self):
        return self.to_string()


# ---------- Дочерний класс TouristBus ----------
class TouristBus(Bus):
    """Туристический автобус. Переопределяет методы интерфейсов."""

    def __init__(self, route, capacity, passengers, status, has_toilet, comfort_level):
        super().__init__(route, capacity, passengers, status)
        self._has_toilet = has_toilet
        self._comfort_level = comfort_level

    def has_toilet(self):
        return self._has_toilet

    def get_comfort_level(self):
        return self._comfort_level

    # ---------- Переопределение методов интерфейсов ----------
    def to_string(self):
        toilet_str = "с туалетом" if self._has_toilet else "без туалета"
        return (f"Туристический автобус {self.route}: {self.passengers}/{self.capacity} пасс., "
                f"статус: {self.status}, {toilet_str}, комфорт: {self._comfort_level}/5")

    def calculate_price(self, distance_km):
        """Туристический автобус дороже: 35 руб/км."""
        return distance_km * 35

    def __str__(self):
        return self.to_string()