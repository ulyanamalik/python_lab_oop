from model2 import Bus          # импортируем класс Bus
from collection import BusFleet   # импортируем класс коллекции

def main():
    # ---------- 1. Создаём несколько автобусов ----------
    b1 = Bus("101", 50, 10, "on_route")
    b2 = Bus("102", 60, 0, "parked")
    b3 = Bus("103", 40, 5, "on_route")
    b4 = Bus("104", 30, 0, "parked")
    b5 = Bus("105", 55, 20, "on_route")
    print()
    # ---------- 2. Создаём коллекцию и добавляем автобусы ----------
    fleet = BusFleet()
    print("Создан автопарк (BusFleet)")

    for bus in [b1, b2, b3, b4, b5]:
        try:
            fleet.add(bus)
            print(f"Добавлен: {bus.route}")
        except ValueError as e:
            print(f"Ошибка добавления {bus.route}: {e}")
    print()

    # Проверка защиты от дубликатов
    print("\nПопытка добавить автобус с существующим маршрутом 101:")
    try:
        fleet.add(Bus("101", 70))
    except ValueError as e:
        print(f"  Ошибка: {e}")

    print(f"\nВ коллекции {len(fleet)} автобусов.")  # __len__
    print()
    # ---------- 3. Вывод всех автобусов (через итерацию) ----------
    print("Все автобусы в коллекции")
    for bus in fleet:               # __iter__
        print(bus)                  # __str__ у Bus
    print()

    # ---------- 4. Поиск по маршруту ----------
    print("Поиск автобуса по маршруту")
    found = fleet.find_by_route("103")
    print(f"Поиск маршрута 103: {found}")
    print()

    # ---------- 5. Фильтрация (логические операции) ----------
    print("Фильтрация: автобусы на маршруте")
    on_route = fleet.find_all_by_status("on_route")   # новая коллекция
    for bus in on_route:
        print(bus)

    print("\nФильтрация: автобусы с пассажирами")
    with_pass = fleet.find_all_with_passengers()
    for bus in with_pass:
        print(bus)
    print()
    # ---------- 6. Сортировка ----------
    print("Сортировка по вместимости (по возрастанию)")
    fleet.sort_by_capacity()
    for bus in fleet:
        print(f"{bus.route}: вместимость {bus.capacity}")

    print("\nСортировка по маршруту (по убыванию)")
    fleet.sort_by_route(reverse=True)
    for bus in fleet:
        print(bus.route)
    print()
    # ---------- 7. Индексация (__getitem__) ----------
    print("Индексация коллекции")
    print(f"Первый автобус: {fleet[0]}")
    print(f"Третий автобус: {fleet[2]}")
    print(f"Срез [1:3]: {fleet[1:3]}")   # срез тоже работает
    print()

    # ---------- 8. Удаление элементов ----------
    print("Удаление по объекту")
    print(f"Удаляем автобус с маршрутом 102: {b2}")
    fleet.remove(b2)
    print(f"Теперь в коллекции {len(fleet)} автобусов:")
    for bus in fleet:
        print(bus)
    print()

    print("\nУдаление по индексу (remove_at)")
    removed = fleet.remove_at(2)
    print(f"Удалён {removed.route} (индекс 2)")
    print(f"Осталось {len(fleet)} автобусов:")
    for bus in fleet:
        print(bus)
    print()
    # ---------- 9. Использование len() и итерации ещё раз ----------
    print("Использование len() и for")
    print(f"Количество автобусов в автопарке: {len(fleet)}")
    print("Перебор всех оставшихся автобусов:")
    for i, bus in enumerate(fleet):
        print(f"  {i}: {bus.route}")
    print()
    # ---------- 10. Сценарий: отправка всех паркующихся автобусов на маршрут ----------
    print("Сценарий: отправка всех автобусов на маршрут")
    parked_fleet = fleet.find_all_by_status("parked")
    for bus in parked_fleet:
        try:
            bus.start_route()
            print(f"Автобус {bus.route} выехал на маршрут")
        except ValueError as e:
            print(f"Ошибка с {bus.route}: {e}")
    print()
    # ---------- 11. Сценарий: попытка добавить некорректный тип ----------
    print("Сценарий: попытка добавить некорректный тип")
    try:
        fleet.add("это строка, не автобус")
    except TypeError as e:
        print(f"Ошибка: {e}")

    # Итог: все методы продемонстрированы, код работает корректно.

if __name__ == "__main__":
    main()