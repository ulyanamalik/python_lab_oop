# base.py
"""Базовый класс Bus (автобус) для лабораторной работы №3."""

from validation3 import (
    validate_route, validate_capacity,
    validate_passengers, validate_status,
    VALID_STATUSES
)

class Bus:
    total_buses = 0
    VALID_STATUSES = VALID_STATUSES

    def __init__(self, route, capacity, passengers=0, status='parked'):
        # Валидация через импортированные функции
        validate_route(route)
        validate_capacity(capacity)
        validate_passengers(passengers, capacity)
        validate_status(status)

        self._route = route
        self._capacity = capacity
        self._passengers = passengers
        self._status = status
        Bus.total_buses += 1

    # ---------- Свойства ----------
    @property
    def route(self):
        return self._route

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        validate_capacity(value)
        self._capacity = value

    @property
    def passengers(self):
        return self._passengers

    @passengers.setter
    def passengers(self, value):
        validate_passengers(value, self._capacity)
        self._passengers = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        validate_status(value)
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

    # ---------- Полиморфные методы (будут переопределяться) ----------
    def get_bus_type(self):
        """Возвращает тип автобуса."""
        return "Обычный автобус"

    def calculate_price(self, distance_km):
        """Рассчитывает стоимость поездки (базовая: 20 руб/км)."""
        return distance_km * 20

    # ---------- Магические методы ----------
    def __str__(self):
        return f"Автобус {self.route}: {self.passengers}/{self.capacity} пасс., статус: {self.status}"

    def __repr__(self):
        return f"Bus('{self.route}', {self.capacity}, {self.passengers}, '{self.status}')"

    def __eq__(self, other):
        if not isinstance(other, Bus):
            return NotImplemented
        return self.route == other.route