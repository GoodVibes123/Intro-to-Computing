#que1
print("ansewer1")
a = int(input("first number:"))
b = int(input("second number:"))
c = int(input("third number:"))
print((a+b+c)/3)
print()
#que2
print("answer2")
a = float(input("enter gross income($):"))
b = int(input("enter number of dependents:"))
c = a - 10000 - b*3000
print("tax= " + str(0.2*c) + "$")
print()
#que3
print("answer3")
SID = int(input("student SID:"))
Name = input("student name:")
Gender = input("gender(F,M,U):")
Course = input("Course Name:")
CGPA = float(input("student CGPA:"))
list1 = [SID, Name, Gender, Course, CGPA]
print("student",list1)
print()
#que4
print("answer4")
a = int(input("marks of 1st student:"))
b = int(input("marks of 2nd student:"))
c = int(input("marks of 3rd student:"))
d = int(input("marks of 4th student:"))
e = int(input("marks of 5th student:"))
list1 = [a, b, c, d, e]
list1.sort()
print(list1)
print()
#que5(a)
print("answer5")
list = ["Red", "Green", "White", "Black", "Pink", "Yellow"]
del list[3]
print("(a)", "color", list)
print()
#que5(b)
list1 = ["Red","Green","White","Black","Pink","Yellow"]
list1[3] = "Purple"
print("(b)", "color", list1[0:4]+list1[5:])
