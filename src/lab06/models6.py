

from typing import Tuple


class Bus:
    """Базовый класс автобуса с аннотациями типов."""

    total_buses: int = 0
    VALID_STATUSES: Tuple[str, str] = ('parked', 'on_route')

    def __init__(self, route: str, capacity: int, passengers: int = 0, status: str = 'parked') -> None:
        self._route: str = route
        self._capacity: int = capacity
        self._passengers: int = passengers
        self._status: str = status
        Bus.total_buses += 1

    # ---------- Свойства ----------
    @property
    def route(self) -> str:
        return self._route

    @property
    def capacity(self) -> int:
        return self._capacity

    @capacity.setter
    def capacity(self, value: int) -> None:
        self._capacity = value

    @property
    def passengers(self) -> int:
        return self._passengers

    @passengers.setter
    def passengers(self, value: int) -> None:
        self._passengers = value

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value: str) -> None:
        self._status = value

    # ---------- Бизнес-методы ----------
    def board(self, num: int) -> None:
        if self.status != 'on_route':
            raise ValueError("Посадка возможна только на маршруте")
        if num <= 0:
            raise ValueError("Число входящих должно быть положительным")
        if self.passengers + num > self.capacity:
            raise ValueError(f"Не хватает мест, свободно {self.capacity - self.passengers}")
        self._passengers += num

    def alight(self, num: int) -> None:
        if num <= 0:
            raise ValueError("Число выходящих должно быть положительным")
        if self.passengers < num:
            raise ValueError(f"В автобусе только {self.passengers} пассажиров")
        self._passengers -= num

    def start_route(self) -> None:
        if self.status != 'parked':
            raise ValueError("Автобус уже не в парке")
        self._status = 'on_route'

    def park(self) -> None:
        if self.status != 'on_route':
            raise ValueError("Автобус не на маршруте")
        if self.passengers != 0:
            raise ValueError("Нельзя парковаться с пассажирами")
        self._status = 'parked'

    # Методы для протоколов
    def display(self) -> str:
        """Возвращает строковое представление (для Protocol Displayable)."""
        return f"Автобус {self.route}: {self.passengers}/{self.capacity} пасс., статус: {self.status}"

    def score(self) -> float:
        """Возвращает оценку/рейтинг (для Protocol Scorable)."""
        return (self.passengers / self.capacity) * 100 if self.capacity > 0 else 0

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
        super().__init__(route, capacity, passengers, status)
        self._route_type: str = route_type
        self._has_air_conditioning: bool = has_air_conditioning

    def get_route_type(self) -> str:
        return self._route_type

    def has_ac(self) -> bool:
        return self._has_air_conditioning

    def display(self) -> str:
        ac_str = "с кондиционером" if self._has_air_conditioning else "без кондиционера"
        return (f"Городской автобус {self.route}: {self.passengers}/{self.capacity} пасс., "
                f"статус: {self.status}, тип: {self._route_type}, {ac_str}")

    def __str__(self) -> str:
        return self.display()


class TouristBus(Bus):
    """Туристический автобус."""

    def __init__(self, route: str, capacity: int, passengers: int, status: str,
                 has_toilet: bool, comfort_level: int) -> None:
        super().__init__(route, capacity, passengers, status)
        self._has_toilet: bool = has_toilet
        self._comfort_level: int = comfort_level

    def has_toilet(self) -> bool:
        return self._has_toilet

    def get_comfort_level(self) -> int:
        return self._comfort_level

    def display(self) -> str:
        toilet_str = "с туалетом" if self._has_toilet else "без туалета"
        return (f"Туристический автобус {self.route}: {self.passengers}/{self.capacity} пасс., "
                f"статус: {self.status}, {toilet_str}, комфорт: {self._comfort_level}/5")

    def __str__(self) -> str:
        return self.display()