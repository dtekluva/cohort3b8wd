# class  Human:
#     skin = True
#     brain = True
#     num_legs = 2
#     num_ears = 2
#     culture = "Human"

#     def describe(self):
#         print(f"I am a {self.culture}..!! That's all.")

# # ade = Human()
# # print(ade.brain)
# # shola = Human()
# # print(shola.brain)
# # kunle = Human()
# # print(kunle.brain)

# class African(Human): # African inherits from human
#     skin_color  = "dark"
#     hair_type = "wooly"
#     culture = "African"

# # shalewa = African()
# # print(shalewa.hair_type)
# # shalewa.describe()

# class Student(African):

#     def __init__(self, name, age, course) -> None:
#         self.name = name
#         self.age = age
#         self.course = course

#     def describe(self):
#         print(f"I am a student and my name is {self.name}")
#         super().describe()

# bolu = Student("bolu", 23, "Electrical")
# bolu.describe()




