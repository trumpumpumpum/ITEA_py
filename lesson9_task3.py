class Car:

    def __init__(self, model, engine_type, max_spped, weight, fuel_type):
        self.model = model
        self.engine_type = engine_type
        self.max_speed = max_spped
        self.weight = weight
        self.fuel_type = fuel_type


    def move(self):
        print(f'The car {self.model} is moving')

    def stop_engine(self):
        print(f'The car {self.model} has been stopped')

    def get_max_speed(self):
        print(f'Max speed is {self.max_speed}')

    def get_weight(self):
        print(f'The car {self.model} weight is {self.weight}t')

    def get_fuel_type(self):
        print(f'The car {self.model} fuel type is {self.fuel_type}')


class Truck(Car):

    def offload(self):
        print('The items are being offloaded')

    def refrigerator(self):
        print(f'The car {self.model} has a refrigerator')


car = Truck('MAN', 'V-12', 140, 10, 'Diesel')
car.move()
car.offload()
car.get_max_speed()
car.get_weight()
car.get_fuel_type()
car.refrigerator()

print('*' * 20)

car2 = Car('bmw', 'v-8', 260, 2, 'Gasoline')
car2.move()
car2.stop_engine()
car2.get_max_speed()
car2.get_weight()
car2.get_fuel_type()






