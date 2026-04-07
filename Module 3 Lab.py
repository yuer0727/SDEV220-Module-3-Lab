
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        
        super().__init__(vehicle_type)
        
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

def main():
    print("Welcome to the Automobile Tracker App!")
    print("-" * 30)
    
    
    v_type = "car"
    
    
    car_year = input("Please enter the year of the car: ")
    car_make = input("Please enter the make of the car (e.g., Toyota): ")
    car_model = input("Please enter the model of the car (e.g., Corolla): ")
    car_doors = input("Please enter the number of doors (2 or 4): ")
    car_roof = input("Please enter the type of roof (solid or sun roof): ")
    
   
    my_car = Automobile(v_type, car_year, car_make, car_model, car_doors, car_roof)
    
    
    print("\nHere is the information you entered:")
    print(f"Vehicle type: {my_car.vehicle_type}")
    print(f"Year: {my_car.year}")
    print(f"Make: {my_car.make}")
    print(f"Model: {my_car.model}")
    print(f"Number of doors: {my_car.doors}")
    print(f"Type of roof: {my_car.roof}")

if __name__ == "__main__":
    main()