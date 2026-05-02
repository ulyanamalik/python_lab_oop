from models4 import Bus, CityBus, TouristBus
from collection4 import BusFleet
from interfaces4 import Printable, Comparable, PriceCalculable

def print_separator(title):
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)

# ---------- Универсальная функция, работающая через интерфейс----------
def print_all_printable(items):
    """Принимает список объектов с интерфейсом Printable и выводит их."""
    for item in items:
        print(item.to_string())


def compare_buses(bus1, bus2):
    """Сравнивает два автобуса через интерфейс Comparable."""
    if isinstance(bus1, Comparable) and isinstance(bus2, Comparable):
        result = bus1.compare_to(bus2)
        if result < 0:
            print(f"{bus1.route} < {bus2.route}")
        elif result == 0:
            print(f"{bus1.route} == {bus2.route}")
        else:
            print(f"{bus1.route} > {bus2.route}")
    else:
        print("Объекты не реализуют интерфейс Comparable")


def main():
    # ========== 1. Создание объектов ==========
    print_separator("Создание объектов разных типов")

    b1 = Bus("101", 50, 10, "on_route")
    b2 = CityBus("201", 60, 5, "parked", "городской", True)
    b3 = TouristBus("301", 30, 15, "on_route", True, 5)

    print(b1.to_string())
    print(b2.to_string())
    print(b3.to_string())

    # ========== 2. Проверка реализации интерфейсов через isinstance() ==========
    print_separator("Проверка реализации интерфейсов через isinstance()")

    print(f"b1 implements Printable: {isinstance(b1, Printable)}")
    print(f"b1 implements Comparable: {isinstance(b1, Comparable)}")
    print(f"b1 implements PriceCalculable: {isinstance(b1, PriceCalculable)}")

    print(f"\nb2 implements Printable: {isinstance(b2, Printable)}")
    print(f"b2 implements Comparable: {isinstance(b2, Comparable)}")
    print(f"b2 implements PriceCalculable: {isinstance(b2, PriceCalculable)}")

    # ========== 3. Универсальная функция print_all_printable() ==========
    print_separator("Универсальная функция print_all_printable()")

    items = [b1, b2, b3]
    print_all_printable(items)

    # ========== 4. Сравнение через интерфейс Comparable ==========
    print_separator("Сравнение через интерфейс Comparable")

    compare_buses(b1, b2)
    compare_buses(b2, b3)
    compare_buses(b1, Bus("101", 40))  # одинаковый маршрут

    # ========== 5. Полиморфизм через интерфейс PriceCalculable ==========
    print_separator("Полиморфизм через интерфейс PriceCalculable (100 км)")

    for bus in [b1, b2, b3]:
        print(f"{bus.route}: {bus.calculate_price(100)} руб")

    # ========== 6. Работа с коллекцией (фильтрация по интерфейсу) ==========
    print_separator("Коллекция: добавление объектов")

    fleet = BusFleet()
    for bus in [b1, b2, b3]:
        fleet.add(bus)
        print(f"Добавлен: {bus.route}")

    print(f"\nВ коллекции {len(fleet)} автобусов.")

    # ========== 7. Фильтрация коллекции по интерфейсу ==========
    print_separator("Фильтрация коллекции по интерфейсу Printable")

    printable_fleet = fleet.get_printable()
    for bus in printable_fleet:
        print(bus.to_string())

    print_separator("Фильтрация коллекции по интерфейсу PriceCalculable")

    price_fleet = fleet.get_price_calculable()
    for bus in price_fleet:
        print(f"{bus.route}: {bus.calculate_price(50)} руб за 50 км")

    # ========== 8. Сортировка коллекции ==========
    print_separator("Сортировка коллекции по маршруту")

    fleet.sort_by_route()
    for bus in fleet:
        print(bus.route)

    # ========== 9. Полиморфизм без условий (через интерфейс) ==========
    print_separator("Полиморфизм без условий (единый вызов to_string())")

    for bus in fleet:
        print(bus.to_string())  # Разные объекты — разные представления!

    # ========== 10. Демонстрация валидации ==========
    print_separator("Демонстрация валидации")

    try:
        invalid_bus = Bus("", 50)
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        fleet.add("не автобус")
    except TypeError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()