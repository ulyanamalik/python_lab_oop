# collection.py
from model2 import Bus

class BusFleet:
    """Коллекция автобусов (автопарк)."""

    def __init__(self):
        self._items = []          # внутренний список для хранения объектов Bus

    # ---- Базовые операции ----
    def add(self, bus):
        """Добавить автобус в коллекцию (проверка типа и уникальности маршрута)."""
        if not isinstance(bus, Bus):
            raise TypeError("Можно добавлять только объекты Bus")
        # Проверка дубликата: автобус с таким же номером маршрута уже есть?
        for existing in self._items:
            if existing.route == bus.route:
                raise ValueError(f"Автобус с маршрутом {bus.route} уже существует в коллекции")
        self._items.append(bus)

    def remove(self, bus):
        """Удалить автобус из коллекции (по объекту)."""
        if bus not in self._items:
            raise ValueError("Такого автобуса нет в коллекции")
        self._items.remove(bus)

    def remove_at(self, index):
        """Удалить автобус по индексу (реализация для 5)."""
        if not isinstance(index, int) or index < 0 or index >= len(self._items):
            raise IndexError("Неверный индекс")
        return self._items.pop(index)

    def get_all(self):
        """Вернуть список всех автобусов (копию)."""
        return self._items.copy()

    # ---- Поиск ----
    def find_by_route(self, route):
        """Найти автобус по номеру маршрута (первый подходящий)."""
        for bus in self._items:
            if bus.route == route:
                return bus
        return None

    def find_all_by_status(self, status):
        """Найти все автобусы с заданным статусом (возвращает новую коллекцию)."""
        result = BusFleet()
        for bus in self._items:
            if bus.status == status:
                result.add(bus)
        return result

    def find_all_with_passengers(self):
        """Найти автобусы, в которых есть пассажиры."""
        result = BusFleet()
        for bus in self._items:
            if bus.passengers > 0:
                result.add(bus)
        return result

    # ---- Сортировка ----
    def sort_by_route(self, reverse=False):
        """Сортировка по номеру маршрута (по алфавиту/числовому значению)."""
        self._items.sort(key=lambda bus: bus.route, reverse=reverse)

    def sort_by_capacity(self, reverse=False):
        """Сортировка по вместимости."""
        self._items.sort(key=lambda bus: bus.capacity, reverse=reverse)

    def sort_by_passengers(self, reverse=False):
        """Сортировка по количеству пассажиров."""
        self._items.sort(key=lambda bus: bus.passengers, reverse=reverse)

    # ---- Магические методы для удобства ----
    def __len__(self):
        """Возвращает количество автобусов в коллекции."""
        return len(self._items)

    def __iter__(self):
        """Позволяет итерироваться по коллекции (for bus in fleet)."""
        return iter(self._items)

    def __getitem__(self, index):
        """Поддержка индексации fleet[0], fleet[1:3] (срез)."""
        return self._items[index]

    def __str__(self):
        """Строковое представление коллекции (количество автобусов)."""
        return f"BusFleet with {len(self)} buses: {[bus.route for bus in self._items]}"

    def __repr__(self):
        return f"BusFleet({self._items})"