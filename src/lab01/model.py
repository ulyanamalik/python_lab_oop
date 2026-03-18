# model.py — класс Bus (автобус) с инкапсуляцией, свойствами и бизнес-методами

from validation import (
    validate_route, validate_capacity,
    validate_passengers, validate_status,
    VALID_STATUSES
)

class Bus:
    # Атрибуты класса
    total_buses = 0                     # счётчик созданных автобусов
    VALID_STATUSES = VALID_STATUSES     # для справки внутри класса

    def __init__(self, route, capacity, passengers=0, status='parked'):
        """Конструктор: инициализация с проверкой данных."""
        validate_route(route)
        validate_capacity(capacity)
        validate_passengers(passengers, capacity)
        validate_status(status)

        self._route = route
        self._capacity = capacity
        self._passengers = passengers
        self._status = status
        Bus.total_buses += 1

    # Свойства (геттеры/сеттеры)
    @property
    def route(self):
        """Геттер номера маршрута (только чтение)."""
        return self._route

    @property
    def capacity(self):
        """Геттер вместимости."""
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        """Сеттер вместимости с валидацией."""
        validate_capacity(value)
        self._capacity = value

    @property
    def passengers(self):
        """Геттер количества пассажиров."""
        return self._passengers

    @passengers.setter
    def passengers(self, value):
        """Сеттер пассажиров (прямое изменение)."""
        validate_passengers(value, self._capacity)
        self._passengers = value

    @property
    def status(self):
        """Геттер состояния."""
        return self._status

    @status.setter
    def status(self, value):
        """Сеттер состояния с проверкой."""
        validate_status(value)
        self._status = value

    # Бизнес-методы
    def board(self, num):
        """Посадка пассажиров (только на маршруте)."""
        if self.status != 'on_route':
            raise ValueError("Посадка возможна только на маршруте")
        if num <= 0:
            raise ValueError("Число входящих должно быть положительным")
        if self.passengers + num > self.capacity:
            raise ValueError(f"Не хватает мест, свободно {self.capacity - self.passengers}")
        self._passengers += num

    def alight(self, num):
        """Высадка пассажиров."""
        if num <= 0:
            raise ValueError("Число выходящих должно быть положительным")
        if self.passengers < num:
            raise ValueError(f"В автобусе только {self.passengers} пассажиров")
        self._passengers -= num

    def start_route(self):
        """Перевод из парка на маршрут."""
        if self.status != 'parked':
            raise ValueError("Автобус уже не в парке")
        self._status = 'on_route'

    def park(self):
        """Возврат в парк (без пассажиров)."""
        if self.status != 'on_route':
            raise ValueError("Автобус не на маршруте")
        if self.passengers != 0:
            raise ValueError("Нельзя парковаться с пассажирами")
        self._status = 'parked'

    # Магические методы
    def __str__(self):
        """Пользовательское строковое представление."""
        return f"Автобус {self.route}: {self.passengers}/{self.capacity} пасс., статус: {self.status}"

    def __repr__(self):
        """Техническое представление для отладки."""
        return f"Bus('{self.route}', {self.capacity}, {self.passengers}, '{self.status}')"

    def __eq__(self, other):
        """Сравнение автобусов по номеру маршрута."""
        if not isinstance(other, Bus):
            return NotImplemented
        return self.route == other.route