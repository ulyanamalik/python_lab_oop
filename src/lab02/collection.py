# collection.py
# Класс-контейнер для хранения автобусов (автопарк).

from model2 import Bus   # импортируем класс Bus из model.py

class BusFleet:
    """
    Коллекция автобусов. Позволяет добавлять, удалять, искать, сортировать,
    получать доступ по индексу, итерироваться и т.д.
    """

    def __init__(self):
        """Инициализация: создаём пустой внутренний список."""
        self._items = []          # защищённый список объектов Bus

    # ---------- Базовые операции управления ----------
    def add(self, bus):
        """
        Добавить автобус в коллекцию.
        Проверяет тип и уникальность номера маршрута.
        """
        if not isinstance(bus, Bus):
            raise TypeError("Можно добавлять только объекты Bus")
        # Проверяем, нет ли уже автобуса с таким же номером маршрута
        for existing in self._items:
            if existing.route == bus.route:
                raise ValueError(f"Автобус с маршрутом {bus.route} уже существует")
        self._items.append(bus)

    def remove(self, bus):
        """Удалить автобус из коллекции (по объекту)."""
        if bus not in self._items:
            raise ValueError("Такого автобуса нет в коллекции")
        self._items.remove(bus)

    def remove_at(self, index):
        """
        Удалить автобус по индексу (реализация для оценки 5).
        Возвращает удалённый объект.
        """
        if not isinstance(index, int) or index < 0 or index >= len(self._items):
            raise IndexError("Неверный индекс")
        return self._items.pop(index)

    def get_all(self):
        """Вернуть копию списка всех автобусов (для безопасного доступа)."""
        return self._items.copy()

    # ---------- Поиск (для оценки 4 и 5) ----------
    def find_by_route(self, route):
        """Найти первый автобус с указанным номером маршрута."""
        for bus in self._items:
            if bus.route == route:
                return bus
        return None

    def find_all_by_status(self, status):
        """
        Вернуть новую коллекцию, содержащую автобусы с заданным статусом.
        (логическая операция – фильтрация)
        """
        result = BusFleet()
        for bus in self._items:
            if bus.status == status:
                result.add(bus)
        return result

    def find_all_with_passengers(self):
        """Вернуть новую коллекцию автобусов, в которых есть пассажиры."""
        result = BusFleet()
        for bus in self._items:
            if bus.passengers > 0:
                result.add(bus)
        return result

    # ---------- Сортировка (для оценки 5) ----------
    def sort_by_route(self, reverse=False):
        """Сортировка по номеру маршрута (по возрастанию/убыванию)."""
        self._items.sort(key=lambda bus: bus.route, reverse=reverse)

    def sort_by_capacity(self, reverse=False):
        """Сортировка по вместимости."""
        self._items.sort(key=lambda bus: bus.capacity, reverse=reverse)

    def sort_by_passengers(self, reverse=False):
        """Сортировка по количеству пассажиров."""
        self._items.sort(key=lambda bus: bus.passengers, reverse=reverse)

    # ---------- Магические методы (для удобства) ----------
    def __len__(self):
        """Возвращает количество автобусов в коллекции."""
        return len(self._items)

    def __iter__(self):
        """Позволяет использовать for bus in fleet."""
        return iter(self._items)

    def __getitem__(self, index):
        """
        Поддержка индексации и срезов: fleet[0], fleet[1:3].
        """
        return self._items[index]

    def __str__(self):
        """Удобное строковое представление коллекции."""
        return f"BusFleet with {len(self)} buses: {[bus.route for bus in self._items]}"

    def __repr__(self):
        """Официальное представление."""
        return f"BusFleet({self._items})"