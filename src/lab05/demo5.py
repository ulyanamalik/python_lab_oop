# demo.py
"""Демонстрация функций высшего порядка, стратегий и цепочек операций."""

from models5 import Bus, CityBus, TouristBus
from collection5 import BusFleet
from strategies5 import (
    by_route, by_capacity, by_passengers, by_route_then_capacity,
    is_on_route, is_parked, has_passengers, is_city_bus, is_tourist_bus,
    capacity_less_than, capacity_greater_than,
    to_string, to_route, to_route_with_type, apply_discount,
    RouteSorter, CapacitySorter, PassengerSorter,
    OnRouteFilter, ParkedFilter,
    AddPassengersStrategy
)

def print_separator(title):
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)

def print_collection(title, collection):
    """Выводит коллекцию с заголовком."""
    print(f"\n{title} ({len(collection)} автобусов):")
    for bus in collection:
        print(f"  {bus.route}: вместимость {bus.capacity}, пассажиров {bus.passengers}, статус: {bus.status}")


def main():
    # ========== 1. СОЗДАНИЕ ОБЪЕКТОВ И КОЛЛЕКЦИИ ==========
    print_separator("Создание объектов и наполнение коллекции")

    b1 = Bus("103", 50, 10, "on_route")
    b2 = Bus("101", 40, 5, "parked")
    b3 = CityBus("105", 55, 0, "parked", "городской", True)
    b4 = CityBus("102", 35, 8, "on_route", "пригородный", False)
    b5 = TouristBus("104", 30, 3, "on_route", True, 5)
    b6 = TouristBus("106", 45, 0, "parked", False, 3)

    fleet = BusFleet()
    for bus in [b1, b2, b3, b4, b5, b6]:
        fleet.add(bus)
        print(f"Добавлен: {bus}")

    print_collection("Исходная коллекция", fleet)

    # ========== 2. СОРТИРОВКА С РАЗНЫМИ СТРАТЕГИЯМИ (оценка 3) ==========
    print_separator("Сортировка по маршруту (by_route)")
    sorted_fleet = BusFleet()
    for bus in sorted(fleet.get_all(), key=by_route):
        sorted_fleet.add(bus)
    print_collection("После сортировки по маршруту", sorted_fleet)

    print_separator("Сортировка по вместимости (by_capacity)")
    sorted_fleet = BusFleet()
    for bus in sorted(fleet.get_all(), key=by_capacity):
        sorted_fleet.add(bus)
    print_collection("После сортировки по вместимости", sorted_fleet)

    print_separator("Сортировка по пассажирам (by_passengers)")
    sorted_fleet = BusFleet()
    for bus in sorted(fleet.get_all(), key=by_passengers):
        sorted_fleet.add(bus)
    print_collection("После сортировки по пассажирам", sorted_fleet)

    print_separator("Сортировка по маршруту, затем вместимости")
    sorted_fleet = BusFleet()
    for bus in sorted(fleet.get_all(), key=by_route_then_capacity):
        sorted_fleet.add(bus)
    print_collection("После составной сортировки", sorted_fleet)

    # ========== 3. ФИЛЬТРАЦИЯ С РАЗНЫМИ ФУНКЦИЯМИ (оценка 3) ==========
    print_separator("Фильтрация: автобусы на маршруте")
    on_route_buses = list(filter(is_on_route, fleet.get_all()))
    print(f"На маршруте ({len(on_route_buses)}): {[b.route for b in on_route_buses]}")

    print_separator("Фильтрация: автобусы с пассажирами")
    with_passengers = list(filter(has_passengers, fleet.get_all()))
    print(f"С пассажирами ({len(with_passengers)}): {[b.route for b in with_passengers]}")

    # ========== 4. ПРИМЕНЕНИЕ map() (оценка 4) ==========
    print_separator("map(): извлечение номеров маршрутов")
    routes = list(map(to_route, fleet.get_all()))
    print(f"Маршруты: {routes}")

    print_separator("map(): преобразование в строки")
    strings = list(map(to_string, fleet.get_all()))
    for s in strings:
        print(f"  {s}")

    print_separator("map(): применение скидки (фабрика функций)")
    discount_10 = apply_discount(10)
    discount_results = list(map(discount_10, fleet.get_all()))
    for res in discount_results:
        print(f"  {res}")

    # ========== 5. ФАБРИКА ФУНКЦИЙ ДЛЯ ФИЛЬТРАЦИИ (оценка 4) ==========
    print_separator("Фабрика фильтров: вместимость < 40")
    filter_capacity_less_40 = capacity_less_than(40)
    small_buses = list(filter(filter_capacity_less_40, fleet.get_all()))
    print(f"Автобусы с вместимостью < 40: {[b.route for b in small_buses]}")

    print_separator("Фабрика фильтров: вместимость > 45")
    filter_capacity_greater_45 = capacity_greater_than(45)
    large_buses = list(filter(filter_capacity_greater_45, fleet.get_all()))
    print(f"Автобусы с вместимостью > 45: {[b.route for b in large_buses]}")

    # ========== 6. МЕТОДЫ КОЛЛЕКЦИИ sort_by() и filter_by() (оценка 4) ==========
    print_separator("Метод коллекции sort_by(by_capacity)")
    fleet_copy = BusFleet()
    for bus in fleet.get_all():
        fleet_copy.add(bus)
    fleet_copy.sort_by(by_capacity)
    print_collection("После sort_by(by_capacity)", fleet_copy)

    print_separator("Метод коллекции filter_by(is_parked)")
    parked_fleet = fleet.filter_by(is_parked)
    print_collection("Автобусы в парке", parked_fleet)

    print_separator("Сравнение lambda и именованной функции")
    lambda_sorted = sorted(fleet.get_all(), key=lambda b: b.route)
    named_sorted = sorted(fleet.get_all(), key=by_route)
    print(f"lambda: {[b.route for b in lambda_sorted]}")
    print(f"named:  {[b.route for b in named_sorted]}")
    print("Результаты одинаковы!")

    # ========== 7. ПАТТЕРН «СТРАТЕГИЯ» ЧЕРЕЗ CALLABLE-ОБЪЕКТЫ (оценка 5) ==========
    print_separator("Callable-объект RouteSorter как стратегия сортировки")
    route_sorter = RouteSorter()
    sorted_by_callable = sorted(fleet.get_all(), key=route_sorter)
    print(f"Сортировка через callable: {[b.route for b in sorted_by_callable]}")

    print_separator("Callable-объект OnRouteFilter как стратегия фильтрации")
    on_route_filter = OnRouteFilter()
    on_route_callable = list(filter(on_route_filter, fleet.get_all()))
    print(f"Фильтрация через callable: {[b.route for b in on_route_callable]}")

    # ========== 8. МЕТОД apply() — применение функции ко всем элементам (оценка 5) ==========
    print_separator("Метод apply(): добавление пассажиров (стратегия AddPassengersStrategy)")
    add_5_strategy = AddPassengersStrategy(5)
    results = fleet.apply(add_5_strategy)
    for res in results:
        print(f"  {res}")

    print_collection("Коллекция после добавления пассажиров", fleet)

    # ========== 9. ЦЕПОЧКА ОПЕРАЦИЙ (filter → sort → map) (оценка 5) ==========
    print_separator("Цепочка операций: фильтрация -> сортировка -> преобразование")

    # Сценарий 1: берём автобусы на маршруте, сортируем по вместимости, выводим маршруты
    result = (fleet
        .filter_by(is_on_route)
        .sort_by(by_capacity)
        .map_to(to_route))
    print(f"Автобусы на маршруте, отсортированные по вместимости: {result}")

    # Сценарий 2: берём автобусы в парке, сортируем по маршруту, выводим информацию
    result2 = (fleet
        .filter_by(is_parked)
        .sort_by(by_route)
        .map_to(to_string))
    print("\nАвтобусы в парке, отсортированные по маршруту:")
    for s in result2:
        print(f"  {s}")

    # Сценарий 3: замена стратегии без изменения кода коллекции
    print_separator("Замена стратегии без изменения кода коллекции")
    
    # Сортируем по маршруту
    fleet.sort_by(by_route)
    print(f"Сортировка по маршруту: {[b.route for b in fleet]}")
    
    # Сортируем по вместимости (другая стратегия)
    fleet.sort_by(by_capacity)
    print(f"Сортировка по вместимости: {[b.route for b in fleet]}")

    # Сортируем по пассажирам (третья стратегия)
    fleet.sort_by(by_passengers)
    print(f"Сортировка по пассажирам: {[b.route for b in fleet]}")

    print("\n Все стратегии взаимозаменяемы — код коллекции не менялся!")

    # ========== 10. ДОПОЛНИТЕЛЬНЫЕ СЦЕНАРИИ ==========
    print_separator("Дополнительный сценарий: фильтрация по типу (городские/туристические)")
    
    city_buses = fleet.filter_by(is_city_bus)
    tourist_buses = fleet.filter_by(is_tourist_bus)
    
    print(f"Городские автобусы: {[b.route for b in city_buses]}")
    print(f"Туристические автобусы: {[b.route for b in tourist_buses]}")

if __name__ == "__main__":
    main()