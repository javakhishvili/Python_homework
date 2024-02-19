


# 1. დაწერეთ პითონის Car (ატრიბუტები: brand, model, year) კლასი და მოახდინეთ ამ კლასისთვის __new__ და __init__ მეთოდის გადაფარვა.


# class Car:
#     def __new__(cls, *args, **kwargs):
#         print("Creating a new instance of Car")
#         instance = super().__new__(cls)
#         return instance

#     def __init__(self, make, model, year):
#         print("Initializing Car instance")
#         self.make = make
#         self.model = model
#         self.year = year


# my_car = Car("Toyota", "Camry", 2022)
# print(my_car.make)  
# print(my_car.model)  
# print(my_car.year)   



#-------------------------------------------------------------------------------------


# 2. Car კლასს დაუმატეთ თითეული ატრიბუტისთვის set და get ფუნქციები მათი ცვლილებებისთვის.

# class Car:
#     def __init__(self, make, model, year):
#         self._make = make
#         self._model = model
#         self._year = year

#     def set_make(self, make):
#         self._make = make

#     def get_make(self):
#         return self._make

#     def set_model(self, model):
#         self._model = model

#     def get_model(self):
#         return self._model

#     def set_year(self, year):
#         self._year = year

#     def get_year(self):
#         return self._year


# my_car = Car("Toyota", "Camry", 2022)
# print(my_car.get_make())  
# print(my_car.get_model()) 
# print(my_car.get_year())   


# my_car.set_make("Honda")
# my_car.set_year(2023)
# print(my_car.get_make())   
# print(my_car.get_year())  


#-------------------------------------------------------------------------------------


# 3. დაამატეთ Car კლასის set ფუნქციებში, ვალიდაციები თითოეული ატრიბუტისთვის, მაგალითად year ატრიბუტი რომ იყოს ყოველთვის ინტეგერი და ასე შემდეგ.

# class Car:
#     def __init__(self, make, model, year):
#         self._make = make
#         self._model = model
#         self._year = year

#     def set_make(self, make):
#         if isinstance(make, str):
#             self._make = make
#         else:
#             print("Error: Make must be a string.")

#     def get_make(self):
#         return self._make

#     def set_model(self, model):
#         if isinstance(model, str):
#             self._model = model
#         else:
#             print("Error: Model must be a string.")

#     def get_model(self):
#         return self._model

#     def set_year(self, year):
#         if isinstance(year, int):
#             self._year = year
#         else:
#             print("Error: Year must be an integer.")

#     def get_year(self):
#         return self._year


# my_car = Car("Toyota", "Camry", 2022)
# print(my_car.get_make())  
# print(my_car.get_model()) 
# print(my_car.get_year())   


# my_car.set_make(123)  
# my_car.set_year("2023")


# my_car.set_make("Honda")
# my_car.set_year(2023)
# print(my_car.get_make())   








