class Person:
    def __init__(self,name,surname,age):
        self.name = name
        self.surname = surname
        self.age = age
    def __str__(self):
        return f"{self.name} {self.surname} {self.age}"
person_1 = Person("Walter","White",52)
print(person_1.__str__())

class Customer(Person):
    def __init__(self, name, surname, age, amount):
        super().__init__(name, surname, age)
        self.amount = amount
    def __str__(self):
        return f"{super().__str__()} {self.amount}"
customer_1 = Customer("Gus","Fring","55","1000")
print(customer_1.__str__())