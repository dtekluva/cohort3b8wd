class Emploee:
    company_name = "Digital Tech"
    def __init__(self, name, age, designation, salary, years_of_work):
        self.name = name
        self.age = age
        self.designation = designation
        self.salary = salary
        self.years = years_of_work
    
    def calBonus(self):
        s = self.salary
        firstp = (s* 20) / 100
        fina = (firstp * 50) / 100

        return fina
    
    def describe(self):
        print("Company: ", self.company_name)
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Designation: ", self.designation)
        print("Salary: ", self.calBonus())
        print("Years of work: ", self.years)

joseph = Emploee("Joseph", 11, "Enugu", 12000000, 4)

joseph.describe()
