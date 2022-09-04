#Aubre A. Anderson  
#GPA Achievement
# This application will accecpts studemts full name and informs you if student(s) have made the Deans List or Honor roll.

GPA = 0.0
student = " "
lastName = " "
firstName = " "
processing = True


def studentsName(student, processing):
    lastName = str(input("Enter Students Last Name: or 'ZZZ' to Quit: "))
    if lastName.upper() == "ZZZ":
        print ("Quitting Program")
        processing = False
        return student, processing
    else:
        firstName = str(input("Enter Students First Name: "))
        student = lastName + " " + firstName
        return student, processing


def messages():
    if GPA >= 3.5:
        print("Deans List")
    elif GPA>=3.25:
        print ("Honor Roll") 
    else:
        print ("Did not make honor roll or deans list")
    

def GPA_score(GPA):
    try:
        GPA = float(input("Enter GPA:" ))
        assert 4.0 >= GPA >= 0.0
        return GPA
    except:
        return GPA_score(GPA)


while processing == True:
    student, processing = studentsName(student, processing)
    if processing == False:
        print ("Quitting Program")
    else:
        studentsName
        GPA = GPA_score(GPA) 
        messages()






