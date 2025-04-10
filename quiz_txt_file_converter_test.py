#define quiz generator program
def quiz_generator():
    #create a file path or directory for the txt file
    filename = input("Enter filename for you quiz (ex. math_quiz): ")
    file_path = fr"D:\OneDrive\Documents\Kelvin\test_quiz_gen\{filename}.txt"
    count = 1 #added count variable to track number of questions
    #loop the program until user wants to exit
    with open(file_path, "a") as file:
        while True:
            #ask the user for the quiz questions
            questions = input(f"Enter your quiz question no.{count} (Press e to exit the program): ")
            if questions.lower() == 'e': #condition to exit program
                print("Exiting the program.")
                break
            #ask the choices
            choice_a = input("Enter choice a:")
            choice_b = input("Enter choice b:")
            choice_c = input("Enter choice c:")
            choice_d = input("Enter choice d:")
            #ask the answer
            while True:
                correct = input("Enter the correct answer (a, b, c, or d): ").lower()
                if correct in ['a', 'b', 'c', 'd']:
                    break
                else:
                    print("Invalid input. Please enter a, b, c, or d.")
            #save all the information to the txt file
            file.write(f"{count}. {questions} \n")
            file.write("a) " + choice_a + "\n")
            file.write("b) " + choice_b + "\n")
            file.write("c) " + choice_c + "\n")
            file.write("d) " + choice_d + "\n")
            file.write("Answer: " + correct + "\n")
            file.write("\n")  # Add a blank line between questions
            count += 1

if __name__ == "__main__":
    quiz_generator()