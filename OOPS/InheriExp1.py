# # Define the base class Vehicle
# class Vehicle:
#     def __init__(self, make, model):
#         self.make = make
#         self.model = model

#     def display_vehicle_info(self):
#         print(f"Make: {self.make}")
#         print(f"Model: {self.model}")

# # Define the base class Insurance
# class Insurance:
#     def __init__(self, insurance_provider, insurance_expiry):
#         self.insurance_provider = insurance_provider
#         self.insurance_expiry = insurance_expiry

#     def display_insurance_info(self):
#         print(f"Insurance Provider: {self.insurance_provider}")
#         print(f"Insurance Expiry: {self.insurance_expiry}")

# # Define the derived class Car that inherits from both Vehicle and Insurance
# class Car(Vehicle, Insurance):
#     def __init__(self, make, model, car_id, insurance_provider, insurance_expiry):
#         Vehicle.__init__(self, make, model)  # Call the constructor of the Vehicle class
#         Insurance.__init__(self, insurance_provider, insurance_expiry)  # Call the constructor of the Insurance class
#         self.car_id = car_id

#     def display_car_info(self):
#         self.display_vehicle_info()  # Use the base class method to display make and model
#         print(f"Car ID: {self.car_id}")
#         self.display_insurance_info()  # Use the Insurance method to display insurance details

# # Get user input for make, model, car ID, insurance provider, and insurance expiry
# the_make = input()
# the_model = input()
# the_car_id = input()
# the_insurance_provider = input()
# the_insurance_expiry = input()

# # Create an instance of the Car class
# car_1 = Car(the_make, the_model, the_car_id, the_insurance_provider, the_insurance_expiry)

# # Display the car's information
# car_1.display_car_info()


def calculateTotalTime():
    total_time=0
    load=0
    input2 = [26,1,5]
    for w in input2:
        if(w >= 5 and w <= 50):
            load+=w
        if load>50:
            load = 0
        total_time += 5*load
    return total_time

print(calculateTotalTime())