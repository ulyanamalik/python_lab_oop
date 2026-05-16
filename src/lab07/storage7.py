# storage.py
"""Сохранение и загрузка данных в JSON."""

import json
from typing import List
from models7 import Bus, CityBus, TouristBus


def save(collection: List[Bus], filepath: str = "data.json") -> None:
    """
    Сохраняет коллекцию автобусов в JSON-файл.
    
    Args:
        collection: список автобусов
        filepath: путь к файлу
    """
    data = [bus.to_dict() for bus in collection]
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load(filepath: str = "data.json") -> List[Bus]:
    """
    Загружает коллекцию автобусов из JSON-файла.
    
    Args:
        filepath: путь к файлу
        
    Returns:
        список автобусов
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        buses = []
        for item in data:
            bus_type = item.get('type', 'bus')
            if bus_type == 'city':
                buses.append(CityBus.from_dict(item))
            elif bus_type == 'tourist':
                buses.append(TouristBus.from_dict(item))
            else:
                buses.append(Bus.from_dict(item))
        return buses
    except FileNotFoundError:
        return []