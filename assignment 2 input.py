#Question 1

print("Answer 1.")

questionstring = "Python is a case sensitive language"

#part a
#printing the length of the string
print("a.",len(questionstring))

#part b
#print the string in reverse order
print("b.",questionstring[::-1])

#part c
#store a substring into a new string
slicedstring = questionstring[10:]
print("c.",slicedstring)

#part d
#replacing a substring with another
replacedstring = questionstring.replace("a case sensitive","object oriented")
print("d.",replacedstring)

#part e
#printing the index of "a"
print("e.",questionstring.index("a"))

#part f
#printing the string wihtout the whitespaces
stringlist = questionstring.split()
print("f. ",*stringlist, sep="")

#_____________________________________________________________

#Question 2

print("\n\nAnswer 2.")

#storing details in variables
name= "Priyanka Soni"
sid= "21103051"
department= "CSE"
cgpa= "9.9"

#printing the desired output with the format function
print("Hey, {} Here!".format(name))
print("My SID is {}".format(sid))
print("I am from {} department and my CGPA is {}".format(department, cgpa))

#_____________________________________________________________

#Question 3

print("\n\nAnswer 3.")

#defining values
a=56
b=10

#printing answer outputs
print("a.",a&b)
print("b.",a|b)
print("c.",a^b)
print("d. New values of a and b are ", a<<2, "and", b<<2)
print("e. New values of a and b are ", a>>2, "and", b>>2)

#_____________________________________________________________

#Question 4

print("\n\nAnswer 4.")

#inputing 3 values
inputlist= list(map(int,input("Input 3 values:").split()))

#finding the greatest value
greatestvalue= inputlist[0]
for i in range(3):
    if inputlist[i] > greatestvalue:
        greatestvalue = inputlist[i]
print("Greatest value is ",greatestvalue)

#_____________________________________________________________

#Question 5

print("\n\nAnswer 5.")

#inputing string
inputstring = input("Enter a string:")

if "name" in inputstring:
    print("Yes")
else:
    print("No")

#_____________________________________________________________

#Question 6

print("\n\nAnswer 6.")

sides = list(map(int,input("Input the length of 3 sides:").split()))

#test to check if the sides can make a triangle
if sides[0] + sides[1] > sides[2] and\
    sides[2] + sides[0] > sides[1] and\
    sides[2] + sides[1] > sides[0]:
    print("Yes")
else:
    print("No")
