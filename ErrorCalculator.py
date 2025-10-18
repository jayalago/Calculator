#calculator class
class Calculator:
    #adds a + b
    def add(self, a, b):
        return a + b
    #subtracts a - b
    def sub(self, a, b):
        return a - b
    #multipys a * b
    def mul(self, a, b):
        return a * b
    #divids a/b but not if b = 0
    def div(self, a, b):
        if b == 0:
            print("Division by zero")
        return a / b
    #prints result
    def print_result(self, result):
        print("The result is:",result)
    # main menu
    print("***Welcome to Calculator***")
    print("1) add")
    print("2) sub")
    print("3) mul")
    print("4) div")
    #var
    calc = Calculator()
    choice = int(input("Enter your choice (1,2,3,4): "))
    num_1 = int(input("Enter first number: "))
    num_2 = int(input("Enter second number: "))
    # Choice
    if choice == 1:  # add
        result = calc.add(num_1, num_2)
        #prints result
        print(f"Result: {result}")
    elif choice == 2:  # subtract
        result = calc.sub(num_1, num_2)
        # prints result
        print(f"Result: {result}")
    elif choice == 3:  # multiplication
        result = calc.mul(num_1, num_2)
        # prints result
        print(f"Result: {result}")
    elif choice == 4:  # division
        result = calc.div(num_1, num_2)
        # prints result
        print(f"Result: {result}")
    else:
        print("Invalid choice")