#!/usr/bin/env python
def main():
    operation = input("What operation would like to perform? OPTIONS: 'add', 'subtract','divide','multiply', or 'quit' to quit: ").lower()
    while(operation == 'add' or operation == 'subtract' or operation == 'divide' or operation == 'multiply'):
        x = float(input("Enter in a number: "))
        y = float(input("Enter ANOTHER  number: "))
        def calculate(x,y):
            if(operation == "add"):
                print(x+y)
            elif(operation == "subtract"):
                print(x-y)
            elif(operation == "multiply"):
                print(x * y)
            elif(operation == "divide"):
                if y != 0:
                    print(x / y)
                else:
                    print("You can't divide by zero!")
        calculate(x,y)  
        operation = input("If you would like to calculate something new, enter the operation you want to perform? OPTIONS: 'add', 'subtract', 'divide', 'multiply', or 'quit' to quit: ").lower()
if __name__ == "__main__":
    main()
