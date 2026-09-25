marks = int(input("Enter your marks: "))
if marks >= 80:
    print("You got an A grade")
if marks >= 70 and marks < 80:
    print("You got a B grade")
if marks >= 60 and marks < 70:
    print("You got a C grade")
if marks >= 50 and marks < 60:
    print("You got a D grade")
if marks < 50:
    print("You got an F grade")