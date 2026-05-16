# exceptions.py
"""Собственные исключения для приложения."""


class ItemNotFoundError(Exception):
    """Объект не найден в коллекции."""
    pass


class DuplicateItemError(Exception):
    """Объект с таким идентификатором уже существует."""
    pass


class InvalidInputError(Exception):
    """Некорректный ввод пользователя."""
    pass