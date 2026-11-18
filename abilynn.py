import random


# ==========================================
#          PRELIM - MIDTERM - FINALS
# ==========================================

def pause():
    input("\nPress ENTER to continue...")


# ==========================================
# PRELIM LESSONS
# ==========================================

def prelim():
    while True:
        print("\n========== PRELIM ==========")
        print("1. Introduction to Programming")
        print("2. Basic Syntax")
        print("3. Variables")
        print("4. Data Types")
        print("5. Input and Output")
        print("0. Back to Main Menu")

        choice = input("\nChoose lesson: ")

        if choice == "1":
            print("\nINTRODUCTION TO PROGRAMMING")
            print("Programming is creating instructions")
            print("that tell a computer what to do.")
            print('Example: print("Hello World")')
            print("Output: Hello World")

            while True:
                print("\n(Y) - Take Quiz (N) - Back to Main Menu")
                choice = input("Enter your choice: ").lower()

                if choice == "y":
                    score = 0
                    print("\n====================================")
                    print("         Quiz")
                    print("====================================")
                    print("1. What is programming?")
                    print(
                        "A. Making guidelines for a computer \nB. To coding \nC. To promote computer \nD. Playing games")
                    answer = input("Enter your choice: ").lower()
                    if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                        if answer == "a":
                            score = score + 1
                            print("Your answer is correct")
                        elif answer == "b":
                            score = score
                            print("Your answer is incorrect")
                        elif answer == "c":
                            score = score
                            print("Your answer is incorrect")
                        else:
                            score = score
                            print("Your answer is incorrect")
                    else:
                        print("Invalid Choice!")

                    print(f"Score: {score}/2")

                    print("\n====================================")
                    print("         Quiz")
                    print("====================================")
                    print("2. What is python?")
                    print(
                        "A. Computer  \nB. Videos \nC. Programming language \nD. Word")
                    answer = input("Enter your choice: ").lower()
                    if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                        if answer == "a":
                            score = score
                            print("Your answer is incorrect")
                        elif answer == "b":
                            score = score
                            print("Your answer is incorrect")
                        elif answer == "c":
                            score = score + 1
                            print("Your answer is correct")
                        else:
                            score = score
                            print("Your answer is incorrect")

                    else:
                        print("Invalid Choice!")
                    print(f"Score: {score}/2")
                    break
                elif choice == "n":
                    break

                else:
                    print("Invalid code!")
                    continue

        elif choice == "2":
            print("\nBASIC SYNTAX")
            print("Syntax means the rules of Python.")
            print('Example: print("Welcome to Python")')
            print("Python uses indentation.")
            print("\n(Y) - Take Quiz (N) - Back to Main Menu")
            choice = input("Enter your choice: ").lower()

            if choice == "y":
                score = 0
                print("\n====================================")
                print("         Quiz")
                print("====================================")
                print("1. What is syntax?")
                print(
                    "A. Rules of  correct grammar \nB. Wrong grammar\nC. Change the word\nD. To Input word")
                answer = input("Enter your choice: ").lower()
                if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                    if answer == "a":
                        score = score + 1
                        print("Your answer is correct")
                    elif answer == "b":
                        score = score
                        print("Your answer is incorrect")
                    elif answer == "c":
                        score = score
                        print("Your answer is incorrect")
                    else:
                        score = score
                        print("Your answer is incorrect")
                else:
                    print("Invalid Choice!")

                print(f"Score: {score}/2")
                print("\n====================================")
                print("         Quiz")
                print("====================================")
                print("2. Identify the correct variable")
                print(
                    "A. name = Aldrin \nB. grade == 91.5 \nC. gra-de = 27.5\nD. 2Name = Aldrin")
                answer = input("Enter your choice: ").lower()
                if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                    if answer == "a":
                        score = score + 1
                        print("Your answer is correct")
                    elif answer == "b":
                        score = score
                        print("Your answer is incorrect")
                    elif answer == "c":
                        score = score
                        print("Your answer is incorrect")
                    else:
                        score = score
                        print("Your answer is incorrect")

                else:
                    print("Invalid Choice!")
                print(f"Score: {score}/2")
                break
            elif choice == "n":
                break

            else:
                print("Invalid code!")
                continue

        elif choice == "3":
            print("\nVARIABLES")
            print("Variables store information.")
            name = "Juan"
            age = 18
            print("name ", name)
            print("age ", age)

            while True:
                print("\n(Y) - Take Quiz (N) - Back to Main Menu")
                choice = input("Enter your choice: ").lower()

                if choice == "y":
                    score = 0
                    print("\n====================================")
                    print("         Quiz")
                    print("====================================")
                    print("1. What is a variable?")
                    print(
                        "A. A storage location for data \nB. A computer need to explain \nC. A programming correct grammar \nD. To comment in computer")
                    answer = input("Enter your choice: ").lower()
                    if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                        if answer == "a":
                            score = score + 1
                            print("Your answer is correct")
                        elif answer == "b":
                            score = score
                            print("Your answer is incorrect")
                        elif answer == "c":
                            score = score
                            print("Your answer is incorrect")
                        else:
                            score = score
                            print("Your answer is incorrect")
                    else:
                        print("Invalid Choice!")

                    print(f"Score: {score}/2")

                    print("\n====================================")
                    print("         Quiz")
                    print("====================================")
                    print("2. Which of the following is an example of a variable?")
                    print("A. age = 18 \nB. # Hello \nC. print() \nD. if")
                    answer = input("Enter your choice: ").lower()
                    if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                        if answer == "a":
                            score = score + 1
                            print("Your answer is correct")
                        elif answer == "b":
                            score = score
                            print("Your answer is incorrect")
                        elif answer == "c":
                            score = score
                            print("Your answer is incorrect")
                        else:
                            score = score
                            print("Your answer is incorrect")

                    else:
                        print("Invalid Choice!")
                    print(f"Score: {score}/2")
                    break
                elif choice == "n":
                    break

                else:
                    print("Invalid code!")
                    continue

        elif choice == "4":
            print("\nDATA TYPES")
            print("String  = Text")
            print("Integer = Whole numbers")
            print("Float   = Decimal numbers")
            print("Boolean = True or False")

            while True:
                print("\n(Y) - Take Quiz (N) - Back to Main Menu")
                choice = input("Enter your choice: ").lower()

                if choice == "y":
                    score = 0
                    print("\n====================================")
                    print("         Quiz")
                    print("====================================")
                    print("1. Which data type is used for text?")
                    print("A. Integer \nB. String \nC. Float \nD. Boolean")
                    answer = input("Enter your choice: ").lower()
                    if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                        if answer == "a":
                            score = score
                            print("Your answer is incorrect")
                        elif answer == "b":
                            score = score + 1
                            print("Your answer is correct")
                        elif answer == "c":
                            score = score
                            print("Your answer is incorrect")
                        else:
                            score = score
                            print("Your answer is incorrect")
                    else:
                        print("Invalid Choice!")

                    print(f"Score: {score}/2")

                    print("\n====================================")
                    print("         Quiz")
                    print("====================================")
                    print("2. Which data type is used for whole numbers?")
                    print("A. bool \nB. float \nC. str \nD. int")
                    answer = input("Enter your choice: ").lower()
                    if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                        if answer == "a":
                            score = score
                            print("Your answer is incorrect")
                        elif answer == "b":
                            score = score
                            print("Your answer is incorrect")
                        elif answer == "c":
                            score = score
                            print("Your answer is incorrect")
                        else:
                            score = score + 1
                            print("Your answer is correct")

                    else:
                        print("Invalid Choice!")
                    print(f"Score: {score}/2")
                    break
                elif choice == "n":
                    break

                else:
                    print("Invalid code!")
                    continue

        elif choice == "5":
            print("\nINPUT AND OUTPUT")
            name = input("Enter your name: ")
            print("Your name is", name)

            while True:
                print("\n(Y) - Take Quiz (N) - Back to Main Menu")
                choice = input("Enter your choice: ").lower()

                if choice == "y":
                    score = 0
                    print("\n====================================")
                    print("         Quiz")
                    print("====================================")
                    print(
                        "1. What function is used to display information on the screen?")
                    print("A. Input \nB. Print \nC. Int \nD. Syntax")
                    answer = input("Enter your choice: ").lower()
                    if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                        if answer == "a":
                            score = score
                            print("Your answer is incorrect")
                        elif answer == "b":
                            score = score + 1
                            print("Your answer is correct")
                        elif answer == "c":
                            score = score
                            print("Your answer is incorrect")
                        else:
                            score = score
                            print("Your answer is incorrect")
                    else:
                        print("Invalid Choice!")

                    print(f"Score: {score}/2")

                    print("\n====================================")
                    print("         Quiz")
                    print("====================================")
                    print("2. What will print('Hello') display?")
                    print("A. Hello \nB. print \nC. Error \nD. Nothing")
                    answer = input("Enter your choice: ").lower()
                    if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                        if answer == "a":
                            score = score + 1
                            print("Your answer is correct")
                        elif answer == "b":
                            score = score
                            print("Your answer is incorrect")
                        elif answer == "c":
                            score = score
                            print("Your answer is incorrect")
                        else:
                            score = score
                            print("Your answer is incorrect")

                    else:
                        print("Invalid Choice!")
                    print(f"Score: {score}/2")
                    break
                elif choice == "n":
                    break

                else:
                    print("Invalid code!")
                    continue

        elif choice == "0":
            break

        else:
            print("Invalid choice!")

        pause()


# ==========================================
# MIDTERM LESSONS
# ==========================================

def midterm():
    while True:
        print("\n========== MIDTERM ==========")
        print("1. Conditional Statements")
        print("2. Nested If")
        print("3. Break and Continue")
        print("4. Arithmetic Operators")
        print("5. Logical Operators")
        print("0. Back to Main Menu")

        choice = input("\nChoose lesson: ")

        if choice == "1":
            print("\nCONDITIONAL STATEMENTS")
            age = int(input("Enter your age: "))

            if age >= 18:
                print("You are an adult.")
            else:
                print("You are a minor.")

            while True:
                print("\n(Y) - Take Quiz (N) - Back to Main Menu")
                choice = input("Enter your choice: ").lower()

                if choice == "y":
                    score = 0

                    print("\n====================================")
                    print("         Quiz")
                    print("====================================")
                    print("1. What is the purpose of an if statement?")
                    print("A. To repeat instructions")
                    print("B. To check a condition")
                    print("C. To store information")
                    print("D. To display comments")

                    answer = input("Enter your choice: ").lower()

                    if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                        if answer == "b":
                            score = score + 1
                            print("Your answer is correct")
                        elif answer == "a":
                            print("Your answer is incorrect")
                        elif answer == "c":
                            print("Your answer is incorrect")
                        else:
                            print("Your answer is incorrect")
                    else:
                        print("Invalid Choice!")

                    print(f"Score: {score}/2")

                    print("\n====================================")
                    print("         Quiz")
                    print("====================================")
                    print("2. What happens when the if condition is False?")
                    print("A. The if block will execute")
                    print("B. The program will always stop")
                    print("C. The else block can execute")
                    print("D. The condition becomes True")

                    answer = input("Enter your choice: ").lower()

                    if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                        if answer == "c":
                            score = score + 1
                            print("Your answer is correct")
                        elif answer == "a":
                            print("Your answer is incorrect")
                        elif answer == "b":
                            print("Your answer is incorrect")
                        else:
                            print("Your answer is incorrect")
                    else:
                        print("Invalid Choice!")

                    print(f"Score: {score}/2")
                    break

                elif choice == "n":
                    break

                else:
                    print("Invalid code!")
                    continue

        elif choice == "2":
            print("\nNESTED IF")
            grade = int(input("Enter your grade: "))

            if grade >= 80:
                if grade >= 90:
                    print("Excellent!")
                else:
                    print("Passed!")
            else:
                print("Failed.")

            while True:
                print("\n(Y) - Take Quiz (N) - Back to Main Menu")
                choice = input("Enter your choice: ").lower()

                if choice == "y":
                    score = 0

                    print("\n====================================")
                    print("         Quiz")
                    print("====================================")
                    print("1. What is a nested if statement?")
                    print("A. An if statement inside another if statement")
                    print("B. An if statement without a condition")
                    print("C. A loop inside a variable")
                    print("D. A print statement inside a comment")

                    answer = input("Enter your choice: ").lower()

                    if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                        if answer == "a":
                            score = score + 1
                            print("Your answer is correct")
                        elif answer == "b":
                            print("Your answer is incorrect")
                        elif answer == "c":
                            print("Your answer is incorrect")
                        else:
                            print("Your answer is incorrect")
                    else:
                        print("Invalid Choice!")

                    print(f"Score: {score}/2")

                    print("\n====================================")
                    print("         Quiz")
                    print("====================================")
                    print("2. What will be displayed if the grade is 95?")
                    print("A. Failed.")
                    print("B. Passed!")
                    print("C. Excellent!")
                    print("D. Nothing")

                    answer = input("Enter your choice: ").lower()

                    if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                        if answer == "c":
                            score = score + 1
                            print("Your answer is correct")
                        elif answer == "a":
                            print("Your answer is incorrect")
                        elif answer == "b":
                            print("Your answer is incorrect")
                        else:
                            print("Your answer is incorrect")
                    else:
                        print("Invalid Choice!")

                    print(f"Score: {score}/2")
                    break

                elif choice == "n":
                    break

                else:
                    print("Invalid code!")
                    continue

        elif choice == "3":
            print("\nBREAK AND CONTINUE")

            for i in range(1, 6):
                if i == 3:
                    continue
                if i == 5:
                    break
                print(i)

            while True:
                print("\n(Y) - Take Quiz (N) - Back to Main Menu")
                choice = input("Enter your choice: ").lower()

                if choice == "y":
                    score = 0

                    print("\n====================================")
                    print("         Quiz")
                    print("====================================")
                    print("1. What is the purpose of the break statement?")
                    print("A. To skip one iteration")
                    print("B. To stop a loop")
                    print("C. To repeat a program")
                    print("D. To create a variable")

                    answer = input("Enter your choice: ").lower()

                    if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                        if answer == "b":
                            score = score + 1
                            print("Your answer is correct")
                        elif answer == "a":
                            print("Your answer is incorrect")
                        elif answer == "c":
                            print("Your answer is incorrect")
                        else:
                            print("Your answer is incorrect")
                    else:
                        print("Invalid Choice!")

                    print(f"Score: {score}/2")

                    print("\n====================================")
                    print("         Quiz")
                    print("====================================")
                    print("2. What does continue do?")
                    print("A. Stops the entire program")
                    print("B. Ends a function")
                    print("C. Skips the current iteration and continues the loop")
                    print("D. Deletes a variable")

                    answer = input("Enter your choice: ").lower()

                    if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                        if answer == "c":
                            score = score + 1
                            print("Your answer is correct")
                        elif answer == "a":
                            print("Your answer is incorrect")
                        elif answer == "b":
                            print("Your answer is incorrect")
                        else:
                            print("Your answer is incorrect")
                    else:
                        print("Invalid Choice!")

                    print(f"Score: {score}/2")
                    break

                elif choice == "n":
                    break

                else:
                    print("Invalid code!")
                    continue

        elif choice == "4":
            print("\nARITHMETIC OPERATORS")
            e = 10
            f = 5
            print("Addition (+):", e + f)
            print("Subtraction (-):", e - f)
            print("Multiplication (*):", e * f)
            print("Division (/):", e / f)
            print("Modulus (%):", e % f)
            print("Exponent (**):", e ** f)
            print("Floor Division (//):", e // f)

            while True:
                print("\n(Y) - Take Quiz (N) - Back to Main Menu")
                choice = input("Enter your choice: ").lower()

                if choice == "y":
                    score = 0

                    print("\n====================================")
                    print("         Quiz")
                    print("====================================")
                    print("1. What is the result of 10 + 5?")
                    print("A. 15")
                    print("B. 50")
                    print("C. 5")
                    print("D. 2")

                    answer = input("Enter your choice: ").lower()

                    if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                        if answer == "a":
                            score = score + 1
                            print("Your answer is correct")
                        elif answer == "b":
                            print("Your answer is incorrect")
                        elif answer == "c":
                            print("Your answer is incorrect")
                        else:
                            print("Your answer is incorrect")
                    else:
                        print("Invalid Choice!")

                    print(f"Score: {score}/2")

                    print("\n====================================")
                    print("         Quiz")
                    print("====================================")
                    print("2. Which operator is used to get the remainder?")
                    print("A. //")
                    print("B. **")
                    print("C. %")
                    print("D. /")

                    answer = input("Enter your choice: ").lower()

                    if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                        if answer == "c":
                            score = score + 1
                            print("Your answer is correct")
                        elif answer == "a":
                            print("Your answer is incorrect")
                        elif answer == "b":
                            print("Your answer is incorrect")
                        else:
                            print("Your answer is incorrect")
                    else:
                        print("Invalid Choice!")

                    print(f"Score: {score}/2")
                    break

                elif choice == "n":
                    break

                else:
                    print("Invalid code!")
                    continue

        elif choice == "5":
            print("\nLOGICAL OPERATORS")
            x = True
            y = False
            print("AND:", x and y)
            print("OR:", x or y)
            print("NOT:", not x)

            while True:
                print("\n(Y) - Take Quiz (N) - Back to Main Menu")
                choice = input("Enter your choice: ").lower()

                if choice == "y":
                    score = 0

                    print("\n====================================")
                    print("         Quiz")
                    print("====================================")
                    print(
                        "1. Which logical operator requires both conditions to be True?")
                    print("A. or")
                    print("B. not")
                    print("C. and")
                    print("D. break")

                    answer = input("Enter your choice: ").lower()

                    if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                        if answer == "c":
                            score = score + 1
                            print("Your answer is correct")
                        elif answer == "a":
                            print("Your answer is incorrect")
                        elif answer == "b":
                            print("Your answer is incorrect")
                        else:
                            print("Your answer is incorrect")
                    else:
                        print("Invalid Choice!")

                    print(f"Score: {score}/2")

                    print("\n====================================")
                    print("         Quiz")
                    print("====================================")
                    print("2. What is the result of True or False?")
                    print("A. True")
                    print("B. False")
                    print("C. None")
                    print("D. Error")

                    answer = input("Enter your choice: ").lower()

                    if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                        if answer == "a":
                            score = score + 1
                            print("Your answer is correct")
                        elif answer == "b":
                            print("Your answer is incorrect")
                        elif answer == "c":
                            print("Your answer is incorrect")
                        else:
                            print("Your answer is incorrect")
                    else:
                        print("Invalid Choice!")

                    print(f"Score: {score}/2")
                    break

                elif choice == "n":
                    break

                else:
                    print("Invalid code!")
                    continue

        elif choice == "0":
            break

        else:
            print("Invalid choice!")

        pause()


# ==========================================
# FINALS LESSONS
# ==========================================

def finals():
    while True:
        print("\n========== FINALS ==========")
        print("1. For Loop")
        print("2. While Loop")
        print("0. Back to Main Menu")

        choice = input("\nChoose lesson: ")

        if choice == "1":
            print("\nFOR LOOP")
            for number in range(1, 10):
                print("study python ")

            while True:
                print("\n(Y) - Take Quiz (N) - Back to Main Menu")
                choice = input("Enter your choice: ").lower()

                if choice == "y":
                    score = 0

                    print("\n====================================")
                    print("         Quiz")
                    print("====================================")
                    print("1. What is the purpose of a for loop?")
                    print("A. To store information")
                    print("B. To repeat instructions")
                    print("C. To display comments")
                    print("D. To stop a program")

                    answer = input("Enter your choice: ").lower()

                    if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                        if answer == "b":
                            score = score + 1
                            print("Your answer is correct")
                        elif answer == "a":
                            print("Your answer is incorrect")
                        elif answer == "c":
                            print("Your answer is incorrect")
                        else:
                            print("Your answer is incorrect")
                    else:
                        print("Invalid Choice!")

                    print(f"Score: {score}/2")

                    print("\n====================================")
                    print("         Quiz")
                    print("====================================")
                    print("2. What does range(1, 5) represent?")
                    print("A. Numbers from 1 to 5")
                    print("B. Numbers from 0 to 5")
                    print("C. Numbers from 1 to 4")
                    print("D. Numbers from 2 to 5")

                    answer = input("Enter your choice: ").lower()

                    if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                        if answer == "c":
                            score = score + 1
                            print("Your answer is correct")
                        elif answer == "a":
                            print("Your answer is incorrect")
                        elif answer == "b":
                            print("Your answer is incorrect")
                        else:
                            print("Your answer is incorrect")
                    else:
                        print("Invalid Choice!")

                    print(f"Score: {score}/2")
                    break

                elif choice == "n":
                    break

                else:
                    print("Invalid code!")
                    continue

        elif choice == "2":
            print("\nWHILE LOOP")
            count = 1

            while count <= 5:
                print(count)
                count += 1

            while True:
                print("\n(Y) - Take Quiz (N) - Back to Main Menu")
                choice = input("Enter your choice: ").lower()

                if choice == "y":
                    score = 0

                    print("\n====================================")
                    print("         Quiz")
                    print("====================================")
                    print("1. What is the purpose of a while loop?")
                    print("A. To repeat instructions while a condition is True")
                    print("B. To store text")
                    print("C. To display comments")
                    print("D. To create a data type")

                    answer = input("Enter your choice: ").lower()

                    if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                        if answer == "a":
                            score = score + 1
                            print("Your answer is correct")
                        elif answer == "b":
                            print("Your answer is incorrect")
                        elif answer == "c":
                            print("Your answer is incorrect")
                        else:
                            print("Your answer is incorrect")
                    else:
                        print("Invalid Choice!")

                    print(f"Score: {score}/2")

                    print("\n====================================")
                    print("         Quiz")
                    print("====================================")
                    print(
                        "2. What happens when the while loop condition becomes False?")
                    print("A. The loop repeats forever")
                    print("B. The loop stops")
                    print("C. The loop restarts automatically")
                    print("D. The variable is deleted")

                    answer = input("Enter your choice: ").lower()

                    if answer == "a" or answer == "b" or answer == "c" or answer == "d":
                        if answer == "b":
                            score = score + 1
                            print("Your answer is correct")
                        elif answer == "a":
                            print("Your answer is incorrect")
                        elif answer == "c":
                            print("Your answer is incorrect")
                        else:
                            print("Your answer is incorrect")
                    else:
                        print("Invalid Choice!")

                    print(f"Score: {score}/2")
                    break

                elif choice == "n":
                    break

                else:
                    print("Invalid code!")
                    continue

        elif choice == "0":
            break

        else:
            print("Invalid choice!")

        pause()


# ==========================================
# SIMPLE CALCULATOR
# ==========================================

def calculator():
    print("\n========== CALCULATOR ==========")

    try:
        num1 = float(input("Enter first number: "))
        operator = input("Choose (+, -, *, /, %, **): ")
        num2 = float(input("Enter second number: "))

        if operator == "+":
            print("Answer:", num1 + num2)
        elif operator == "-":
            print("Answer:", num1 - num2)
        elif operator == "*":
            print("Answer:", num1 * num2)
        elif operator == "/":
            if num2 != 0:
                print("Answer:", num1 / num2)
            else:
                print("Cannot divide by zero!")
        elif operator == "%":
            if num2 != 0:
                print("Answer:", num1 % num2)
            else:
                print("Cannot divide by zero!")
        elif operator == "**":
            if num2 != 0:
                print("Answer:", num1 / num2)
            else:
                print("Cannot divide by zero!")
        else:
            print("Invalid choice")

    finally:
        print("finally")


while True:
    print("\n===== PYTHON PROGRAM =====")
    print("1. PRELIM")
    print("2. MIDTERM")
    print("3. FINALS")
    print("4. CALCULATOR")
    print("0. EXIT")

    choice = input("Choose option: ")

    if choice == "1":
        prelim()
    elif choice == "2":
        midterm()
    elif choice == "3":
        finals()
    elif choice == "4":
        calculator()
    elif choice == "0":
        print("Thank you!")
    else:
        print("Invalid choice!")
