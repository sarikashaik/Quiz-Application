# opening and quiz instructions

print("\t\t\t\t\t\t*****WELCOME to QUIZ*****\n\n")
print("INSTRUCTIONS!!!\n")
print("! Enter your details correctly.")
print("! This quiz contains 3 subjects.\n\t* Python\n\t* Mathematics\n\t* General Knowledge\n! Each subject consists of 5 questions.")
print("! The questions are of type multiple choice.\n! Enter the option number correctly, else your answer gets incorrect.")


# collecting user details and saving them in a file (username file)


print("\n\n-------------USER DETAILS---------------\n")

user_name = (input("Enter your name: "))
user_roll_num = (input("\nEnter your Roll Number: "))

user_total_score = 0
python_score = 0
maths_score = 0
gk_score = 0

# start of the quiz function


def startquiz():

    global user_total_score
    global python_score
    global maths_score
    global gk_score
    
# start of python quiz
    
    pythonFile = open("python questions.txt","r")
    
    print("\n----------PYTHON----------")                       
    
    for p_line in pythonFile:
        p_data = p_line.split(",")
        print("\nQuestion:\n",p_data[0])
        print("\nOption 1:",p_data[1])
        print("Option 2:",p_data[2])
        print("Option 3:",p_data[3])
        print("Option 4:",p_data[4])
        
        user_answer = int(input("What is your answer ?\n"))
        
        if (user_answer == int(p_data[5])):
            print("\nYAY! Your answer is correct...")
            python_score += 1
        else:
            print("\nIncorrect Answer")
            print("The correct option is",p_data[5])
    print("\nYour Score in python is: ",python_score)
     
    pythonFile.close()

# start of maths quiz

    mathsFile = open("maths questions.txt","r")
    
    print("\n----------MATHEMATICS----------")                       

    for m_line in mathsFile:
        m_data = m_line.split(",")
        print("\nQuestion:\n",m_data[0])
        print("\nOption 1:",m_data[1])
        print("Option 2:",m_data[2])
        print("Option 3:",m_data[3])
        print("Option 4:",m_data[4])

        user_answer = int(input("What is your answer ?\n"))

        if (user_answer == int(m_data[5])):
            maths_score += 1
            print("YAY! Your answer is correct...")
               
        else:
            print("\nIncorrect Answer")
            print("\nThe correct option is",m_data[5])
        
    print("\nYour Score in Mathematics is: ",maths_score)

    mathsFile.close()

# start of general knowledge quiz

    gkFile = open("gk questions.txt","r")
    
    print("\n----------GENERAL KNOWLEDGE----------")                       

    for gk_line in gkFile:
        gk_data = gk_line.split(",")
        print("\nQuestion:\n",gk_data[0])
        print("\nOption 1:",gk_data[1])
        print("Option 2:",gk_data[2])
        print("Option 3:",gk_data[3])
        print("Option 4:",gk_data[4])

        user_answer = int(input("What is your answer ?\n"))
        
        if (user_answer == int(gk_data[5])):
            gk_score += 1
            print("YAY! Your answer is correct...")
        
        else:
            print("\nIncorrect Answer")
            print("\nThe correct option is",gk_data[5])
          
    print("\nYour Score in General Knowledge is: ",gk_score)

    gkFile.close()
    
# displaying total score

    user_total_score = (python_score + maths_score + gk_score)
    print("\n\n*******\n\n")
    print("TOTAL SCORE :",user_total_score)

    if (user_total_score == 15):
        print("Status: A")
        print("hi-fi!! you did it.")
    elif (user_total_score >= 10):
        print("Status: B")
        print("congo!! good score.")
    else:
        print("Status: C")
        print("try hard")
    
    
# end of the quiz function


# start of the function displaying user details in the file

def user_details_display_file():
    
    user_file = open("user_details.txt","a")
    
    user_file.write("Student details and their Marks scored in the respective subjects.")
    
    user_file.write("\nNAME: ")
    user_file.write(user_name)
    
    user_file.write("\nROLL NUMBER: ")
    user_file.write(user_roll_num)

    user_file.write("\nPYTHON SCORE: ")
    user_file.write(str(python_score))

    user_file.write("\nMATHEMATICS SCORE: ")
    user_file.write(str(maths_score))

    user_file.write("\nGENARAL KNOWLEDGE SCORE: ")
    user_file.write(str(gk_score))
    
    user_file.write("\nTOTAL SCORE: ")
    user_file.write(str(user_total_score))
    
    user_file.write("\n---------------------------------------------------------------------------\n")
    
    user_file.close()

# end of function displaying user details in the file



# start of the program

startquiz()
user_details_display_file()
