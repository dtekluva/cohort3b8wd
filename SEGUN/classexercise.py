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


# class employee():

#     company_name = "shell global venture"

#     def __init__(self, name, age,designation,salary,yrs_work):
#         self.name = name
#         self.age = age
#         self.designation= designation
#         self.salary = salary
#         self.yrs_work = yrs_work


#     def describe(self):
#         print("description. \n")
#         print("name :", self.name)
#         print("age :", self.age)
#         print("designation :", self.designation)
#         print("salary :", self.salary)
#         print("yrs_work :", self.yrs_work)
#         print("yearly bonus :", self.yearly_bonus)
        
#     def yearly_bonus(self):
#         return self.salary*self.yrs_work //100

# employee1 = employee("Alex Dokubo", 35, "ADMIN", 400000, 2)
# employee2 = employee("bola adebiyi", 55, "ADMIN", 4900000, 2)
# employee1.describe()
# employee2.describe()
# print(employee1.yearly_bonus() )
# print(employee2.yearly_bonus()) 



class humans:
    skin = True
    brain = True
    num_leg = 2
    num_ears = 2

class european(humans):
    skin_color= "white"
    hair_type = "silky"

    def describe(self):
        print(f"i am a {self.skin_color}....and have {self.hair_type} hair")
        

class employee(european):

    def __init__(self, name,age,salary,dept):
        self.name = name
        self.age = age
        self.salary = salary
        self.dept = dept

    def describe(self):
        super().describe()
        print("my name is",self.name)
        print("i am ",self.age, "yrs old")
        print("i earn a total of",self.salary, "monthly and")
        print("i work in",self.dept,"of telly4africa media")

teanm1=employee("kinging aderibigbe",34, 20000, "HR")
team2 = employee("omotayo ayodeji",46,"admin",30987)

teanm1.describe()
team2.describe()


    
