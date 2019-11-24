class Vehicle:
    def __init__(self):
        self.__saya = "ok"
    def vehicle_method(self):
        print("Halo saya induknya class")
    
    def __coba_p_method(self):
        return "saya private"
    
    def _coba_pp_method(self):
        return "saya protected"
    

    def get_saya(self):
        return self.__saya
    
    def cal_coba_p_method(self):
        return self.__coba_p_method()


# Car adalah turunan (child) dari Vehicle
class Car(Vehicle):
    def car_method(self):
        print("Saya turunannya class Vehicle, dipanggil dari method car_method pada class Car")

# sama sepeerti car, Cycle juga turunan dari Vehicle
class Cycle(Vehicle):
    def cycle_method(self):
        print("Saya turunannya class Vehicle, dipanggil dari method cycle_method pada class Cycle")

cycle = Cycle()
cycle.vehicle_method()
# cycle.__coba_p_method()
cycle.cycle_method()
print(cycle._coba_pp_method())

v = Vehicle()
print(v.get_saya())
print(v.cal_coba_p_method())
# v.__coba_p_method()