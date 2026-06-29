# Mini_Project
# Create Calculator
'''Features
➕ Addition
➖ Subtraction
✖ Multiplication
➗ Division
// Floor Division
% Modulus
** Power
√ Square Root
Exit Option'''

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b


def div(a,b):
    if b == 0:
        return("Cannot Divided By Zero")
    return a/b

def floor_div(a,b):
    if b == 0:
        return("Cannot Divided By Zero")
    return a//b

def modules(a,b):
    if b == 0:
        return("Cannot Divided By Zero")
    return a%b

def power(a,b):
    return a**b



def square(a,b):
    return a**b


# main loop
while True:
    print("\n ===============Python Calculater==============")
    print("1. Addition")
    print("2. Substraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("6. Modules")
    print("7. Power")
    print("8. Square Root")
    print("9. Exit")

    
    
    choice = input("\n Enter Your Chice")
    
    if choice == "9":
        print("\nThank you for using the calculator!")
        break

    elif choice == "8":
        num = float(input("Enter The Value"))
        num2 = float(input("Enter The Value"))
        print("Square Root:",square(num,num2))
        continue

    if choice in ["1","2","3","4","5","6","7"]:
        num1 = int(input("Enter The Number 1"))
        num2 = int(input("Enter The Number 2"))

        if choice == "1":
            print("Addition:",add(num1,num2))
        elif choice == "2":
            print("Substraction:",sub(num1,num2))
        elif choice == "3":
            print("Multiplication:",mult(num1,num2))
        elif choice == "4":
            print("Division:",div(num1,num2))
        elif choice == "5":
            print("Floor Division:",floor_div(num1,num2))
        elif choice == "6":
            print("Modules:",modules(num1,num2))
        elif choice == "7":
            print("Power:",power(num1,num2))
        

    else:
        print("Please Enter Valid Number!")

    


    
