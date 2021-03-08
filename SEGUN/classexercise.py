# class Note:

#     cover_color = "brown"

#     def __init__(self, title, body, size,color = 10):
#         self.title = title
#         self.size = size
#         self.body = body

#     def __str__(self) -> str:
#         return f"{self.title}. {self.size} leaves Notebook"

#     def show_body(self):
#         print("Title : ", self.title.upper())
#         print("#######################")
#         print(self.body)

#         print(len(self.body))

#     def describe(self):
#         print("Desription. \n")
#         print(self.title)
#         print("Title length : ",len(self.title))
#         print("Body length : ",len(self.body))


# note1 = Note("happy day", "Today is a happy day")
# note2 = Note("hehehe", "Nothing worth reading")
# note3 = Note("ooupsie", "Mistake while typing. LOL", 30)


# print(note1)
# print(note3)
# print(note2)

# note3.show_body()
# note3.n_chars()
# note1.describe()
# print(note1.cover_color)


class employee():

    company_name = "shell global venture"

    def __init__(self, name, age,designation,salary,yrs_work):
        self.name = name
        self.age = age
        self.designation= designation
        self.salary = salary
        self.yrs_work = yrs_work


    def describe(self):
        print("description. \n")
        print("name :", self.name)
        print("age :", self.age)
        print("designation :", self.designation)
        print("salary :", self.salary)
        print("yrs_work :", self.yrs_work)
        print("yearly bonus :", self.yearly_bonus)
        
    def yearly_bonus(self):
        return self.salary*self.yrs_work //100

employee1 = employee("Alex Dokubo", 35, "ADMIN", 400000, 2)
employee2 = employee("bola adebiyi", 55, "ADMIN", 4900000, 2)
employee1.describe()
employee2.describe()
print(employee1.yearly_bonus())
print(employee2.yearly_bonus()) 






    
