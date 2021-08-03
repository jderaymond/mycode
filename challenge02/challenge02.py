#!/usr/bin/env python3

icecream = ["flavors", "salty"]

tlgclass= ["Adrian","Bikash","Chas","Chathula","Chris","Hongyi","Jauric","Joe L.","Joe V.","Josh","Justin","Karlo","Kerri-Leigh","Jason","Nicholas","Peng","Philippe","Pierre","Stephen","Yun"]


icecream.append(99)

student = input("Pick a number between 0 and 19: ")
student_integer = int(student)
print(f"{icecream[-1]} {icecream[0]}, and {tlgclass[student_integer]} chooses to be {icecream[1]}.")

