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

#     cover_color = "brown"

#     def __init__(self, title, body, size = 10):
#         self.title = title
#         self.size = size
#         self.body = body

#     def __str__(self):
#         return f"{self.title}. {self.size} leaves Notebook"

#     def show_body(self):
#         print("Title : ", self.title.upper())
#         print("#######################")
#         print(self.body)

#     def n_chars(self):
#         print(len(self.body))

#     def describe(self):
#         print("Desription. \n")
#         print(self.title)
#         print("Title length : ",len(self.title))
#         print("Body length : ",len(self.body))
#         print("Color : ",self.cover_color)



# note1 = Note("happy day", "Today is a happy day")
# note2 = Note("hehehe", "Nothing worth reading")
# note3 = Note("ooupsie", "Mistake while typing. LOL", 30)


# # print(note1)
# # print(note3)
# # print(note2)

# # note3.show_body()
# note3.n_chars()
# note1.describe()
# # print(note1.cover_color)


class Employee():

    company_name = "New Age Corp."

    def __init__(self, name, age, designation, salary, years_of_work) -> None:
        self.name = name
        self.age = age
        self.designation = designation
        self.salary = salary
        self.years_of_work = years_of_work

    def describe(self):
        print("Name : ", self.name)
        print("Age : ", self.age)
        print("designation : ", self.designation)
        print("salary : ", self.salary)
        print("Work years : ", self.years_of_work)
        print("Yearly bonus : ", self.yearly_bonus())

    def yearly_bonus(self):
        return self.salary * self.years_of_work * 0.1

employee1 = Employee("John Williams", 41, "HR", 2304000, 2)
employee1.describe()

# print(employee1.yearly_bonus())