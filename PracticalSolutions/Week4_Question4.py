""" Write a program that takes in a student’s test score (out of 100) and
 returns their letter grade based on the following scale:
 90-100=A, 80-89 =B, 70 – 79 =C, 60-69=D and below 60=F"""

def studentScore():
    studentName = input("What is your name: ")
    testScore = int(input("What is your test score: "))

    if testScore > 100:
        print("Please check that again - the maximum score is 100!")

    elif testScore > 90:
        if testScore <= 100:
            print(studentName + " your score is " + str(testScore) + " and is graded A!")

    elif testScore > 80:
        if testScore <= 89:
            print(studentName + " your score is " + str(testScore) + " and is graded B!")

    elif testScore > 70:
        if testScore <= 79:
            print(studentName + " your score is " + str(testScore) + " and is graded C!")

    elif testScore > 60:
        if testScore <= 69:
            print(studentName + " your score is " + str(testScore) + " and is graded D!")

    elif testScore < 60 :
        print(studentName + " your score is " + str(testScore) + " and is graded F!")

studentScore()

