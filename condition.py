age = 21

if (age >=18):
    print("Can vote & apply for licence ")
    print("Can drive")


#Next Ques

light = "yellow"

if (light == "red"):
    print("Stop")

elif (light == "green"):
    print("go")

elif (light == "yellow"):
    print("Ready")



#Ques

marks = int(input("Enetr Student marks: "))

if (marks >=90):
    grade = "A"

elif (marks >=80 and marks <90):
    grade = "B"

elif (marks >=70 and marks <80):
    grade = "C"

else:
    grade = "D"

print ("Grade of the student :", grade)