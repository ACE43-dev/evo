# # # parent class
# # class Person:
# #     def __init__(self,name,age:int,nature):
# #         self.name = name
# #         self.age = age 
# #         self.nature = nature
    
# #     def showNature(self):
# #         print(self.nature)
       
# # #child class
# # class Student(Person):
# #     def __init__(self,age,name,nature,standard):
# #         Person.__init__(self,age,name,nature)
# #         # super().__init__(age,name,nature)#By using the super() function, you do not have to use the name of the parent element, 
# #         #it will automatically inherit the methods and properties from its parent.
# #         self.standard = standard
    
# #     def showStd(self):
# #         print(self.standard)

        
        

# # p1 = Person("himayu",18,"idk")
# # p1.showNature()
# # s1 = Student('Himayu',18,'idk',"2nd")
# # s1.showStd()

# # #polymorphism means many form 
# # #example of function polymorphism is len()

# # #example of class polymorphism
# # # class Car:
# # #   def __init__(self, brand, model):
# # #     self.brand = brand
# # #     self.model = model

# # #   def move(self):
# # #     print("Drive!")

# # # class Boat:
# # #   def __init__(self, brand, model):
# # #     self.brand = brand
# # #     self.model = model

# # #   def move(self):
# # #     print("Sail!")

# # # class Plane:
# # #   def __init__(self, brand, model):
# # #     self.brand = brand
# # #     self.model = model

# # #   def move(self):
# # #     print("Fly!")

# # # car1 = Car("Ford", "Mustang")       #Create a Car object
# # # boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# # # plane1 = Plane("Boeing", "747")     #Create a Plane object

# # # for x in (car1, boat1, plane1):
# # #   x.move()

# class Car:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model
#     self.engine = self.Engine()

#   class Engine:
#     def __init__(self):
#       self.status = "Off"

#     def start(self):
#       self.status = "Running"
#       print("Engine started")

#     def stop(self):
#       self.status = "Off"
#       print("Engine stopped")

#   def drive(self):
#     if self.engine.status == "Running":
#       print(f"Driving the {self.brand} {self.model}")
#     else:
#       print("Start the engine first!")

# car = Car("Toyota", "Corolla")
# car.drive()
# car.engine.start()
# car.drive()
# print(car.engine.status)

#file handling 
try:
    with open("demofile.txt","rt") as f:
        x = f.read()
        
    print(x)

except FileNotFoundError:
    try:
        
        with open("demofile.txt","x") as f:
            f.write("new file")
        with open("demofile.txt","rt") as f:
            x = f.read()
        
        print(x)
    except: 
        print("file can't be created")
    
