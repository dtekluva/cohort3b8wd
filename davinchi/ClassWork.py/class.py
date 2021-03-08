# class Dog:
#     pass

# bruno = Dog()
# busky = Dog()
# tiger = Dog()
# print(type(bruno))
# print(type(busky))
# print(type(tiger))
# print(type("21"))

# class Dog:

#     species = "Canis familiaris" # class attribute
#     sound = "bark"

#     def __init__(self, name, age):
#             self.name = name # instance attributes
#             self.age = age

#     def __str__(self) -> str:
#         return f"{self.name}, {self.age}, {self.species}"

# bruno = Dog("bruno", "2")
# busky = Dog("busky", "1.5")
# tiger = Dog("tiger", "2")

# print(bruno)
# print(busky)
# print(tiger)


# class Note:

#     cover_color = "Brown"

#     def __init__(self, name, body, designation = 10):
#         self.name = name
#         self.body = body
#         self.designation = designation

#     def __str__(self) -> str:
#         return f"{self.name}. {self.designation} leaves Notebook"

#     def show_body(self):
#         print("name : ", self.name.upper())
#         print("#######################")
#         print(self.body)

#     def n_chars(self):
#         print(len(self.body))

#     def describe(self):
#         print("Desription. \n")
#         print(self.name)
#         print("name length : ",len(self.name))
#         print("Body length : ",len(self.body))


# note1 = Note("happy day", "Today is a happy day")
# note2 = Note("hehehe", "Nothing worth reading")
# note3 = Note("ooupsie", "Mistake while typing. LOL", 30)


# # print(note1)
# # print(note3)
# # print(note2)

# note3.show_body()
# note3.n_chars()
# note1.describe()
# print(f"the colour of the cover is {note2.cover_color}")


class Company:

    comany_name  = "Liberty_Cred"

    def __init__(self, name, age, designation, salary, yrs_of_work):
        self.name = name
        self.age = age
        self.designation = designation
        self.salary = salary
        self.yrs_of_work = yrs_of_work


    def describe(self):
        print("name: ", self.name)
        print("age: ", self.age)
        print("salary: ", self.salary)
        print("designation: ",  self.designation)
        print("Yearly bonus: ", self.yearly_bonus())

    def yearly_bonus(self):
        return self.salary * self.yrs_of_work * 0.25

        

employee1 = Company("Seye", 44, "Sales & Marketing", 230000, 2)
employee1.describe() 