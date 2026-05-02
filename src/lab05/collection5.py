# collection.py
"""Класс-контейнер BusFleet с поддержкой функций высшего порядка."""

from models5 import Bus

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

    def get_all(self):
        return self._items.copy()

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __str__(self):
        return f"BusFleet with {len(self)} buses: {[bus.route for bus in self._items]}"

    # ========== НОВЫЕ МЕТОДЫ ДЛЯ ЛР-5 ==========

    def sort_by(self, key_func, reverse=False):
        """
        Сортирует коллекцию с помощью переданной функции-ключа.
        
        Аргументы:
            key_func: функция, которая извлекает ключ для сравнения
            reverse: если True, сортировка по убыванию
        """
        self._items.sort(key=key_func, reverse=reverse)
        return self  # возвращаем self для цепочек вызовов

    def filter_by(self, predicate):
        """
        Фильтрует коллекцию с помощью переданной функции-предиката.
        Возвращает НОВУЮ коллекцию с отфильтрованными элементами.
        
        Аргументы:
            predicate: функция, возвращающая True/False для каждого элемента
        """
        result = BusFleet()
        for bus in self._items:
            if predicate(bus):
                result.add(bus)
        return result

    def apply(self, func):
        """
        Применяет произвольную функцию ко всем элементам коллекции.
        
        Аргументы:
            func: функция, которая принимает один аргумент (bus) и возвращает что-либо
        """
        results = []
        for bus in self._items:
            results.append(func(bus))
        return results

    def map_to(self, transform_func):
        """
        Преобразует коллекцию в список результатов применения функции.
        
        Аргументы:
            transform_func: функция для преобразования каждого элемента
        """
        return list(map(transform_func, self._items))