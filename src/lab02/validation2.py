
VALID_STATUSES = ('parked', 'on_route')

def validate_route(value):

    if not isinstance(value, str) or not value.strip():
        raise ValueError("Номер маршрута должен быть непустой строкой")

def validate_capacity(value):

    if not isinstance(value, int) or value <= 0:
        raise ValueError("Вместимость должна быть положительным целым числом")

def validate_passengers(value, capacity=None):

    if not isinstance(value, int) or value < 0:
        raise ValueError("Число пассажиров должно быть целым и ≥ 0")
    if capacity is not None and value > capacity:
        raise ValueError(f"Пассажиров не может быть больше вместимости ({capacity})")

def validate_status(value):

    if value not in VALID_STATUSES:
        raise ValueError(f"Статус должен быть одним из {VALID_STATUSES}")