# models.py
"""Классы предметной области: Bus, CityBus, TouristBus."""

from typing import Tuple


class Bus:
    """Базовый класс автобуса."""

    total_buses: int = 0
    VALID_STATUSES: Tuple[str, str] = ('parked', 'on_route')

    def __init__(self, route: str, capacity: int, passengers: int = 0, status: str = 'parked') -> None:
        """
        Конструктор автобуса.
        
        Args:
            route: Номер маршрута
            capacity: Вместимость автобуса
            passengers: Количество пассажиров (по умолчанию 0)
            status: Статус автобуса (parked/on_route)
        
        Raises:
            ValueError: Если данные некорректны
        """
        # Валидация номера маршрута
        if not route or not route.strip():
            raise ValueError("Номер маршрута не может быть пустым")
        
        # Валидация вместимости
        if capacity <= 0:
            raise ValueError("Вместимость должна быть положительным числом")
        
        # Валидация количества пассажиров
        if passengers < 0:
            raise ValueError("Количество пассажиров не может быть отрицательным")
        if passengers > capacity:
            raise ValueError(f"Пассажиров ({passengers}) не может быть больше вместимости ({capacity})")
        
        # Валидация статуса
        if status not in Bus.VALID_STATUSES:
            raise ValueError(f"Статус должен быть 'parked' или 'on_route'")

        self._route: str = route
        self._capacity: int = capacity
        self._passengers: int = passengers
        self._status: str = status
        Bus.total_buses += 1

    @property
    def route(self) -> str:
        """Номер маршрута (только чтение)."""
        return self._route

    @property
    def capacity(self) -> int:
        """Вместимость автобуса."""
        return self._capacity

    @capacity.setter
    def capacity(self, value: int) -> None:
        """Устанавливает вместимость с проверкой."""
        if value <= 0:
            raise ValueError("Вместимость должна быть положительным числом")
        if self._passengers > value:
            raise ValueError(f"Нельзя уменьшить вместимость: в автобусе {self._passengers} пассажиров")
        self._capacity = value

    @property
    def passengers(self) -> int:
        """Количество пассажиров."""
        return self._passengers

    @passengers.setter
    def passengers(self, value: int) -> None:
        """Устанавливает количество пассажиров с проверкой."""
        if value < 0:
            raise ValueError("Количество пассажиров не может быть отрицательным")
        if value > self._capacity:
            raise ValueError(f"Пассажиров ({value}) не может быть больше вместимости ({self._capacity})")
        self._passengers = value

    @property
    def status(self) -> str:
        """Статус автобуса."""
        return self._status

    @status.setter
    def status(self, value: str) -> None:
        """Устанавливает статус с проверкой."""
        if value not in Bus.VALID_STATUSES:
            raise ValueError(f"Статус должен быть 'parked' или 'on_route'")
        self._status = value

    # ---------- Бизнес-методы ----------
    def board(self, num: int) -> None:
        """
        Посадка пассажиров.
        
        Args:
            num: Количество пассажиров для посадки
            
        Raises:
            ValueError: Если посадка невозможна
        """
        if self.status != 'on_route':
            raise ValueError("Посадка возможна только на маршруте")
        if num <= 0:
            raise ValueError("Число входящих должно быть положительным")
        if self.passengers + num > self.capacity:
            raise ValueError(f"Не хватает мест, свободно {self.capacity - self.passengers}")
        self._passengers += num

    def alight(self, num: int) -> None:
        """
        Высадка пассажиров.
        
        Args:
            num: Количество пассажиров для высадки
            
        Raises:
            ValueError: Если высадка невозможна
        """
        if num <= 0:
            raise ValueError("Число выходящих должно быть положительным")
        if self.passengers < num:
            raise ValueError(f"В автобусе только {self.passengers} пассажиров")
        self._passengers -= num

    def start_route(self) -> None:
        """Выезд на маршрут."""
        if self.status != 'parked':
            raise ValueError("Автобус уже не в парке")
        self._status = 'on_route'

    def park(self) -> None:
        """Возврат в парк."""
        if self.status != 'on_route':
            raise ValueError("Автобус не на маршруте")
        if self.passengers != 0:
            raise ValueError("Нельзя парковаться с пассажирами")
        self._status = 'parked'

    # ---------- Методы для протоколов и отображения ----------
    def display(self) -> str:
        """Возвращает строковое представление автобуса."""
        return f"Автобус {self.route}: {self.passengers}/{self.capacity} пасс., статус: {self.status}"

    def score(self) -> float:
        """Возвращает оценку/рейтинг автобуса."""
        return (self.passengers / self.capacity) * 100 if self.capacity > 0 else 0

    # ---------- Методы для JSON ----------
    def to_dict(self) -> dict:
        """Преобразует объект в словарь для JSON."""
        return {
            'type': 'bus',
            'route': self._route,
            'capacity': self._capacity,
            'passengers': self._passengers,
            'status': self._status
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Bus':
        """Создаёт объект из словаря."""
        return cls(data['route'], data['capacity'], data['passengers'], data['status'])

    # ---------- Магические методы ----------
    def __str__(self) -> str:
        return self.display()

    def __repr__(self) -> str:
        return f"Bus('{self.route}', {self.capacity}, {self.passengers}, '{self.status}')"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Bus):
            return NotImplemented
        return self.route == other.route


class CityBus(Bus):
    """Городской автобус."""

    def __init__(self, route: str, capacity: int, passengers: int, status: str,
                 route_type: str, has_air_conditioning: bool) -> None:
        """
        Конструктор городского автобуса.
        
        Args:
            route: Номер маршрута
            capacity: Вместимость
            passengers: Количество пассажиров
            status: Статус
            route_type: Тип маршрута (городской/пригородный)
            has_air_conditioning: Наличие кондиционера
        """
        super().__init__(route, capacity, passengers, status)
        
        # Дополнительная валидация
        if not route_type or not route_type.strip():
            raise ValueError("Тип маршрута не может быть пустым")
        
        self._route_type: str = route_type
        self._has_air_conditioning: bool = has_air_conditioning

    def get_route_type(self) -> str:
        """Возвращает тип маршрута."""
        return self._route_type

    def has_ac(self) -> bool:
        """Возвращает наличие кондиционера."""
        return self._has_air_conditioning

    def display(self) -> str:
        """Возвращает строковое представление городского автобуса."""
        ac_str = "с кондиционером" if self._has_air_conditioning else "без кондиционера"
        return (f"Городской автобус {self.route}: {self.passengers}/{self.capacity} пасс., "
                f"статус: {self.status}, тип: {self._route_type}, {ac_str}")

    def to_dict(self) -> dict:
        """Преобразует объект в словарь для JSON."""
        data = super().to_dict()
        data['type'] = 'city'
        data['route_type'] = self._route_type
        data['has_air_conditioning'] = self._has_air_conditioning
        return data

    @classmethod
    def from_dict(cls, data: dict) -> 'CityBus':
        """Создаёт объект из словаря."""
        return cls(data['route'], data['capacity'], data['passengers'], data['status'],
                   data['route_type'], data['has_air_conditioning'])

    def __str__(self) -> str:
        return self.display()


class TouristBus(Bus):
    """Туристический автобус."""

    def __init__(self, route: str, capacity: int, passengers: int, status: str,
                 has_toilet: bool, comfort_level: int) -> None:
        """
        Конструктор туристического автобуса.
        
        Args:
            route: Номер маршрута
            capacity: Вместимость
            passengers: Количество пассажиров
            status: Статус
            has_toilet: Наличие туалета
            comfort_level: Уровень комфорта (1-5)
        """
        super().__init__(route, capacity, passengers, status)
        
        # Дополнительная валидация
        if comfort_level < 1 or comfort_level > 5:
            raise ValueError("Уровень комфорта должен быть от 1 до 5")
        
        self._has_toilet: bool = has_toilet
        self._comfort_level: int = comfort_level

    def has_toilet(self) -> bool:
        """Возвращает наличие туалета."""
        return self._has_toilet

    def get_comfort_level(self) -> int:
        """Возвращает уровень комфорта."""
        return self._comfort_level

    def display(self) -> str:
        """Возвращает строковое представление туристического автобуса."""
        toilet_str = "с туалетом" if self._has_toilet else "без туалета"
        return (f"Туристический автобус {self.route}: {self.passengers}/{self.capacity} пасс., "
                f"статус: {self.status}, {toilet_str}, комфорт: {self._comfort_level}/5")

    def to_dict(self) -> dict:
        """Преобразует объект в словарь для JSON."""
        data = super().to_dict()
        data['type'] = 'tourist'
        data['has_toilet'] = self._has_toilet
        data['comfort_level'] = self._comfort_level
        return data

    @classmethod
    def from_dict(cls, data: dict) -> 'TouristBus':
        """Создаёт объект из словаря."""
        return cls(data['route'], data['capacity'], data['passengers'], data['status'],
                   data['has_toilet'], data['comfort_level'])

    def __str__(self) -> str:
        return self.display()