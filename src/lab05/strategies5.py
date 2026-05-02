# strategies.py
"""Функции-стратегии, фильтры, фабрики и callable-объекты для лабораторной работы №5."""

# ========== СТРАТЕГИИ СОРТИРОВКИ (для sorted и sort) ==========

def by_route(bus):
    """Ключ для сортировки по номеру маршрута."""
    return bus.route

def by_capacity(bus):
    """Ключ для сортировки по вместимости."""
    return bus.capacity

def by_passengers(bus):
    """Ключ для сортировки по количеству пассажиров."""
    return bus.passengers

def by_route_then_capacity(bus):
    """Ключ для сортировки по маршруту, затем по вместимости (кортеж)."""
    return (bus.route, bus.capacity)


# ========== ФУНКЦИИ-ФИЛЬТРЫ (для filter) ==========

def is_on_route(bus):
    """Фильтр: автобус на маршруте."""
    return bus.status == 'on_route'

def is_parked(bus):
    """Фильтр: автобус в парке."""
    return bus.status == 'parked'

def has_passengers(bus):
    """Фильтр: в автобусе есть пассажиры."""
    return bus.passengers > 0

def is_city_bus(bus):
    """Фильтр: городской автобус (по типу)."""
    from models5 import CityBus
    return isinstance(bus, CityBus)

def is_tourist_bus(bus):
    """Фильтр: туристический автобус."""
    from models5 import TouristBus
    return isinstance(bus, TouristBus)

def capacity_less_than(limit):
    """Фабрика функций: создаёт фильтр для отбора автобусов с вместимостью < limit."""
    def filter_fn(bus):
        return bus.capacity < limit
    return filter_fn

def capacity_greater_than(limit):
    """Фабрика функций: создаёт фильтр для отбора автобусов с вместимостью > limit."""
    def filter_fn(bus):
        return bus.capacity > limit
    return filter_fn


# ========== ФУНКЦИИ ДЛЯ map (преобразование) ==========

def to_string(bus):
    """Преобразует автобус в строку."""
    return str(bus)

def to_route(bus):
    """Извлекает номер маршрута."""
    return bus.route

def to_route_with_type(bus):
    """Извлекает кортеж (маршрут, тип автобуса)."""
    return (bus.route, bus.get_bus_type())

def apply_discount(percent):
    """Фабрика функций: создаёт функцию для применения скидки (демонстрация map)."""
    def discount_fn(bus):
        # Условная скидка на вместимость (учебный пример)
        new_capacity = int(bus.capacity * (1 - percent / 100))
        return f"Автобус {bus.route}: была вместимость {bus.capacity}, стала {new_capacity} (скидка {percent}%)"
    return discount_fn


# ========== CALLABLE-ОБЪЕКТЫ (паттерн Стратегия) ==========

class RouteSorter:
    """Callable-объект для сортировки по маршруту."""
    def __call__(self, bus):
        return bus.route

class CapacitySorter:
    """Callable-объект для сортировки по вместимости."""
    def __call__(self, bus):
        return bus.capacity

class PassengerSorter:
    """Callable-объект для сортировки по количеству пассажиров."""
    def __call__(self, bus):
        return bus.passengers


class OnRouteFilter:
    """Callable-объект для фильтрации автобусов на маршруте."""
    def __call__(self, bus):
        return bus.status == 'on_route'

class ParkedFilter:
    """Callable-объект для фильтрации автобусов в парке."""
    def __call__(self, bus):
        return bus.status == 'parked'


class AddPassengersStrategy:
    """Callable-объект для добавления пассажиров (стратегия обработки)."""
    def __init__(self, num):
        self.num = num

    def __call__(self, bus):
        try:
            bus.board(self.num)
            return f"{bus.route}: добавлено {self.num} пассажиров, стало {bus.passengers}"
        except ValueError as e:
            return f"{bus.route}: ошибка - {e}"