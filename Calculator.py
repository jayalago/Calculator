#Very simple calculator program

#Functionality of the calculator
class Calculator:
    def add(self, a, b):
        return a + b
    def sub(self, a, b):
        return a - b
    def mul(self, a, b):
        return a * b
    def div(self, a, b):
        if b == 0:
            print("Division by zero")
        return a / b
    def print_result(self, result):
        print("The result is:", result)

#Optics of the calculator
class main:
    calc = Calculator()
    #Main menu options
    print("***Welcome to Calculator***")
    print("1) add \n2) sub \n3) mul \n4) div ")
    choice = int(input("Enter your choice (1,2,3,4): "))
    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter second number: "))
    #Choice = From user input
    if choice == 1: #add
        result = calc.add(num_1, num_2)
        calc.print_result(result)
    elif choice == 2: #subtract
        result = calc.sub(num_1, num_2)
        calc.print_result(result)
    elif choice == 3: #multiplication
        result = calc.mul(num_1, num_2)
        calc.print_result(result)
    elif choice == 4: #division
        result = calc.div(num_1, num_2)
        calc.print_result(result)
    else:
        print("Invalid choice")

