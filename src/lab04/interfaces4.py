from abc import ABC, abstractmethod

class Printable(ABC):
    """Интерфейс для объектов, которые могут быть выведены в удобном формате."""
    
    @abstractmethod
    def to_string(self):
        """Возвращает строковое представление объекта."""
        pass


class Comparable(ABC):
    """Интерфейс для объектов, которые можно сравнивать."""
    
    @abstractmethod
    def compare_to(self, other):
        """
        Сравнивает текущий объект с другим.
        Возвращает:
        - отрицательное число, если self < other
        - 0, если self == other
        - положительное число, если self > other
        """
        pass


class PriceCalculable(ABC):
    """Интерфейс для объектов, у которых можно рассчитать стоимость поездки."""
    
    @abstractmethod
    def calculate_price(self, distance_km):
        """Рассчитывает стоимость поездки на заданное расстояние."""
        pass