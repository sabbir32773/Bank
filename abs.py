"""
from abc import ABC, abstractmethod


class Father(ABC):
    @abstractmethod
    def go_school(self):
        pass

    # concrete method
    def result(self):
        print("Yes, I've gone to school.")


class Nobita(Father):
    def go_school(self):
        super().result()

    def playing(self):
        print("Playing Football.")

    def singing(self):
        print("Singing")


nobita = Nobita()
nobita.go_school()
nobita.playing()

Comment"""


class Employee:
    def __init__(self):
        self.name = "Sumon Ali"

    def display(self):
        print(self.name)


ob1 = Employee()
ob1.display()


# Example of the parameterized constructor:
class Myclass:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city
        print("Constructor Method Invoked!")

    def print_data(self):
        print(self.name)
        print(self.age)
        print(self.city)


ob1 = Myclass("Suzana", 12, "Rangpur")
ob1.print_data()
