# app.py
"""Бизнес-логика приложения."""

from typing import List, Optional
from models7 import Bus, CityBus, TouristBus
from collection7 import BusFleet
from exceptions7 import DuplicateItemError, ItemNotFoundError, InvalidInputError


class BusApp:
    """Управление данными приложения."""

    def __init__(self) -> None:
        self._fleet: BusFleet = BusFleet()

    def load_initial_data(self, buses: List[Bus]) -> None:
        """Загружает начальные данные в коллекцию."""
        for bus in buses:
            try:
                self._fleet.add(bus)
            except ValueError:
                pass

    def get_all_buses(self) -> List[Bus]:
        """Возвращает список всех автобусов."""
        return self._fleet.get_all()

    def add_bus(self, bus: Bus) -> None:
        """
        Добавляет автобус.
        
        Raises:
            DuplicateItemError: если автобус с таким маршрутом уже есть
        """
        try:
            self._fleet.add(bus)
        except ValueError as e:
            raise DuplicateItemError(str(e))

    def remove_bus_by_route(self, route: str) -> Bus:
        """
        Удаляет автобус по маршруту.
        
        Raises:
            ItemNotFoundError: если автобус не найден
        """
        try:
            return self._fleet.remove_by_route(route)
        except ValueError as e:
            raise ItemNotFoundError(str(e))

    def find_bus_by_route(self, route: str) -> Optional[Bus]:
        """Находит автобус по маршруту."""
        return self._fleet.find_by_route(route)

    def find_buses_by_status(self, status: str) -> List[Bus]:
        """Находит все автобусы с заданным статусом."""
        return self._fleet.filter_by_predicate(lambda bus: bus.status == status)

    def find_buses_with_passengers(self) -> List[Bus]:
        """Находит автобусы с пассажирами."""
        return self._fleet.filter_by_predicate(lambda bus: bus.passengers > 0)

    def sort_buses_by_route(self, reverse: bool = False) -> None:
        """Сортирует автобусы по маршруту."""
        self._fleet.sort_by(key_func=lambda bus: bus.route, reverse=reverse)

    def sort_buses_by_capacity(self, reverse: bool = False) -> None:
        """Сортирует автобусы по вместимости."""
        self._fleet.sort_by(key_func=lambda bus: bus.capacity, reverse=reverse)

    def sort_buses_by_passengers(self, reverse: bool = False) -> None:
        """Сортирует автобусы по количеству пассажиров."""
        self._fleet.sort_by(key_func=lambda bus: bus.passengers, reverse=reverse)

    def get_fleet(self) -> BusFleet:
        return self._fleet

    def start_route(self, route: str) -> None:
        """Отправляет автобус на маршрут."""
        bus = self.find_bus_by_route(route)
        if bus is None:
            raise ItemNotFoundError(f"Автобус с маршрутом {route} не найден")
        bus.start_route()

    def park_bus(self, route: str) -> None:
        """Ставит автобус в парк."""
        bus = self.find_bus_by_route(route)
        if bus is None:
            raise ItemNotFoundError(f"Автобус с маршрутом {route} не найден")
        bus.park()

    def board_passengers(self, route: str, num: int) -> None:
        """Посадка пассажиров."""
        bus = self.find_bus_by_route(route)
        if bus is None:
            raise ItemNotFoundError(f"Автобус с маршрутом {route} не найден")
        bus.board(num)

    def alight_passengers(self, route: str, num: int) -> None:
        """Высадка пассажиров."""
        bus = self.find_bus_by_route(route)
        if bus is None:
            raise ItemNotFoundError(f"Автобус с маршрутом {route} не найден")
        bus.alight(num)

    def get_statistics(self) -> dict:
        """Возвращает статистику по коллекции."""
        buses = self._fleet.get_all()
        total = len(buses)
        on_route = len([b for b in buses if b.status == 'on_route'])
        parked = len([b for b in buses if b.status == 'parked'])
        with_pass = len([b for b in buses if b.passengers > 0])
        total_pass = sum(b.passengers for b in buses)
        return {
            'total': total,
            'on_route': on_route,
            'parked': parked,
            'with_passengers': with_pass,
            'total_passengers': total_pass
        }