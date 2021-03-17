class European:
    skin_type = "soft"
    eyes = "white"
    num_legs = 2
    num_ears = 2
    tribe = "British"

    def describe(self):
        print(f"I am {self.tribe}..!! That's all.")


class Employee(European): 
    skin_color  = "white"
    hair_type = "long_hair"
    tribe = "European"


class Guru(Employee):

    def __init__(self, name, age, dept, salary) -> None:
        self.name = name
        self.age = age
        self.dept = dept
        self.salary = salary

    def describe(self):
        print(f"I am an employee and my name is {self.name}")
        super().describe()

# mitchelle.European = Guru("Mitchel", 31, "production", "$4,000 monthly")
Mitchelle.describe()
