# collection.py
"""Класс-контейнер для хранения автобусов (Bus, CityBus, TouristBus)."""

from base3 import Bus

class BusFleet:
    def __init__(self):
        self._items = []

    def add(self, bus):
        if not isinstance(bus, Bus):
            raise TypeError("Можно добавлять только объекты Bus или его наследников")
        for existing in self._items:
            if existing.route == bus.route:
                raise ValueError(f"Автобус с маршрутом {bus.route} уже существует")
        self._items.append(bus)

    def remove(self, bus):
        if bus not in self._items:
            raise ValueError("Такого автобуса нет в коллекции")
        self._items.remove(bus)

    def remove_at(self, index):
        if not isinstance(index, int) or index < 0 or index >= len(self._items):
            raise IndexError("Неверный индекс")
        return self._items.pop(index)

    def get_all(self):
        return self._items.copy()

    # ---------- Поиск ----------
    def find_by_route(self, route):
        for bus in self._items:
            if bus.route == route:
                return bus
        return None

    def find_all_by_status(self, status):
        result = BusFleet()
        for bus in self._items:
            if bus.status == status:
                result.add(bus)
        return result

    def find_all_with_passengers(self):
        result = BusFleet()
        for bus in self._items:
            if bus.passengers > 0:
                result.add(bus)
        return result

    # ---------- Фильтрация по типу (для оценки 5) ----------
    def get_only_city_buses(self):
        """Возвращает новую коллекцию только с городскими автобусами."""
        from models3 import CityBus
        result = BusFleet()
        for bus in self._items:
            if isinstance(bus, CityBus):
                result.add(bus)
        return result

    def get_only_tourist_buses(self):
        """Возвращает новую коллекцию только с туристическими автобусами."""
        from models3 import TouristBus
        result = BusFleet()
        for bus in self._items:
            if isinstance(bus, TouristBus):
                result.add(bus)
        return result

    # ---------- Сортировка ----------
    def sort_by_route(self, reverse=False):
        self._items.sort(key=lambda bus: bus.route, reverse=reverse)

    def sort_by_capacity(self, reverse=False):
        self._items.sort(key=lambda bus: bus.capacity, reverse=reverse)

    def sort_by_passengers(self, reverse=False):
        self._items.sort(key=lambda bus: bus.passengers, reverse=reverse)

    # ---------- Магические методы ----------
    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __str__(self):
        return f"BusFleet with {len(self)} buses: {[bus.route for bus in self._items]}"

    def __repr__(self):
        return f"BusFleet({self._items})"