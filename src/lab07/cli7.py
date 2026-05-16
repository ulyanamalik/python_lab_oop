# cli.py
"""Консольный интерфейс пользователя."""

from typing import Optional
from models7 import Bus, CityBus, TouristBus
from app7 import BusApp
from exceptions7 import DuplicateItemError, ItemNotFoundError, InvalidInputError


class CLI:
    """Консольное меню приложения."""

    def __init__(self, app: BusApp) -> None:
        self.app: BusApp = app

    def run(self) -> None:
        """Запуск основного цикла приложения."""
        self._print_welcome()
        while True:
            self._print_menu()
            choice = self._get_choice()
            if choice == 0:
                self._exit_app()
                break
            self._execute_choice(choice)

    def _print_welcome(self) -> None:
        print(r"""
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║     █████╗ ██╗   ██╗████████╗ ██████╗ ██████╗  █████╗ ██████╗ ██╗  ██╗
    ║    ██╔══██╗██║   ██║╚══██╔══╝██╔═══██╗██╔══██╗██╔══██╗██╔══██╗██║ ██╔╝
    ║    ███████║██║   ██║   ██║   ██║   ██║██████╔╝███████║██████╔╝█████╔╝ 
    ║    ██╔══██║██║   ██║   ██║   ██║   ██║██╔═══╝ ██╔══██║██╔══██╗██╔═██╗ 
    ║    ██║  ██║╚██████╔╝   ██║   ╚██████╔╝██║     ██║  ██║██║  ██║██║  ██╗
    ║    ╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚═════╝ ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝
    ║                                                              ║
    ║                   СИСТЕМА УПРАВЛЕНИЯ АВТОПАРКОМ                 ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
         """)
        print("  Добро пожаловать! Выберите действие из меню ниже.\n")

    def _print_menu(self) -> None:
        print("\n" + "-" * 40)
        print("ГЛАВНОЕ МЕНЮ")
        print("-" * 40)
        print("1. Показать все автобусы")
        print("2. Добавить автобус")
        print("3. Найти автобус по маршруту")
        print("4. Удалить автобус")
        print("5. Отправить автобус на маршрут")
        print("6. Посадить пассажиров")
        print("7. Высадить пассажиров")
        print("8. Фильтрация автобусов")
        print("9. Сортировка автобусов")
        print("10. Статистика")
        print("0. Выход")
        print("-" * 40)

    def _get_choice(self) -> int:
        try:
            return int(input("\nВыберите пункт меню: "))
        except ValueError:
            print("Ошибка: введите число от 0 до 10")
            return -1

    def _execute_choice(self, choice: int) -> None:
        if choice == 1:
            self._show_all_buses()
        elif choice == 2:
            self._add_bus()
        elif choice == 3:
            self._find_bus()
        elif choice == 4:
            self._delete_bus()
        elif choice == 5:
            self._start_route()
        elif choice == 6:
            self._board_passengers()
        elif choice == 7:
            self._alight_passengers()
        elif choice == 8:
            self._filter_menu()
        elif choice == 9:
            self._sort_menu()
        elif choice == 10:
            self._show_statistics()
        elif choice == -1:
            pass
        else:
            print("Ошибка: неверный пункт меню")

    def _show_all_buses(self) -> None:
        """Показывает все автобусы в виде таблицы."""
        buses = self.app.get_all_buses()
        if not buses:
            print("\n Автобусов нет в автопарке.")
            return
        
        print("\n" + "=" * 80)
        print("СПИСОК АВТОБУСОВ")
        print("=" * 80)
        print(f"{'N':<3} {'Маршрут':<8} {'Вместимость':<12} {'Пассажиры':<10} {'Статус':<12} {'Тип':<15}")
        print("-" * 80)
        for i, bus in enumerate(buses, 1):
            bus_type = bus.__class__.__name__
            print(f"{i:<3} {bus.route:<8} {bus.capacity:<12} {bus.passengers:<10} {bus.status:<12} {bus_type:<15}")
        print("=" * 80)

    def _add_bus(self) -> None:
        """Добавление нового автобуса с выбором типа."""
        print("\n--- ДОБАВЛЕНИЕ АВТОБУСА ---")
        
        print("Выберите тип автобуса:")
        print("1. Обычный")
        print("2. Городской")
        print("3. Туристический")
        
        try:
            type_choice = int(input("Ваш выбор: "))
            if type_choice not in [1, 2, 3]:
                raise InvalidInputError("Неверный тип")
        except ValueError:
            print("Ошибка: введите число")
            return
        except InvalidInputError as e:
            print(f"Ошибка: {e}")
            return

        try:
            route = input("Номер маршрута: ").strip()
            if not route:
                raise InvalidInputError("Маршрут не может быть пустым")
            
            capacity = int(input("Вместимость: "))
            if capacity <= 0:
                raise InvalidInputError("Вместимость должна быть положительной")
            
            passengers = int(input("Количество пассажиров (0): ") or "0")
            if passengers < 0:
                raise InvalidInputError("Пассажиры не могут быть отрицательными")
            if passengers > capacity:
                raise InvalidInputError(f"Пассажиров ({passengers}) не может быть больше вместимости ({capacity})")
            
            status = input("Статус (parked/on_route) [parked]: ").strip() or "parked"
            if status not in ['parked', 'on_route']:
                raise InvalidInputError("Статус должен быть 'parked' или 'on_route'")

            if type_choice == 1:
                bus = Bus(route, capacity, passengers, status)
            elif type_choice == 2:
                route_type = input("Тип маршрута (городской/пригородный): ").strip()
                has_ac = input("Наличие кондиционера (да/нет): ").strip().lower() == 'да'
                bus = CityBus(route, capacity, passengers, status, route_type, has_ac)
            else:
                has_toilet = input("Наличие туалета (да/нет): ").strip().lower() == 'да'
                comfort = int(input("Уровень комфорта (1-5): "))
                bus = TouristBus(route, capacity, passengers, status, has_toilet, comfort)

            self.app.add_bus(bus)
            print(f"Автобус {route} успешно добавлен!")

        except ValueError as e:
            print(f"Ошибка ввода числа: {e}")
        except InvalidInputError as e:
            print(f"Ошибка: {e}")
        except DuplicateItemError as e:
            print(f"Ошибка: {e}")

    def _find_bus(self) -> None:
        """Поиск автобуса по маршруту."""
        route = input("\nВведите номер маршрута для поиска: ").strip()
        bus = self.app.find_bus_by_route(route)
        if bus:
            print("\n" + "=" * 50)
            print("Найден автобус:")
            print(f"   {bus.display()}")
            print("=" * 50)
        else:
            print(f"Автобус с маршрутом {route} не найден")

    def _delete_bus(self) -> None:
        """Удаление автобуса с подтверждением."""
        route = input("\nВведите номер маршрута для удаления: ").strip()
        bus = self.app.find_bus_by_route(route)
        if bus is None:
            print(f"Автобус с маршрутом {route} не найден")
            return

        print(f"\nАвтобус для удаления: {bus.display()}")
        confirm = input("Удалить этот автобус? (y/n): ").strip().lower()
        if confirm == 'y':
            try:
                self.app.remove_bus_by_route(route)
                print(f"Автобус {route} удалён")
            except ItemNotFoundError as e:
                print(f"Ошибка: {e}")
        else:
            print("Удаление отменено")

    def _start_route(self) -> None:
        """Отправка автобуса на маршрут."""
        route = input("\nВведите номер маршрута: ").strip()
        try:
            self.app.start_route(route)
            print(f"Автобус {route} выехал на маршрут")
        except ItemNotFoundError as e:
            print(f"Ошибка: {e}")
        except ValueError as e:
            print(f"Ошибка: {e}")

    def _board_passengers(self) -> None:
        """Посадка пассажиров."""
        route = input("\nВведите номер маршрута: ").strip()
        try:
            num = int(input("Количество пассажиров для посадки: "))
            self.app.board_passengers(route, num)
            print(f"Посажено {num} пассажиров в автобус {route}")
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
        except ItemNotFoundError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Ошибка: {e}")

    def _alight_passengers(self) -> None:
        """Высадка пассажиров."""
        route = input("\nВведите номер маршрута: ").strip()
        try:
            num = int(input("Количество пассажиров для высадки: "))
            self.app.alight_passengers(route, num)
            print(f"Высажено {num} пассажиров из автобуса {route}")
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
        except ItemNotFoundError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Ошибка: {e}")

    def _filter_menu(self) -> None:
        """Меню фильтрации автобусов."""
        print("\n--- ФИЛЬТРАЦИЯ АВТОБУСОВ ---")
        print("1. По статусу (на маршруте)")
        print("2. По статусу (в парке)")
        print("3. С пассажирами")
        
        try:
            choice = int(input("Ваш выбор: "))
            if choice == 1:
                buses = self.app.find_buses_by_status('on_route')
                print(f"\nАвтобусы на маршруте ({len(buses)}):")
            elif choice == 2:
                buses = self.app.find_buses_by_status('parked')
                print(f"\nАвтобусы в парке ({len(buses)}):")
            elif choice == 3:
                buses = self.app.find_buses_with_passengers()
                print(f"\nАвтобусы с пассажирами ({len(buses)}):")
            else:
                print("Неверный выбор")
                return
            
            if not buses:
                print("  Нет автобусов")
            for bus in buses:
                print(f"  - {bus.display()}")
        except ValueError:
            print("Ошибка: введите число")

    def _sort_menu(self) -> None:
        """Меню сортировки автобусов."""
        print("\n--- СОРТИРОВКА АВТОБУСОВ ---")
        print("1. По маршруту")
        print("2. По вместимости (от меньшей к большей)")
        print("3. По количеству пассажиров")
        
        try:
            choice = int(input("Ваш выбор: "))
            if choice == 1:
                self.app.sort_buses_by_route()
                print("Отсортировано по маршруту")
            elif choice == 2:
                self.app.sort_buses_by_capacity()
                print("Отсортировано по вместимости")
            elif choice == 3:
                self.app.sort_buses_by_passengers()
                print("Отсортировано по пассажирам")
            else:
                print("Неверный выбор")
                return
            self._show_all_buses()
        except ValueError:
            print("Ошибка: введите число")

    def _show_statistics(self) -> None:
        """Показывает статистику."""
        stats = self.app.get_statistics()
        print("\n" + "=" * 50)
        print("СТАТИСТИКА АВТОПАРКА")
        print("=" * 50)
        print(f"Всего автобусов:      {stats['total']}")
        print(f"На маршруте:          {stats['on_route']}")
        print(f"В парке:              {stats['parked']}")
        print(f"С пассажирами:        {stats['with_passengers']}")
        print(f"Всего пассажиров:     {stats['total_passengers']}")
        print("=" * 50)

    def _exit_app(self) -> None:
        print("\n" + "=" * 60)
        print("До свидания! Спасибо за использование приложения!")
        print("=" * 60)    
        print("\nДанные сохранены. До скорой встречи!")