# Write a Python program to detect the number of local variables declared in a function.


def detect_lv():
    lvname = "Joseph"
    lvschool = "univelcity"
    lvteacher = "Mr Atha"

print(detect_lv.__code__.co_nlocals)