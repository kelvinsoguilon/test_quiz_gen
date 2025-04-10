#define quiz generator program
def quiz_generator():
    #create a file path or directory for the txt file
    filename = "quiz.txt"
    count = 1
#loop the program until user wants to exit
    with open(filename, "a") as file:
        while True:
            questions = input(f"Enter your quiz question no.{count}. (Press e to exit the program): ")
            if questions.lower == 'e':
                print("Exiting the program.")
                break
            count += 1
#ask the user for the quiz questions
#ask the choices
#ask the answer
#save all the information to the txt file