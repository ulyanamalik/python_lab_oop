# main.py
"""Точка входа в приложение."""

from app7 import BusApp
from cli7 import CLI
from storage7 import load, save


def main() -> None:
    """Запуск приложения."""
    # Загрузка данных из файла
    loaded_buses = load("data.json")
    
    # Создание приложения и загрузка данных
    app = BusApp()
    app.load_initial_data(loaded_buses)
    
    # Запуск CLI
    cli = CLI(app)
    cli.run()
    
    # Сохранение данных при выходе
    save(app.get_all_buses(), "data.json")
    print("Данные сохранены в файл data.json")


if __name__ == "__main__":
    main()