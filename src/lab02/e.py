from model2 import Bus
from collection import BusFleet

b1 = Bus('111', 40, 3, "parked")
b2 = Bus('112', 30, 5, "parked")

fleet = BusFleet()
fleet.add(b1)
fleet.add(b2)

fleet.sort_by_route(reverse=True)
print(fleet) 