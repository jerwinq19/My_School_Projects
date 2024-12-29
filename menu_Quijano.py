# BSIT-1A JERWIN QUIJANO
import os
import time
import random as ran

def clear_screen():
    input("\n\nPRESS ENTER TO PROCEED TO THE NEXT PART...")
    os.system('cls')
    
def main_menu(): # INTRO MENU
    while True:
        name = input("Enter your name: ").title()
        if name.isnumeric() or name == '' or name == ' ':
            print("Please enter an appropriate value.")
        else:
            os.system("cls")
            break
    text1 = (f"Welcome ⸜( ^ ᵕ ^ )⸝♡ {name}! to my Menu program!")
    for char in text1:
        print(char,end="",flush=True)
        time.sleep(0.01)
    clear_screen()
    text2 = ("In this menu program, you will encounter different topics such as Print Statements,\nVariables, Operators, Conditionals Statements, Loops, and Functions.")  
    for char in text2:
        print(char,end="",flush=True)
        time.sleep(0.01)    
    clear_screen()
    
def print_statements():# PRINT STATEMENTS
    while True:
        print("-"*150)
        print("Welcome to Print statements!")
        print("-"*150)
        print(
            '''[1] With explination\n[2] Without explination\n[3] Try it yourself'''
        )
        print("-"*150)  
        ask = input("\nEnter your options (Q to Quit):  ").lower()

        clear_screen()
        if ask == '1':
            print("-"*150)
            print(
                
                '''The print() function in Python is used to output data to the console. It can take any number of parameters, which can be separated by commas.\nBy default, the items are converted to text form, separated by spaces, and there is a single newline character ("\.n") at the end.'''
            )
            print("-"*150)
            clear_screen()
            print("-"*150)
            print("In this tutorial, we will cover various types of print statements in Python.")
            print("Printing statements is a fundamental concept in programming, and mastering it will enhance your coding skills.")
            print("Let's dive in and explore the different ways we can use print statements in Python!")
            print("-"*150)
            clear_screen()

            print("-"*150)
            print("\t\t\t\t\t\tThere are several uses of Print Statements!") #BASIC PRINT
            print("-"*150)
            print("1. Basic Print Statement - This is the simplest form, where you just print a string or a variable.")
            print("-"*150)
            print("The syntax is [ print('hello world') ] <-- inside the parenthesis there where will you put the things you want to print!")
            print("Like the example above is it put 'hello world'")
            print("\nStructure:\n\nprint('hello world')\n\nThe output will be \n\nOutput\nhello world!")
            print("-"*150)
            clear_screen()

            print("-"*150)
            print("2. Formatted String - You can use formatted strings to include variables or expressions within a string.") #FORMATTED PRINT
            print("-"*150)
            print("First, you need to declare a Variable for this example, I will declare name = 'Alice' and age = 30\nand I will use the f keyword! Example below.")
            print("\n\nStructure:\n")
            text = "name = 'Alice'\nage = 30\nprintf(f'My name is {name} and I am {age} years old.')"
            print(text)
            print("\nOutput:\nMy name is Alice and I am 30 years old.")
            print("-"*150)
            clear_screen()

            print("-"*150)
            print("3. Concatenation: -  You can concatenate strings using the '+' operator.") #CONCATINATION
            print("-"*150)
            print("Same procedure! First, you need to declare a Variable for this example, I will declare first_name = 'Jerwin' and last_name = 'Quijano'\nExample below.")
            print("\n\nStructure:\n")
            text = "first_name = 'Jerwin'\nlast_name = 'Quijano'\nprint('Full name:', + first_name + '' + last_name)"
            print(text)
            clear_screen()
            print("\n\nOutput:\nFull name: Jerwin Quijano")
            print("\nThe purpose of ' ' is to put a white space! in between the string! if you don't put it this will be the output.")
            print("\nOutput:\n\nFull name: JerwinQuijano")
            print("-"*150)
            clear_screen()

            print("-"*150)
            print("4. Multiple Arguments: - You can print multiple items separated by commas [,].") #MULTIPLE ARGUEMENTS
            print("-"*150)
            print("It is like the number 3 it looks the same but it uses a comma [,] instead of a plus [+].\nDo the same procedure again! Declare a Variable! in this case, I will declare [ x = 10 and y = 20 ] below you will see the structure.")
            print("\nStructure:\nx = 10\ny = 20\nprint(f'The value of x is', x,'and the value of y is', y)")
            print("\nOutput\nThe value of x is 10 and the value of y is 20")
            print("-"*150)
            clear_screen()

            print("-"*150)
            print("Yehey, you have reached the end of print statements. Do not forget to try another code from the menu!")
            print("-"*150)
            clear_screen()
        
        
        elif ask == "2":
            
            #1. basic print statement
            print("-"*150)
            print(
                '''The syntax for Basic Print statements\n\nSyntax:\nprint('hello world')\nOutput:\nhello world'''
            )
            print("-"*150)
            clear_screen()
            
            #2. formatted printing
            print("-"*150)
            print(
                '''The syntax for Formatted print\n\nSyntax:\nname = "Jerwin"\nage = 18\ncourse = "BSIT"\nprint(f"Hello my name is {name} and i am {age} years old! and i am pursuing {course}.\n\nOutput:\nHello my name is Jerwin and i am 18 years old! and i am pursuing BSIT.")'''
            )
            print("-"*150)
            clear_screen()
            
            #3. Concatenation:
            print("-"*150)
            print(
                '''The syntax for Concatenation\n\nSyntax:\nfirst_name = "Jerwin"\nlast_name = "Quijano"\nprint("Full name:", + first_name + "" + last_name)\n\nOutput:\nFull name: Jerwin Quijano'''
            )
            print("-"*150)
            clear_screen()
            
            #Multiple Arguments
            print("-"*150)
            print(
                '''The syntax for Multiple Arguments:\nx = 10\ny = 20\nprint(f"The value of x is", x,"and the value of y is", y)\n\nOutput:\nThe value of x is 10 and the value of y is 20"'''
            )
            print("-"*150)
            clear_screen()
            
            print("-"*150)
            print("Yehey, you have reached the end of print statements. Do not forget to try another code from the menu!")
            print("-"*150)
            clear_screen()
        
        elif ask == '3':
            while True:
                print("Welcome to section 3. You can try your newly learned stuff here!")
                print("1. Basic Print Statement\n2. Formatted String\n3. Concatenation\n4. Multiple Arguments\n5. Exit")
                print("-"*150)
                ask = input("What do you want to try?: ")
                clear_screen()

                if ask == '1':
                    print("-"*150)
                    print("Welcome to Basic print statement!")
                    print("-"*150)
                    temp = "    "
                    print(f"Hello, {temp}!")
                    print("-"*150)
                    in_ask = input("What do you want to put?: ")
                    print("-"*150)
                    print(f'''Terminal:\n\nHello, {in_ask}!''')
                    clear_screen()

                elif ask == '2':
                    print("-"*150)
                    print("Welcome to Formatted print statement!")
                    print("-"*150)
                    temp = "\t"
                    print(f"Hello, {temp}!")
                    in_ask = input("What do you want to put?: ")
                    print("-"*150)
                    print(f'''Terminal:\n\nHello, {in_ask}!''')
                    clear_screen()

                elif ask == '3':
                    print("-"*150)
                    print("Welcome to Concatenation!")
                    print("-"*150)
                    
                    print(
                        f'''print("Your name is " + var1 + " and you are " + var2)\n'''
                    )
                    var1 = input("Enter first variable: ")
                    var2 = input("Enter second variable: ")
                    print("-"*150)
                    print(f'''Terminal:\n\nYour name is {var1} and you are {var2}''')
                    clear_screen()

                elif ask == '4':
                    print("-"*150)
                    print("Welcome to Multiple Arguments!")
                    print("-"*150)
                    print(
                        f'''print("Your full name: ", var1, "and you are", var2)\n'''
                    )
                    
                    var1 = input("Enter first variable: ")
                    var2 = input("Enter second variable: ")
                    print("-"*150)
                    print(f'''Terminal:\n\nYour full name: {var1} {var2} ''')
                    clear_screen()

                elif ask == '5':
                    print("Exiting...")
                    break

                else:
                    print("Invalid selection. Please choose a valid option.\n")

                      
        elif ask == 'q':
            print("Going to the main menu.")
            break
        else:
            print(f"[{ask}] <--- You entered an invalid input.")
                         
def variable(): #2 VARIABLE
    
    while True:
        text = "Variable"
        print("-"*150)
        print(f"|{text:^148}|")
        print("-"*150)
        print("[1] What is a Variable")
        print("[2] Example of Variable")
        print("[3] Go to main menu")
        print("-"*150)
        ask = input("Enter your choice: ")
        
        if ask.isnumeric():
            if ask == '1':
                clear_screen()
                print("Welcome to Variable")
                print("-"*150)
                print("What is variable?\n")
                print("   - A variable in Python is like a container that holds a value of a piece of data.\nIt's a way to store information that can be accessed and manipulated throughout a program.")
                print("-"*150)
                clear_screen()
                
                print("-"*150)
                print(
                    '''How to  declare a variable? First think of a unique name of it! Example are below.\n\nvariable_name = value\n\nx = 10\nname = "Jerwin"\nis_Student = True\n\nIn this example, x is a variable that stores the integer value '10', name is a variable that stores the string value "Jerwin", and is_student is a variable\nthat stores the boolean value True.\n\nNote You cannot use white space instead use "_" underscore.'''
                )
                print("-"*150)
                clear_screen()
                
                print("-"*150)
                print(
                    '''Multi Words Variable Names:\n\nVariable names with more than one word can be difficult to read.\nThere are several techniques you can use to make them more readable:\n\n[Camel Case]\nEach word, except the first, starts with a capital letter:\n\nmyVariableName = "Jerwin"\n\n[Pascal Case]\nEach word starts with a capital letter:\n\nMyVariableName = "Jerwin"\n\n[Snake Case]\nEach word is separated by an underscore character:\n\nmy_variable_name = "Jerwin"'''
                )
                print("-"*150)
                clear_screen()
            elif ask == '2':
                clear_screen()
                print("Variable sample: ")
                
                print("Now set a value to a variable")
                
                name = input("name = ")
                addy = input("address = ")
                print('''\nNow print the variable you just declared''')
                ask = input("(Y/N) to print: ").lower()
                print("\nOutput:")
                if ask == 'y':
                    print(f'''Your name: {name}, and your address: {addy}''')
                else:
                    print("okay.")
                clear_screen()
            elif ask == '3':
                print("going to main menu.")
                clear_screen()
                break
        else:
            print("Invalid input.")        

def Operators(): #3
    print("Welcome to Operators")
    print("-"*150)
    print(
        '''Operators in Python are symbols that perform operations on variables and values. Python\nsupports various types of operators, including arithmetic, comparison, assignment,\nand logical.'''
    )
    while True:
        print("-"*150)
        print(
            '''[1] Arithmetic Operators\n[2] Comparison Operators\n[3] Assignment Operators\n[4] Logical Operators\n[Q] to main menu'''
        )
        print("-"*150)
        ask = input("Select an Option: ").lower()
        
        
        if ask == '1':
            #NUMBER 1
            clear_screen()
            print("1. Arithmetic Operators: These operators are used to perform mathematical operations like\naddition, subtraction, multiplication, division, etc.")
            print("-"*150)
            print(
                '''Input:\n\nx = 10\ny = 5\nprint("Addition:", x + y)\nprint("Subtraction:, x - y"\nprint("Multiplication:", x * y)\nprint("Division", x / y)'''
            )
            print("-"*150)
            print("Output:\nAddition: 15\nSubtraction: 5\nMultiplication: 50\nDivision: 2")
            print("-"*150)
            clear_screen()
        
        elif ask == '2':
            #NUMBER 2
            clear_screen()
            print("-"*150)
            print("2. Comparison Operators: These operators are used to compare two values and return a Boolean\nvalue (True or False).")
            print("-"*150)
            print(
                '''Input:\n\nx = 10\ny = 5\nprint("Equal to:", x == y)\nprint("Not equal to:, x != y")\nprint("Greater than:", x > y)\nprint("Less than:", x < y)\nprint("Greater than or equal to:", x >= y)\nprint("Less than or equal to:", x <= y)'''
            )
            clear_screen()
            print("-"*150)
            print(f"Output:\n\nEqual to: False\nNot equal to: True\nGreater than: True\nLess than: False\nGreater than or equal to: True\nLess than or equal to: False")
            print("-"*150)
            
            clear_screen()
        
        elif ask == '3':
            #NUMBER 3
            clear_screen()
            print("-"*150)
            print("3. Assignment Operators: These operators are used to assign values to variables.")
            print("-"*150)
            print(
                '''Example:\n\n# Assignment operator (=)\ny = 10\nprint("y =", y)\n\n# Addition assignment operator (+=)\ny = 10\ny += 3\nprint("y = ",y)\n\n# Subtraction assignment operator (-=)\ny = 10\ny -= 2\nprint("y = ", y)\n# Multiplication assignment operator (*=)\n\ny = 5\ny *= 2\nprint("y = ",a)\n# Division assignment operator (/=)\n\ny = 10\ny /= 2\nprint("y =", y)'''
            )
            clear_screen()
            print("-"*150)
            print("Output:\n\ny = 10\ny = 13\ny = 8\ny = 10\ny = 5.0")
            clear_screen()
        
        elif ask == '4':
            #NUMBER 4 
            clear_screen()
            print("-"*150)
            print("4. Logical Operators: These operators are used to combine conditional statements.")
            print("-"*150)
            print(
                '''Input:\n\nx = 10\nprint(x > 5 and x < 15)\nprint(x > 15 or x < 5)\nprint(not x > 5)'''
            )
            print("-"*150)
            print("Output\n\nTrue\nFalse\nFalse")
            
            clear_screen()
        elif ask == 'q':
            print("Going to main menu")
            clear_screen()
            break
        else:
            print("You entered an invalid input.")
            clear_screen()
    
def conditionals(): #4
    print("-"*150)
    print("Welcome to Conditionals")
    print("-"*150)
    print(
        '''Conditionals are used to make decisions based on whether a certain\ncondition is true or false. In Python, the if, elif (short for "else if"),\nand else keywords are used to create conditional statements.\n\nHere's a brief explanation:'''
    )
    print("• if statement: The `if` statement is used to execute a block of code if a specified condition is true\nIt can be followed by an optional `elif` (else if) statement and an optional `else` statement.\n")
    print("• elif statement: The `elif` statement is used to check additional conditions `if`\nthe preceding if statement(s) are false. It allows you to check multiple conditions sequentially.\n")
    print("• else statement: The else statement is used to execute a block of code if none of the preceding\nif or elif statements are true. It is optional and can only appear at the end of an if statement.")
    print("-"*150)
    clear_screen()
    print("-"*150)
    print("Example:")
    print(
        '''if x > 5:\n   print("x is greater than 5")\nelif x == 5:\n   print("x is equal to 5")\nelse:\n   print("x is less than 5")'''
    )
    print("-"*150)
    print(
        '''\nIn this example, the if statement checks if `x` is greater than 5. If it is, it prints "x is greater\nthan 5". If `x`is not greater than 5, the `elif` statement checks if `x` is equal to 5. If it is, it prints\n"x is equal to 5". If neither condition is true, the else statement prints "`x` is less than 5".'''
    )
    clear_screen()
    
def loops(): #5
    
    while True:
        text = "Welcome to Loops"
        print("-"*150)
        print(f"|{text:^148}|")
        print("-"*150)
        print("This section of the menu will tackle two which is for loops and while loops!")
        print("[1] For loop section")
        print("[2] While loop section")
        print("[3] Go to main menu")
        print("-"*150)
        ask = input("Which one you want to go?: ").lower()
        
        if ask == 'q':
                print("going to the main menu.")
                clear_screen()
                break
            
        
        if ask.isalpha() or ask == '':
            print("Please input a appropriate value.")
        else:
            clear_screen()
            
            if ask == '1':
                while True:
                    text = "Welcome to For Loops"
                    print("-"*150)
                    print(f"|{text:^148}|")
                    print("-"*150)
                    print("[1] What is forloop?")
                    print("[2] Example programs For loop")
                    print("[Q] To quit.")
                    print("-"*150)
                    ask2 = input("Options: ")
                    
                    if ask2 == '1':
                        clear_screen()
                        print("-"*150)
                        print("What is a for loop?\n\n  - A for loop is used to iterate over a sequence (such as a list, tuple, string, or range)\nor other iterable objects. It executes a block of code for each item in the sequence.")
                        print(
                            '''\nExamples:\n\nnames = ['jerwin', 'nico','quijano']\nfor name in names:\n  print(names)\n\nOutput:\njerwin\nnico\nquijano'''
                            )
                        clear_screen()
                        print(
                            '''\nExample in using range it accepts 3 parameters which range(start,stoping point,step) now let's try!\n\nfor i in range(1,5):\n  print(i)\n\nOutput:\n1\n2\n3\n4'''
                            )
                        clear_screen()
                            
                    elif ask2 == '2':
                        while True:
                            clear_screen()   
                            print("For loop sample\n")
                            print("[1] Triangle")
                            print("[2] Hollow Square")
                            print("[3] Pyramid")
                            print("[Q] To exit")
                            print("-"*150)
                            in_ask = input("Options: ").lower()
                                
                            if in_ask == '1':
                                height = input("Enter the height of triangle: ")
                                
                                if height.isnumeric():
                                    height = int(height)
                                    for i in range(height):
                                        for j in range(1,i):
                                            print("*",end="")
                                        print()
                                else:
                                    print("invalid input.")
                                
                                        
                            elif in_ask == '2':
                                n = 5
                                for i in range(1,n+1):
                                    if i == 1 or i ==5:
                                        print("* * * * *")
                                    else:
                                        print("*       *")
                                
                            elif in_ask == '3':
                                n = input('Enter the height of your triangle: ')
                                if n.isnumeric():
                                    n = int(n)
                                    for i in range(n):
                                        for j in range(n,i,-1):
                                            print(" ",end="")
                                            
                                        for j in range(1,i):
                                            print("*",end="")
                                            
                                        for j in range(1,i-1):
                                            print("*",end="")
                                        print()
                                else:
                                    print("Invalid input.")
                                
                            elif in_ask == 'q':
                                print("exiting.")
                                clear_screen()
                                break
                    elif ask2 == 'q':
                        print("exiting.")
                        clear_screen()
                        break
                    else:
                        print("invalid input.")
                        
            elif ask == '2':
                while True:
                    print("-"*150)
                    print("\t\t\t\t\t\t\tWelcome to while loops")
                    print("-"*150)
                    print("[1] What is a while loop?")
                    print("[2] While loop sample programs")
                    print("[3] To exit.")
                    print("-"*150)
                
                    in_ask = input("Options: ").lower()

                    if in_ask == '1':
                        print("What is a while loop?\n\n  - A `while` loop is used to repeatedly execute a block of code as long as a specified\ncondition is true. It continues to execute the code block until the condition becomes false.")
                        
                        print(
                            '''\n\nExample:\n\ni = 1\nwhile i <= 5:\n  print(i)\n  i += 1\n\nOutput:\n1\n2\n3\n4\n5'''
                            )
                        clear_screen()
                        
                    elif in_ask == '2':
                        clear_screen()
                        while True:
                            print("While loop sample\n")
                            print("[1] Counting")
                            print("[2] Summing a number")
                            print("[3] Guessing game")
                            print("[4] To exit")
                            print("-"*150)
                            ask = input("Options: ").lower()
                            if ask.isnumeric():
                                if ask == '1': #counting
                                    i = 1
                                    while True:
                                        n = input("How many secs: ")
                                        if n == '' or n ==' ' or n.isalpha():
                                            print("invalid input.")
                                            continue
                                        else:
                                            n = int(n)
                                            while i < n + 1:
                                                print(f"Counting:{i:2}",end="\r")
                                                i += 1
                                                time.sleep(0.3)
                                            print("Counting done!")
                                            clear_screen()
                                            break
                                elif ask == '2': #summation of number
                                    count = 0
                                    total = 0
                                    ask = input("Enter how many number you want to sum: ")
                                    if ask.isnumeric():
                                        while True:
                                            ilan = input("Enter a number: ")
                                            if ilan.isnumeric():
                                                ilan = int(ilan)
                                                total += ilan
                                                count += 1
                                                if int(ask) == count:
                                                    print(f"The total summation of number is: {total:.2f}")
                                                    break
                                            else:
                                                print("That is not a number.")
                                                clear_screen()
                                    else:
                                        print("invalid input")           
                                    clear_screen()
                                elif ask == '3': #number guessing game
                                    random_number = ran.randint(1,10)
                                    di_pa_nahulaan = True

                                    while di_pa_nahulaan:
                                        
                                        ask = int(input("Enter your guess number from 1-10: "))
                                        
                                        if ask < random_number:
                                            print("\nGo higher.\n")
                                        elif ask > random_number:
                                            print("\nGo lower.\n")
                                        
                                        
                                        if ask == random_number:
                                            print(f"\nThe correct number is {ask}\nCongrats na hulaan mo.\n")
                                            in_ask = input('Enter gusto mo ulit mag laro?(Y/N): ').lower()
                                            if in_ask == 'y':
                                                random_number = ran.randint(1,10)
                                                continue
                                            elif in_ask == 'n':
                                                print("\nThank you for playing.\n")
                                                di_pa_nahulaan = False
                                            else:
                                                print("invalid input.")
                                    clear_screen() 
                                elif ask == '4':
                                    print("exiting.")
                                    clear_screen()
                                    break   
                            else:
                                print("invalid input.")
                    elif in_ask == '3':
                        clear_screen()
                        break 
                              
            elif ask == '3':
                break
              
def lists(): # 7
    while True:
        print("-"*150)
        print("\t\t\t\t\t\t\tWelcome to the List topic section!")
        print("-"*150)
        
        print("Choose a topic:")
        print("1. What is a list?")
        print("2. Operations on list")
        print("3. Example programs")
        print("-"*150)
        options = input("Enter your choice (PRESS Q TO QUIT): ").lower()
        
        if options == '1':
            clear_screen()
            print("-"*150)
            print("\t\t\t\t\t\t\t\tWhat is a list?")
            print("-"*150)
            print("  - A list is a data structure that is used to store a collection of items. Lists are ordered,\nmutable (changeable), and can contain elements of different data types. You can create a list by\nplacing comma-separated values inside square brackets [ ].")
        
            print(
            '''\nExample of a list:\n\nmy_list = [1, 2, 3, 4, 5]'''
            )
            clear_screen()
            
        elif options == '2':
            clear_screen()
            print("-"*150)
            print("\t\t\t\t\t\t\t\tOperations on list")
            print("-"*150)
            print("  - Operations on lists include adding elements, removing elements, accessing elements by index, and slicing lists.")
            
            clear_screen()
            while True:
                print("-"*150)
                print("List operations")
                print("-"*150)
                print("1. Adding elements")
                print("2. Removing elements")
                print("3. Accessing elements by index")
                print("4. Slicing lists")
                print("-"*150)
                options = input("Enter your choice (PRESS Q TO QUIT): ").lower()
                
                
                if options == '1':
                    clear_screen()
                    print("-"*150)
                    print(
                        '''Input:\nmy_list = [1, 2, 3, 'a', 'b', 'c']\n\n# Adding Element\nmy_list.append('jerwin')\nprint(my_list)'''
                    )
                    print("-"*150)
                    print(
                        "\nOutput:\n[1, 2, 3, 'a', 'b', 'c', 'jerwin']"
                    )

                    clear_screen()
                
                elif options == '2':
                    clear_screen()
                    print("-"*150)
                    print(
                        '''Input:\nmy_list = [1, 2, 3, 'a', 'b', 'c', 'jerwin']\n\n# Removing Elements\nmy_list.remove("jerwin")'''
                    )
                    print("-"*150)
                    print("\nOutput:\n[1, 2, 3, 'a', 'b', 'c']")
                    clear_screen()
                    
                
                elif options == '3':
                    clear_screen()
                    print("-"*150)
                    print(
                        '''Input:\nmy_list = [1, 2, 3, 'a', 'b', 'c','jerwin']\n\n# Accessing Elements\nprint(my_list[0])\nprint(my_list[-1])'''
                    )
                    print("-"*150)
                    print("\nOutput:\n1\njerwin")
                    clear_screen()
                
                elif options == '4':
                    clear_screen()
                    print("-"*150)
                    print(
                        '''Input:\nmy_list = [1, 2, 3, 'a', 'b', 'c','jerwin']\n\n# Slicing List\nprint(my_list[4:7])'''
                    )
                    print("-"*150)
                    print("\nOutput:\n['b','c', 'jerwin']")
                    clear_screen()  
                    
                elif options == 'q':
                    print("Going to the main menu.")
                    clear_screen()
                    break
                
                else:
                    print("you entered an invalid input.")
        elif options == '3':
            clear_screen()
            
            print("-"*150)
            print("Welcome to List example programs!")
            print("-"*150)
            print('There are 3 category Easy, Medium, and Hard.')
            print("1. Easy\n2. Medium\n3. Hard")
            print("-"*150)
            
            ask = input('Enter your choice: ')
            if ask =='' or ask ==' ' or ask.isalpha():
                print("enter a valid input.")
            else:
                if ask == '1':
                    expenses = []
                    while True:
                        # EASY LIST PROJECT
                        print("Welcome to Expenses Manager")
                        clear_screen()
                        print("-"*30)
                        print("Expenses Manager")
                        print("-"*30)
                        print("1. Add Expense\n2. View Expenses\n3. Calculate Total\n4. Exit")
                        print("-"*30)
                        choice = input("Enter your choice: ")

                        if choice == "1":
                                amount = input("Enter expense amount: ")
                                if amount == '' or amount == ' ' or amount.isalpha():
                                    print("please enter an Valid value")
                                else:
                                    amount = float(amount)
                                    expenses.append(amount)
                                    print(f"{amount}$ is added to expenses.")
                                clear_screen()
                        elif choice == "2":
                                clear_screen()
                                if len(expenses) == 0:
                                    print("You haven't put anything yet.")
                                else:
                                    print("-"*30)
                                    num = 1
                                    for item in expenses:
                                        print(f"[{num:0}]: {item:.2f}$")
                                        num += 1
                                    print("-"*30)
                                clear_screen()
                        elif choice == "3":
                                clear_screen()
                                if len(expenses) == 0:
                                    print("You haven't put anything yet.")
                                else:
                                    total = sum(expenses)
                                    print("-"*30)
                                    num = 1
                                    for item in expenses:
                                        print(f"[{num:0}]: {item:.2f}$")
                                        num += 1
                                    print("-"*30)
                                    print(f"Total epxenses: {total:.2f}$")
                                clear_screen()
                                    
                        elif choice == "4":
                            clear_screen()
                            break
                        else:
                            print("Invalid choice. Please try again.")
                            clear_screen()    
                elif ask =='2':
                    print("This example is Simple grading system using list.")
                    clear_screen()
                    # MEDIUM LIST EXAMPLE
                    grade = []
                    name2 = []
                    name = input("Enter your name: ").title()
                    course = input('Enter your section and course: ').upper()
                    while True:
                        ask = input("How many subjects: ")
                        if ask.isnumeric():
                            clear_screen()
                            ask = int(ask)
                            for i in range(1,ask+1):
                                while True:
                                    sub_name = input(f"Enter subject name for {i}: ").upper()
                                    if sub_name.isalnum():
                                        print(f"{sub_name} subject added.")
                                        name2.append(sub_name)
                                        break
                                    else:
                                        print("invalid value.")
                                        continue
                                while True:
                                    sub = input(f"Enter the grade of subject #{i}: ")
                                    print()
                                    if sub.isalpha() or sub == '' or sub == ' ':
                                        print("Please enter a valid value.")
                                        continue
                                    else:
                                        if int(sub) >= 101:
                                            print("You exceed the grading number.")
                                        else:  
                                            sub = int(sub)
                                            print(f"[ {sub} ] is added to the grade system.")
                                            print()
                                            grade.append(sub)    
                                            break 
                            clear_screen()     
                            average = sum(grade) / len(grade)
                            print()
                            text = "Report card"
                            print("-"*60)
                            print(f"{text:^60}")
                            print("-"*60)
                            print(f"{name: <50} {course}")
                            print("-"*60)

                            for names,subs in zip(name2,grade):
                                print(f"{names: <50} {subs}")
                            print("-"*60)
                            print(f"Average: {average:.2f}")
                            break   
                        else:
                            print("enter an appropirate value")
                            continue     
                elif ask == '3':
                    print('This Example program is a Todo list.')
                    clear_screen()
                    todo_list = []    
                    def view_list():
                        num = 1
                        for list in todo_list:
                            print(f"{num}: {list}")
                            num += 1
                        if len(todo_list) == 0:
                            print("No Havent put anything yet.")
                        print("-"*50)
                        
                    while True:
                        print("-"*50)
                        print("\t\t\t\b\b\bMenu")
                        print("-"*50)
                        print(
                            '''1. Add a Todo List\n2. View Todo list\n3. Update Todo list\n4. Delete Todo list\n5. Exit the app.'''
                        )
                        print("-"*50)
                        ask = input("Enter your options: ")

                        if ask.isalpha() or ask == '' or ask == ' ':
                            print("You entered an invalid input.")
                            clear_screen()
                        else:
                            if ask == '1':
                                clear_screen()
                                ask = input("How many items do you want to add?: ")
                                if ask == '' or ask ==' ' or ask.isalpha():
                                    print("invalid input.")
                                    clear_screen()
                                else:
                                    ask = int(ask)
                                    num = 0
                                    while num < ask:
                                        print("-" * 50)
                                        task = input("What do you want to add to the todo list?: ")
                                        todo_list.append(task)
                                        print(f"[ {task} ] Successfully added to the todo list!")
                                        num += 1
                                
                            elif ask == '2':
                                clear_screen()
                                view_list()
                                clear_screen()
                            
                            elif ask == '3':
                                clear_screen()
                                if len(todo_list) == 0:
                                    print("you haven't put anything yet.")
                                    clear_screen()
                                else:
                                    clear_screen()
                                    print("-"*50)
                                    view_list()
                                    ask = int(input("Enter a number you want to update: "))
                                    new_value = input("Enter the new value: ")
                                    prev = todo_list[ask - 1]
                                    todo_list[ask - 1] = new_value
                                    print(f"You change {prev} to {new_value}")
                                    clear_screen() 
                                    
                            elif ask == '4':
                                clear_screen()
                                if len(todo_list) == 0:
                                    print("you haven't put anything yet.")
                                    clear_screen()
                                else:
                                    view_list()
                                    ask = input("Enter the number you want to delete: ")
                                    if ask == ' ' or ask == '' or ask.isalpha():
                                        print("You entered an invalid input.")
                                    else:
                                        ask = int(ask)
                                        prev = todo_list[ask -1]
                                        todo_list.pop(ask - 1)
                                        print(f"{prev} is deleted to the list.")
                                    
                            elif ask == '5':
                                print("exiting the app.")
                                clear_screen()
                                break
                                
                            
                            elif options == 'q':
                                print("going to the main menu")
                                clear_screen()
                                break
                clear_screen()
        elif options == 'q':
            print('Exiting the List section.')
            clear_screen()
            break
        else:
            print('invalid input')
            clear_screen()

def define(): # 6
    while True:
        print("-"*150)
        print("\t\t\t\t\t\tWelcome to the Define or function Section of the menu!")
        print("-"*150)
        
        print("[1] What is function?")
        print("[2] Example uses of function")
        print("[3] To exit")
        
        print("-"*150)
        ask = input("Enter your input: ")
    
        if ask =='' or ask == ' ' or ask.isalpha():
            print("invalid input.")
            continue
        else:
            if ask == '1':
                    clear_screen()
                    print("-"*150)
                    print("What is function?")
                    print("-"*150)
                    print(
                        '''What is a Def in python?\n\n\t- def is a keyword used to define a function. A function is a block of reusable code\nthat performs a specific task. By using def, you can create your own functions to encapsulate\na set ofinstructions and execute them whenever needed.\n\n'''
                    )

                    print(
                        '''Here is some example syntax of a def:\n\ndef function_name(parameters):\n\t# Your code block\n\t# Perform the desired task\n\t# Optionally, return a value'''
                    )
                    clear_screen()
                    print(
                        '''\n\nLet us breakdown the example above!\n\n• [def] is use to start or to indicate the function\n\n• [Function name] you can give your function any name but!! there is a but!\nbe specific of name that you will give to the function.\n\n• (Parameters) Parameters is optional that you can pass in a function and it\nis also called a temporary variable inside your function!'''
                    )
                    
                    print(
                        '''\n• [ : ] A colon to indicate the function code block!'''
                    )
                    print("-"*150)
                    clear_screen()
                    print("-"*150)
                    
                    print(
                        '''Within the function's code block, you can write the instructions that define the behavior of the function.\nThis can include variable declarations, calculations, conditionals, loops, and more. You can also use the\nreturn statement to specify the value that the function should output.'''
                    )
                    print("\nHere is an example of a function that uses return.")
                    
                    print(
                        '''\ndef sqaure(num):\n   rel = num ** 2\n   return rel\n\nprint(square(10))\n\nOutput:\n100'''
                    )
                    print("-"*150)
                    clear_screen()
            elif ask == '2':
                while True:
                    clear_screen()
                    print("-"*150)
                    print("Welcome to Example of function")
                    print("-"*150)
                    print("[1] Function with arguments")
                    print("[2] Calling a function")
                    print("[Q] To exit")
                        
                    ask = input("Options: ").lower()
                    if ask == '1':
                        clear_screen()
                        print("-"*150)
                        print(
                                '''Information can be passed into functions as arguments.\n\nFunction with arguments:\n\ndef my_function(name1):\n  print(f"Hello, {name1}")'''
                            )
                        print("-"*150)
                        print("\nNow try it your self")
                            
                        ask = input("Enter a value: ")
                        print(f'''\nmy_function("{ask}")''')
                        print("Terminal\n")
                        print(f"Hello, {ask} ")
                        
                    elif ask == '2':
                        clear_screen()
                        print("Calling a function sample")
                        print("\nCall the function to work!")
                            
                        print(
                                '''\ndef plus():\n   ask1 = int(input('Enter a number: ))\n   ask2 = int(input('Enter a number: ))\n   rel = ask1 + ask2\n   print(f"The result is: {rel}")'''
                            )
                        print("-"*150)
                        while True:
                            ask = input("\nNow call the function: ").lower()
                                
                            if ask == "plus()":
                                in_ask1 = int(input("Enter a number: "))
                                in_ask2 = int(input("Enter a number: "))
                                print("The result is: ",in_ask1 + in_ask2)
                                break
                            else:
                                print("It seems that you call it wrong..")
                                continue   
                            
                    elif ask == 'q':
                        print("going to main menu.")
                        clear_screen()
                        break
                    else:
                            print("Invalid input.")
                        
            elif ask == '3':
                clear_screen()
                break
  
def display_menu():
    print("+","-"*50,"+")
    print("|  \t\t     MAIN MENU\t\t             |")
    print("+","-"*50,"+")
    print("|  [1] Print Statements\t\t\t\t     |")
    print("|  [2] Variables\t\t\t\t     |")
    print("|  [3] Operators\t\t\t\t     |")
    print("|  [4] Conditionals Statement\t\t\t     |")
    print("|  [5] Loops\t\t\t\t\t     |")
    print("|  [6] Functions\t\t\t\t     |")
    print("|  [7] List\t\t\t\t\t     |")
    print("+","-"*50,"+")

main_menu()
while True:
    display_menu()
    options = input("\nWhere do you want to go? Press (1/7) to explore the menu! (Q) for Exiting: ").lower()
    
    if options == '1':
        clear_screen()
        print_statements()
    elif options == '2':
        clear_screen()
        variable()
    elif options == '3':
        clear_screen()
        Operators()
    elif options == '4':
        clear_screen()
        conditionals()
    elif options == '5':
        clear_screen()
        loops()
    elif options == '6':
        clear_screen()
        define()
    elif options == '7':
        clear_screen()
        lists()
    elif options == 'q':
        print("Exiting the menu, goodbye!")
        clear_screen()
        break
    
    else:
        print("invalid input")
        clear_screen()
