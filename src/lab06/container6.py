# container.py
"""Generic-коллекция, TypeVar и Protocol для лабораторной работы №6."""

from typing import TypeVar, Generic, Callable, Optional, List, Iterator
from typing import Protocol


#ПРОТОКОЛЫ

class Displayable(Protocol):
    """Протокол для объектов, которые можно отобразить."""
    def display(self) -> str:
        ...


class Scorable(Protocol):
    """Протокол для объектов, которые имеют оценку/рейтинг."""
    def score(self) -> float:
        ...


#TypeVar

T = TypeVar('T')                      # Базовый TypeVar без ограничений
R = TypeVar('R')                      # Для map (результат может быть другого типа)

D = TypeVar('D', bound=Displayable)   # Только объекты с методом display()
S = TypeVar('S', bound=Scorable)      # Только объекты с методом score()


#GENERIC КОЛЛЕКЦИЯ

class TypedCollection(Generic[T]):
    """
    Generic-версия коллекции из ЛР-2.
    Хранит объекты типа T.
    """

    def __init__(self) -> None:
        self._items: List[T] = []

    #Базовые операции
    def add(self, item: T) -> None:
        """Добавляет элемент в коллекцию."""
        self._items.append(item)

    def remove(self, item: T) -> None:
        """Удаляет элемент из коллекции (по объекту)."""
        self._items.remove(item)

    def get_all(self) -> List[T]:
        """Возвращает копию списка всех элементов."""
        return self._items.copy()

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self) -> Iterator[T]:
        return iter(self._items)

    def __getitem__(self, index: int) -> T:
        return self._items[index]

    def __str__(self) -> str:
        return f"TypedCollection with {len(self)} items"

    # Новые методы
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        """
        Находит первый элемент, удовлетворяющий условию.
        Возвращает элемент или None.
        """
        for item in self._items:
            if predicate(item):
                return item
        return None

    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        """
        Возвращает список всех элементов, удовлетворяющих условию.
        """
        return [item for item in self._items if predicate(item)]

    def map(self, transform: Callable[[T], R]) -> List[R]:
        """
        Применяет функцию преобразования ко всем элементам.
        Возвращает список результатов (тип может отличаться).
        """
        return [transform(item) for item in self._items]


#СПЕЦИАЛИЗИРОВАННЫЕ КОЛЛЕКЦИИ

class DisplayableCollection(TypedCollection[D]):
    """
    Коллекция для объектов, реализующих протокол Displayable.
    Демонстрирует ограничение TypeVar через bound.
    """
    pass


class ScorableCollection(TypedCollection[S]):
    """
    Коллекция для объектов, реализующих протокол Scorable.
    Демонстрирует ограничение TypeVar через bound.
    """
    pass