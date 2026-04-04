# demo.py
from lab02.model2 import Bus
from collection import BusFleet

def print_separator(title):
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)

def main():
    b1 = Bus("101", 50, 10, "on_route")
    b2 = Bus("102", 60, 0, "parked")
    b3 = Bus("103", 40, 5, "on_route")
    b4 = Bus("104", 30, 0, "parked")
    b5 = Bus("105", 55, 20, "on_route")

    fleet = BusFleet()
    print("Создан автопарк (BusFleet)")

    for bus in [b1, b2, b3, b4, b5]:
        try:
            fleet.add(bus)
            print(f"Добавлен: {bus.route}")
        except ValueError as e:
            print(f"Ошибка добавления {bus.route}: {e}")

    # Проверка дубликата
    print("\nПопытка добавить автобус с существующим маршрутом 101:")
    try:
        fleet.add(Bus("101", 70))
    except ValueError as e:
        print(f"  Ошибка: {e}")

    print(f"\nВ коллекции {len(fleet)} автобусов.")

    print_separator("Все автобусы в коллекции")
    for bus in fleet:
        print(bus)

    print_separator("Поиск автобуса по маршруту")
    found = fleet.find_by_route("103")
    print(f"Поиск маршрута 103: {found}")

    print_separator("Фильтрация: автобусы на маршруте")
    on_route = fleet.find_all_by_status("on_route")
    for bus in on_route:
        print(bus)

    print_separator("Сортировка по вместимости (по возрастанию)")
    fleet.sort_by_capacity()
    for bus in fleet:
        print(f"{bus.route}: вместимость {bus.capacity}")

    print_separator("Индексация коллекции")
    print(f"Первый автобус: {fleet[0]}")
    print(f"Срез [1:3]: {fleet[1:3]}")

    print_separator("Удаление по объекту")
    fleet.remove(b2)
    print(f"После удаления 102 осталось {len(fleet)} автобусов.")

    print_separator("Удаление по индексу (remove_at)")
    removed = fleet.remove_at(2)
    print(f"Удалён {removed.route}")

    print_separator("Использование len() и for")
    print(f"Количество автобусов в автопарке: {len(fleet)}")
    for i, bus in enumerate(fleet):
        print(f"  {i}: {bus.route}")

    print_separator("Сценарий: отправка всех автобусов на маршрут")
    parked_fleet = fleet.find_all_by_status("parked")
    for bus in parked_fleet:
        try:
            bus.start_route()
            print(f"Автобус {bus.route} выехал на маршрут")
        except ValueError as e:
            print(f"Ошибка с {bus.route}: {e}")

    print_separator("Сценарий: попытка добавить некорректный тип")
    try:
        fleet.add("это строка, не автобус")
    except TypeError as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()