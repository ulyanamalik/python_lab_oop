# collection.py
"""Класс коллекции BusFleet."""

from typing import List, Optional, Callable, Iterator
from models7 import Bus


class BusFleet:
    """Коллекция автобусов."""

    def __init__(self) -> None:
        self._items: List[Bus] = []

    def add(self, bus: Bus) -> None:
        """Добавляет автобус в коллекцию."""
        for existing in self._items:
            if existing.route == bus.route:
                raise ValueError(f"Автобус с маршрутом {bus.route} уже существует")
        self._items.append(bus)

    def remove(self, bus: Bus) -> None:
        """Удаляет автобус из коллекции."""
        if bus not in self._items:
            raise ValueError("Такого автобуса нет в коллекции")
        self._items.remove(bus)

    def remove_by_route(self, route: str) -> Bus:
        """Удаляет автобус по маршруту и возвращает его."""
        for i, bus in enumerate(self._items):
            if bus.route == route:
                return self._items.pop(i)
        raise ValueError(f"Автобус с маршрутом {route} не найден")

    def get_all(self) -> List[Bus]:
        return self._items.copy()

    def find_by_route(self, route: str) -> Optional[Bus]:
        for bus in self._items:
            if bus.route == route:
                return bus
        return None

    def find_by_predicate(self, predicate: Callable[[Bus], bool]) -> Optional[Bus]:
        for bus in self._items:
            if predicate(bus):
                return bus
        return None

    def filter_by_predicate(self, predicate: Callable[[Bus], bool]) -> List[Bus]:
        return [bus for bus in self._items if predicate(bus)]

    def sort_by(self, key_func: Callable[[Bus], any], reverse: bool = False) -> None:
        self._items.sort(key=key_func, reverse=reverse)

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[Bus]:
        return iter(self._items)

    def __getitem__(self, index: int) -> Bus:
        return self._items[index]

    def __str__(self) -> str:
        return f"BusFleet with {len(self)} buses"