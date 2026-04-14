# models.py
"""Дочерние классы автобусов: CityBus и TouristBus."""

from base3 import Bus
from validation3 import validate_route_type, validate_comfort_level

class CityBus(Bus):
    """Городской автобус (доп. атрибуты: тип маршрута, кондиционер)."""

    def __init__(self, route, capacity, passengers, status, route_type, has_air_conditioning):
        # Вызов конструктора базового класса через super()
        super().__init__(route, capacity, passengers, status)

        # Валидация новых атрибутов
        validate_route_type(route_type)

        # Новые атрибуты
        self._route_type = route_type
        self._has_air_conditioning = has_air_conditioning   # bool

    # ---------- Новые методы ----------
    def get_route_type(self):
        return self._route_type

    def has_ac(self):
        return self._has_air_conditioning

    # ---------- Переопределение методов базового класса (полиморфизм) ----------
    def get_bus_type(self):
        return "Городской автобус"

    def calculate_price(self, distance_km):
        """Городской автобус дешевле: 15 руб/км."""
        return distance_km * 15

    # ---------- Переопределение __str__ ----------
    def __str__(self):
        ac_str = "с кондиционером" if self._has_air_conditioning else "без кондиционера"
        return (f"Городской автобус {self.route}: {self.passengers}/{self.capacity} пасс., "
                f"статус: {self.status}, тип маршрута: {self._route_type}, {ac_str}")

    def __repr__(self):
        return (f"CityBus('{self.route}', {self.capacity}, {self.passengers}, '{self.status}', "
                f"'{self._route_type}', {self._has_air_conditioning})")


class TouristBus(Bus):
    """Туристический автобус (доп. атрибуты: туалет, уровень комфорта)."""

    def __init__(self, route, capacity, passengers, status, has_toilet, comfort_level):
        super().__init__(route, capacity, passengers, status)

        # Валидация новых атрибутов
        validate_comfort_level(comfort_level)

        self._has_toilet = has_toilet          # bool
        self._comfort_level = comfort_level    # int: 1-5

    # ---------- Новые методы ----------
    def has_toilet(self):
        return self._has_toilet

    def get_comfort_level(self):
        return self._comfort_level

    # ---------- Переопределение методов базового класса (полиморфизм) ----------
    def get_bus_type(self):
        return "Туристический автобус"

    def calculate_price(self, distance_km):
        """Туристический автобус дороже: 35 руб/км."""
        return distance_km * 35

    # ---------- Переопределение __str__ ----------
    def __str__(self):
        toilet_str = "с туалетом" if self._has_toilet else "без туалета"
        return (f"Туристический автобус {self.route}: {self.passengers}/{self.capacity} пасс., "
                f"статус: {self.status}, {toilet_str}, комфорт: {self._comfort_level}/5")

    def __repr__(self):
        return (f"TouristBus('{self.route}', {self.capacity}, {self.passengers}, '{self.status}', "
                f"{self._has_toilet}, {self._comfort_level})")