# Лабораторная работа №4: Интерфейсы и абстрактные классы (ABC).Вариант 5.
## Цель работы

Познакомиться с абстрактными базовыми классами (ABC), 

освоить понятие интерфейса (контракта поведения), 

научиться задавать обязательные методы для классов и закрепить полиморфизм через единый интерфейс.

### 1. `Printable`
Интерфейс для объектов, которые могут быть выведены в удобном формате.

| Метод | Описание |
|-------|----------|
| `to_string()` | Возвращает строковое представление объекта |

### 2. `Comparable`
Интерфейс для объектов, которые можно сравнивать между собой.

| Метод | Описание |
|-------|----------|
| `compare_to(other)` | Сравнивает текущий объект с другим. Возвращает отрицательное число (self < other), 0 (self == other) или положительное число (self > other) |

### 3. `PriceCalculable`
Интерфейс для объектов, у которых можно рассчитать стоимость поездки.

| Метод | Описание |
|-------|----------|
| `calculate_price(distance_km)` | Рассчитывает стоимость поездки на заданное расстояние |

## Реализация интерфейсов в классах

| Класс | Printable | Comparable | PriceCalculable |
|-------|-----------|------------|-----------------|
| `Bus` | `to_string()` | `compare_to()` | `calculate_price()` (×20) |
| `CityBus` | переопределён | наследует | переопределён (×15) |
| `TouristBus` | переопределён | наследует | переопределён (×35) |



### Сценарий 1: Создание объектов разных типов
Создаются обычный, городской и туристический автобусы. Вызывается метод `to_string()` для каждого.

<img width="1398" height="238" alt="image" src="https://github.com/user-attachments/assets/48af6070-0b10-42c2-8412-bfa8c16f9e9f" />


### Сценарий 2: Проверка реализации интерфейсов через `isinstance()`
Проверяется, что каждый объект реализует нужные интерфейсы.

<img width="1066" height="374" alt="image" src="https://github.com/user-attachments/assets/e36a8911-9794-406a-b134-e205e8e99dbe" />




### Сценарий 3: Универсальная функция `print_all_printable()`
Функция принимает список объектов с интерфейсом `Printable` и выводит их через `to_string()`.

<img width="1400" height="242" alt="image" src="https://github.com/user-attachments/assets/efcdd5c4-2005-4323-bdea-86e67c59513a" />


### Сценарий 4: Сравнение через интерфейс `Comparable`
Функция `compare_buses()` сравнивает два автобуса через метод `compare_to()`.

<img width="754" height="222" alt="image" src="https://github.com/user-attachments/assets/9e775167-8b3f-4b50-bed2-277f04d38f1a" />


### Сценарий 5: Полиморфизм через интерфейс `PriceCalculable`
Для разных автобусов вызывается `calculate_price(100)`. Результат различается в зависимости от типа.

<img width="842" height="206" alt="image" src="https://github.com/user-attachments/assets/939e485d-4863-49fd-8d07-7875366b7b5c" />


### Сценарий 6: Коллекция и добавление объектов
Автобусы добавляются в `BusFleet`. Выводится количество элементов.

<img width="654" height="302" alt="image" src="https://github.com/user-attachments/assets/af925f7a-b3e2-4d4f-853d-100669a09c2a" />


### Сценарий 7: Фильтрация коллекции по интерфейсу
- `get_printable()` – возвращает объекты с интерфейсом `Printable`
- `get_price_calculable()` – возвращает объекты с интерфейсом `PriceCalculable`

<img width="1410" height="460" alt="image" src="https://github.com/user-attachments/assets/866c3269-cb54-4535-9d6b-c021ff9200c0" />


### Сценарий 8: Сортировка коллекции
Сортировка автобусов по номеру маршрута.

<img width="606" height="222" alt="image" src="https://github.com/user-attachments/assets/46e7072c-a2a3-464c-901d-243ab4aa755c" />


### Сценарий 9: Полиморфизм без условий
Единый вызов `to_string()` для разных объектов даёт разные представления.

<img width="1426" height="248" alt="image" src="https://github.com/user-attachments/assets/ab6e25ef-dee6-42c5-bc88-5d2b14398cb6" />


### Сценарий 10: Демонстрация валидации
Проверка обработки ошибок при создании объектов с некорректными данными.

<img width="992" height="180" alt="image" src="https://github.com/user-attachments/assets/1874bac8-a5af-4041-a3b7-8bc78e47a529" />



