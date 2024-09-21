# Define a class named Person
class Person:
    # Constructor to initialize name and age attributes
    def __init__(self, name, age):
        self.name = name   
        self.age = age    

    # display information about the person
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

    # to display greet the person
    def greet(self):
        print(f"Hello {self.name}, you are {self.age} years old!")

# Create an object 
person = Person("Ayyar", 30)  # Instantiating the Person class
person.display_info()        # Displaying person's name and age
person.greet()               # Greeting the person
