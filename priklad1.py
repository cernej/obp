from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self, color):
        self.color = color
    
    @abstractmethod
    def consumption(self):
        pass

    def info(self):
        return f"Car color: {self.color}"


class CombustionCor(Car):
    def __init__(self, color, fuel_consumption):
        super().__init__(color)
        self.fuel_consumption = fuel_consumption
    
    def consumption(self):
        return f"Consumption: {self.fuel_consumption} l/100km"


class ElectricCar(Car):
    def __init__(self, color, energy_consumption):
        super().__init__(color)
        self.energy_consumption = energy_consumption
    
    def consumption(self):
        return f"Consumption: {self.energy_consumption} kWh/100km"


if __name__ == "__main__":
    car = CombustionCor('blue', 10)
    print(car.consumption())