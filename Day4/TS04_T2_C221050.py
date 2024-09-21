class Person:
    # Constructor to initialize name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #  display the person's name and age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

    # Method to update the age
    def update_age(self, new_age):
        self.age = new_age
        print(f"Updated Age: {self.age}")

# Creating two instances of Person
person1 = Person("Ayyar", 30)
person2 = Person("Jaber", 25)

# Updating the age of the first person
person1.update_age(35)

# Printing the updated details of both persons
person1.display()  # Displaying person1 name and age
person2.display()  ## Displaying person2 name and age
