# demo.py
from base3 import Bus
from models3 import CityBus, TouristBus
from collection3 import BusFleet

def print_separator(title):
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)

def main():
    #Создание объектов разных типов
    print_separator("Создание объектов разных типов")

    b1 = Bus("101", 50, 10, "on_route")
    b2 = CityBus("201", 60, 5, "parked", "городской", True)
    b3 = CityBus("202", 40, 0, "on_route", "пригородный", False)
    b4 = TouristBus("301", 30, 15, "on_route", True, 5)
    b5 = TouristBus("302", 35, 0, "parked", False, 3)

    print(f"Создан: {b1}")
    print(f"Создан: {b2}")
    print(f"Создан: {b3}")
    print(f"Создан: {b4}")
    print(f"Создан: {b5}")

    #Добавление в коллекцию
    print_separator("Добавление разных типов автобусов в коллекцию")

    fleet = BusFleet()
    for bus in [b1, b2, b3, b4, b5]:
        try:
            fleet.add(bus)
            print(f"Добавлен: {bus.route} ({bus.get_bus_type()})")
        except ValueError as e:
            print(f"Ошибка: {e}")

    print(f"\nВ коллекции {len(fleet)} автобусов.")

    # Полиморфизм: get_bus_type()
    print_separator("Полиморфизм: метод get_bus_type()")

    for bus in fleet:
        print(f"{bus.route}: {bus.get_bus_type()}")

    #Полиморфизм: calculate_price()
    print_separator("Полиморфизм: метод calculate_price() (100 км)")

    distance = 100
    for bus in fleet:
        price = bus.calculate_price(distance)
        print(f"{bus.route} ({bus.get_bus_type()}): {price} руб за {distance} км")

    #Проверка типов через isinstance()
    print_separator("Проверка типов через isinstance()")

    for bus in fleet:
        if isinstance(bus, CityBus):
            print(f"{bus.route}: это городской автобус")
        elif isinstance(bus, TouristBus):
            print(f"{bus.route}: это туристический автобус")
        else:
            print(f"{bus.route}: это обычный автобус")

    # Фильтрация по типу 
    print_separator("Фильтрация: только городские автобусы")

    city_fleet = fleet.get_only_city_buses()
    for bus in city_fleet:
        print(bus)

    print_separator("Фильтрация: только туристические автобусы")

    tourist_fleet = fleet.get_only_tourist_buses()
    for bus in tourist_fleet:
        print(bus)

    # Новые методы дочерних классов 
    print_separator("Новые методы дочерних классов")

    print("Городские автобусы:")
    for bus in city_fleet:
        print(f"  Маршрут {bus.route}: тип маршрута = {bus.get_route_type()}, "
              f"кондиционер = {'да' if bus.has_ac() else 'нет'}")

    print("\nТуристические автобусы:")
    for bus in tourist_fleet:
        print(f"  Маршрут {bus.route}: туалет = {'да' if bus.has_toilet() else 'нет'}, "
              f"комфорт = {bus.get_comfort_level()}/5")

    #Бизнес-методы 
    print_separator("Бизнес-методы (посадка/высадка)")

    print(f"До посадки: {b2}")
    b2.start_route()
    b2.board(10)
    print(f"После посадки 10: {b2}")
    b2.alight(3)
    print(f"После высадки 3: {b2}")

    #Полиморфизм без условий (единый вызов start_route)
    print_separator("Полиморфизм без условий (единый вызов start_route)")

    # Создаём специальные автобусы в статусе parked для демонстрации
    test_city = CityBus("999", 50, 0, "parked", "тестовый", True)
    test_tourist = TouristBus("888", 40, 0, "parked", True, 4)

    print(f"Создан тестовый городской: {test_city}")
    print(f"Создан тестовый туристический: {test_tourist}")

    for bus in [test_city, test_tourist]:
        bus.start_route()
        print(f"{bus.route} ({bus.get_bus_type()}) выехал на маршрут. Статус: {bus.status}")

    # Итоговое состояние
    print_separator("Итоговое состояние коллекции")

    for bus in fleet:
        print(bus)

    # Демонстрация валидации
    print_separator("Демонстрация валидации (ошибки при создании)")

    try:
        invalid_bus = CityBus("", 50, 0, "parked", "городской", True)
    except ValueError as e:
        print(f"Ошибка при создании CityBus: {e}")

    try:
        invalid_tourist = TouristBus("303", 40, 0, "parked", True, 10)
    except ValueError as e:
        print(f"Ошибка при создании TouristBus: {e}")

    try:
        invalid_capacity = Bus("", -10)
    except ValueError as e:
        print(f"Ошибка при создании Bus: {e}")

if __name__ == "__main__":
    main()