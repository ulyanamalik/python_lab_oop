from model import Bus

def main():
    # Атрибут класса до создания объектов
    print("Всего автобусов:", Bus.total_buses)

    # Создание автобусов
    b1 = Bus("101", 50, 10, "on_route")
    b2 = Bus("102", 60)                # по умолчанию статус parked
    b3 = Bus("101", 40)                 # тот же маршрут

    print("\n--- Объекты ---")
    print("b1:", b1)
    print("b2:", repr(b2))
    print("b3:", b3)

    print("\n--- Сравнение ---")
    print("b1 == b2?", b1 == b2)
    print("b1 == b3?", b1 == b3)        # одинаковый маршрут

    print("\n--- Атрибут класса ---")
    print("Bus.total_buses =", Bus.total_buses)
    print("Через экземпляр b1.total_buses =", b1.total_buses)

    print("\n--- Изменение свойств (setter) ---")
    print("Старая вместимость b1:", b1.capacity)
    b1.capacity = 45
    print("Новая вместимость:", b1.capacity)

    try:
        b1.capacity = -10
    except ValueError as e:
        print("Ошибка при отрицательной вместимости:", e)

    try:
        b1.status = "flying"
    except ValueError as e:
        print("Ошибка при неверном статусе:", e)

    print("\n--- Бизнес-методы и состояния ---")
    # b1 уже на маршруте
    print("b1:", b1)
    b1.board(5)
    print("После посадки 5:", b1)
    b1.alight(3)
    print("После высадки 3:", b1)

    # Попытка посадить слишком много
    try:
        b1.board(100)
    except ValueError as e:
        print("Ошибка при посадке 100:", e)

    # b2 в парке – нельзя сажать
    print("\nb2 (в парке):", b2)
    try:
        b2.board(1)
    except ValueError as e:
        print("Ошибка посадки в парке:", e)

    # Отправляем b2 на маршрут
    b2.start_route()
    print("b2 после выезда на маршрут:", b2)
    b2.board(20)
    print("Посадили 20:", b2)

    # Пытаемся поставить в парк с пассажирами
    try:
        b2.park()
    except ValueError as e:
        print("Ошибка парковки с пассажирами:", e)

    # Высаживаем и паркуем
    b2.alight(b2.passengers)
    b2.park()
    print("После высадки и парковки:", b2)

    print("\n--- Некорректное создание ---")
    cases = [
        ("", 50, 0, "parked"),       # пустой маршрут
        ("103", -5, 0, "parked"),    # отрицательная вместимость
        ("104", 30, -1, "parked"),   # отрицательные пассажиры
        ("105", 30, 40, "parked"),   # пассажиров больше вместимости
        ("106", 30, 0, "broken"),    # неверный статус
    ]
    for r, cap, p, st in cases:
        try:
            Bus(r, cap, p, st)
            print(f"Неожиданно создан: {r}")
        except ValueError as e:
            print(f"Ошибка ({r}): {e}")

if __name__ == "__main__":
    main()