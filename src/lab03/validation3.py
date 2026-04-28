

VALID_STATUSES = ('parked', 'on_route')

def validate_route(value):
    """Проверяет, что номер маршрута — непустая строка."""
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Номер маршрута должен быть непустой строкой")

def validate_capacity(value):
    """Проверяет, что вместимость — положительное целое число."""
    if not isinstance(value, int) or value <= 0:
        raise ValueError("Вместимость должна быть положительным целым числом")

def validate_passengers(value, capacity=None):
    """
    Проверяет количество пассажиров:
    - целое неотрицательное;
    - если передана capacity, то не превышает её.
    """
    if not isinstance(value, int) or value < 0:
        raise ValueError("Число пассажиров должно быть целым и ≥ 0")
    if capacity is not None and value > capacity:
        raise ValueError(f"Пассажиров не может быть больше вместимости ({capacity})")

def validate_status(value):
    """Проверяет, что статус входит в список допустимых."""
    if value not in VALID_STATUSES:
        raise ValueError(f"Статус должен быть одним из {VALID_STATUSES}")

def validate_route_type(value):
    """Проверяет, что тип маршрута — непустая строка."""
    if not isinstance(value, str) or not value.strip():
        raise ValueError("Тип маршрута должен быть непустой строкой")

def validate_comfort_level(value):
    """Проверяет, что уровень комфорта — целое число от 1 до 5."""
    if not isinstance(value, int) or value < 1 or value > 5:
        raise ValueError("Уровень комфорта должен быть целым числом от 1 до 5")