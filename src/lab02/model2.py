# model.py
# Класс Bus (автобус) для лабораторной работы №2.
# Импортирует функции валидации из отдельного модуля validation.py.

from validation2 import validate_route, validate_capacity, validate_passengers, validate_status, VALID_STATUSES

class Bus:
    # Атрибуты класса – общие для всех экземпляров.
    total_buses = 0                     # счётчик созданных автобусов
    VALID_STATUSES = VALID_STATUSES     # дублируем константу для удобства (можно обращаться через класс)

    def __init__(self, route, capacity, passengers=0, status='parked'):
        """
        Конструктор. Вызывается при создании нового автобуса.
        :param route: номер маршрута (непустая строка)
        :param capacity: вместимость (целое положительное число)
        :param passengers: начальное количество пассажиров (0 по умолчанию)
        :param status: состояние ('parked' или 'on_route')
        """
        # Валидация входных данных через импортированные функции
        validate_route(route)
        validate_capacity(capacity)
        validate_passengers(passengers, capacity)
        validate_status(status)

        # Защищённые атрибуты (с одним подчёркиванием) – не рекомендуется обращаться напрямую
        self._route = route
        self._capacity = capacity
        self._passengers = passengers
        self._status = status

        # Увеличиваем счётчик созданных автобусов (атрибут класса)
        Bus.total_buses += 1

    # ---------- Свойства (property) – контролируемый доступ к атрибутам ----------
    @property
    def route(self):
        """Геттер для номера маршрута (только чтение)."""
        return self._route

    @property
    def capacity(self):
        """Геттер для вместимости."""
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        """Сеттер для вместимости с проверкой (использует импортированную валидацию)."""
        validate_capacity(value)
        self._capacity = value

    @property
    def passengers(self):
        """Геттер для количества пассажиров."""
        return self._passengers

    @passengers.setter
    def passengers(self, value):
        """Сеттер для пассажиров (с проверкой)."""
        validate_passengers(value, self._capacity)
        self._passengers = value

    @property
    def status(self):
        """Геттер для состояния."""
        return self._status

    @status.setter
    def status(self, value):
        """Сеттер для состояния (с проверкой)."""
        validate_status(value)
        self._status = value

    # ---------- Бизнес-методы (основная логика) ----------
    def board(self, num):
        """
        Посадка пассажиров.
        Доступна только когда автобус на маршруте.
        """
        if self.status != 'on_route':
            raise ValueError("Посадка возможна только на маршруте")
        if num <= 0:
            raise ValueError("Число входящих должно быть положительным")
        if self.passengers + num > self.capacity:
            raise ValueError(f"Не хватает мест, свободно {self.capacity - self.passengers}")
        self._passengers += num

    def alight(self, num):
        """Высадка пассажиров (проверяет, что есть кого высаживать)."""
        if num <= 0:
            raise ValueError("Число выходящих должно быть положительным")
        if self.passengers < num:
            raise ValueError(f"В автобусе только {self.passengers} пассажиров")
        self._passengers -= num

    def start_route(self):
        """Выехать на маршрут (можно только из парка)."""
        if self.status != 'parked':
            raise ValueError("Автобус уже не в парке")
        self._status = 'on_route'

    def park(self):
        """Вернуться в парк (только с пустым автобусом)."""
        if self.status != 'on_route':
            raise ValueError("Автобус не на маршруте")
        if self.passengers != 0:
            raise ValueError("Нельзя парковаться с пассажирами")
        self._status = 'parked'

    # ---------- Магические методы ----------
    def __str__(self):
        """Человеко-читаемое представление (для print)."""
        return f"Автобус {self.route}: {self.passengers}/{self.capacity} пасс., статус: {self.status}"

    def __repr__(self):
        """Техническое представление (для отладки)."""
        return f"Bus('{self.route}', {self.capacity}, {self.passengers}, '{self.status}')"

    def __eq__(self, other):
        """Сравнение автобусов по номеру маршрута."""
        if not isinstance(other, Bus):
            return NotImplemented
        return self.route == other.route