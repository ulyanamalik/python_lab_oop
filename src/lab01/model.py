class Bus:
    total_buses = 0                     # атрибут класса
    VALID_STATUSES = ('parked', 'on_route')

    def __init__(self, route, capacity, passengers=0, status='parked'):
        # Валидация входных данных через отдельные методы
        self._validate_route(route)
        self._validate_capacity(capacity)
        self._validate_passengers(passengers, capacity)
        self._validate_status(status)

        self._route = route
        self._capacity = capacity
        self._passengers = passengers
        self._status = status

        Bus.total_buses += 1

    # ---------- Методы валидации ----------
    def _validate_route(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("Номер маршрута должен быть непустой строкой")

    def _validate_capacity(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Вместимость должна быть положительным целым числом")

    def _validate_passengers(self, value, capacity=None):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Число пассажиров должно быть целым и ≥ 0")
        if capacity is not None and value > capacity:
            raise ValueError(f"Пассажиров не может быть больше вместимости ({capacity})")

    def _validate_status(self, value):
        if value not in Bus.VALID_STATUSES:
            raise ValueError(f"Статус должен быть одним из {Bus.VALID_STATUSES}")

    # ---------- Свойства ----------
    @property
    def route(self):
        return self._route

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        self._validate_capacity(value)
        self._capacity = value

    @property
    def passengers(self):
        return self._passengers

    @passengers.setter
    def passengers(self, value):
        self._validate_passengers(value, self._capacity)
        self._passengers = value

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        self._validate_status(value)
        self._status = value

    # ---------- Бизнес-методы ----------
    def board(self, num):
        """Посадка пассажиров (только на маршруте)."""
        if self.status != 'on_route':
            raise ValueError("Посадка возможна только на маршруте")
        if num <= 0:
            raise ValueError("Число входящих должно быть положительным")
        if self.passengers + num > self.capacity:
            raise ValueError(f"Не хватает мест, свободно {self.capacity - self.passengers}")
        self._passengers += num

    def alight(self, num):
        """Высадка пассажиров."""
        if num <= 0:
            raise ValueError("Число выходящих должно быть положительным")
        if self.passengers < num:
            raise ValueError(f"В автобусе только {self.passengers} пассажиров")
        self._passengers -= num

    def start_route(self):
        """Выехать на маршрут (из парка)."""
        if self.status != 'parked':
            raise ValueError("Автобус уже не в парке")
        self._status = 'on_route'

    def park(self):
        """Вернуться в парк (без пассажиров)."""
        if self.status != 'on_route':
            raise ValueError("Автобус не на маршруте")
        if self.passengers != 0:
            raise ValueError("Нельзя парковаться с пассажирами")
        self._status = 'parked'

    # ---------- Магические методы ----------
    def __str__(self):
        return f"Автобус {self.route}: {self.passengers}/{self.capacity} пасс., статус: {self.status}"

    def __repr__(self):
        return f"Bus('{self.route}', {self.capacity}, {self.passengers}, '{self.status}')"

    def __eq__(self, other):
        if not isinstance(other, Bus):
            return NotImplemented
        return self.route == other.route