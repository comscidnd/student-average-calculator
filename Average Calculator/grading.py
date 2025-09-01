
grading = (input("Enter Grading 1st or 2nd : "))
name = (input("Enter Student Name : " ))
gender = (input("Gender : "))

subjectOne = (float(input("Math : ")))
subjectTwo = (float(input("Science: ")))
subjectThree = (float(input("P.E : ")))
subjectFour = (float(input("A.P : ")))
subjectFive = (float(input("English : ")))
subjectSix = (float(input("Filipino : ")))
subjectSeven = (float(input("Hekasi: ")))


totalAverage = (subjectOne + subjectTwo + subjectThree + subjectFour + subjectFive + subjectSix + subjectSeven ) / 7

print("\nGrading : ", grading)
print("Student Name : ", name)
print("Gender : ", gender)
print("General Average : {:.2f}".format(totalAverage))

if totalAverage >= 100:
    print("ERROR")
elif totalAverage >= 98:
    print("WITH HIGHEST HONORS")
elif totalAverage >= 95:
    print("WITH HIGH HONORS")
elif totalAverage >= 90:
    print("WITH HONORS")
elif totalAverage >= 75:
    print("PASSED!")
else:
    print("FAILED!")
    
