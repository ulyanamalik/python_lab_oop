

from models6 import Bus, CityBus, TouristBus
from container6 import TypedCollection, DisplayableCollection, ScorableCollection
from container6 import Displayable, Scorable


def print_separator(title: str) -> None:
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)


def main() -> None:
    #СОЗДАНИЕ ОБЪЕКТОВ
    print_separator("Создание объектов разных типов")

    b1 = Bus("101", 50, 10, "on_route")
    b2 = CityBus("201", 60, 5, "parked", "городской", True)
    b3 = TouristBus("301", 30, 15, "on_route", True, 5)
    b4 = Bus("102", 40, 0, "parked")
    b5 = CityBus("202", 35, 8, "on_route", "пригородный", False)

    for bus in [b1, b2, b3, b4, b5]:
        print(bus.display())

    #ОБЫЧНАЯ GENERIC-КОЛЛЕКЦИЯ
    print_separator("TypedCollection[Bus] — обычная типизированная коллекция")

    bus_collection: TypedCollection[Bus] = TypedCollection()

    for bus in [b1, b2, b3, b4, b5]:
        bus_collection.add(bus)
        print(f"Добавлен: {bus.route}")

    print(f"\nВ коллекции {len(bus_collection)} автобусов.")

    print("\nВсе автобусы в коллекции:")
    for bus in bus_collection:
        print(f"  {bus.display()}")

    #МЕТОД FIND
    print_separator("Метод find() — поиск первого подходящего")

    # Поиск существующего автобуса
    found = bus_collection.find(lambda bus: bus.route == "201")
    if found:
        print(f"Найден автобус с маршрутом 201: {found.display()}")
    else:
        print("Автобус с маршрутом 201 не найден")

    # Поиск несуществующего автобуса
    not_found = bus_collection.find(lambda bus: bus.route == "999")
    print(f"Поиск маршрута 999: {not_found}")

    #МЕТОД FILTER
    print_separator("Метод filter() — отбор автобусов на маршруте")

    on_route_buses = bus_collection.filter(lambda bus: bus.status == 'on_route')
    print(f"Автобусы на маршруте ({len(on_route_buses)}):")
    for bus in on_route_buses:
        print(f"  {bus.route}")

    #МЕТОД MAP С РАЗНЫМИ ТИПАМИ РЕЗУЛЬТАТА
    print_separator("Метод map() — преобразование с изменением типа результата")

    # Преобразование 1: автобус → маршрут (Bus → str)
    routes: List[str] = bus_collection.map(lambda bus: bus.route)
    print(f"Маршруты (тип List[str]): {routes}")

    # Преобразование 2: автобус → вместимость (Bus → int)
    capacities: List[int] = bus_collection.map(lambda bus: bus.capacity)
    print(f"Вместимость (тип List[int]): {capacities}")

    # Преобразование 3: автобус → отформатированная строка
    strings: List[str] = bus_collection.map(lambda bus: f"{bus.route}: {bus.passengers}/{bus.capacity}")
    print("Строковое представление (List[str]):")
    for s in strings:
        print(f"  {s}")

    #КОЛЛЕКЦИЯ С ОГРАНИЧЕНИЕМ ПО ПРОТОКОЛУ
    print_separator("DisplayableCollection — коллекция объектов с методом display()")

    # Создаём коллекцию для объектов, у которых есть метод display()
    displayable_collection: DisplayableCollection = DisplayableCollection()

    # Добавляем объекты разных типов (все имеют метод display())
    displayable_collection.add(b1)   # Bus
    displayable_collection.add(b2)   # CityBus
    displayable_collection.add(b3)   # TouristBus

    print("Все объекты в DisplayableCollection (вызов display()):")
    for item in displayable_collection:
        print(f"  {item.display()}")

    #ДРУГОЙ ПРОТОКОЛ (Scorable)
    print_separator("ScorableCollection — коллекция объектов с методом score()")

    scorable_collection: ScorableCollection = ScorableCollection()
    scorable_collection.add(b1)
    scorable_collection.add(b2)
    scorable_collection.add(b3)

    print("Все объекты в ScorableCollection (результат score()):")
    for item in scorable_collection:
        print(f"  Автобус {item.route}: оценка = {item.score():.2f}")

    #ДЕМОНСТРАЦИЯ, ЧТО НАСЛЕДОВАНИЕ НЕ ТРЕБУЕТСЯ
    print_separator("Демонстрация: классы НЕ наследуются от протоколов")

    print("Класс Bus не наследуется от Displayable, но имеет метод display()")
    print("Класс CityBus не наследуется от Displayable, но имеет метод display()")
    print("Класс TouristBus не наследуется от Displayable, но имеет метод display()")
    print("\nЭто структурная типизация: важен интерфейс (наличие методов), а не наследование!")

    #ПОПЫТКА ДОБАВИТЬ ОБЪЕКТ БЕЗ НУЖНОГО МЕТОДА (закомментировано, так как вызовет ошибку)
    print_separator("Примечание о Type Safety")

    print("Если попытаться добавить в DisplayableCollection объект без метода display(),")
    print("статический анализатор типов (mypy / IDE) покажет ошибку.")
    print("Это демонстрирует пользу Generic и TypeVar с ограничениями (bound).")

    #ДОПОЛНИТЕЛЬНЫЙ СЦЕНАРИЙ: ФИЛЬТРАЦИЯ С ИСПОЛЬЗОВАНИЕМ map
    print_separator("Дополнительный сценарий: filter + map")

    # Берём автобусы на маршруте, извлекаем их маршруты
    on_route_routes = bus_collection.filter(lambda bus: bus.status == 'on_route')
    on_route_routes = list(map(lambda bus: bus.route, on_route_routes))
    print(f"Автобусы на маршруте: {on_route_routes}")

    #ВЫВОД СПИСКА МАРШРУТОВ ЧЕРЕЗ map
    print_separator("Финальный вывод: все маршруты в коллекции")

    all_routes = bus_collection.map(lambda bus: bus.route)
    print(f"Все маршруты: {all_routes}")


if __name__ == "__main__":
    main()