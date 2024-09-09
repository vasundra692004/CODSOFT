def addition(a,b):
    return a + b
def subtraction(a,b):
    return a - b
def multiply(a,b):
    return a * b
def division(a,b):
    if b == 0:
        return "can't divide it by 0 !"
    return a / b
print(" Select the operation")
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISION")

while True:
    option = input("ENTER THE CHOICE (1/2/3/4)")
    if option in ('1','2','3','4'):
        try:
            number1 = float(input("Enter the 1st Number : "))
            number2 = float(input("Enter the 2nd Number : "))
        except ValueError:
            print("invalid input")
            continue
    if option == '1':
        ans= addition(number1,number2)
    elif option == '2':
        ans = subtraction(number1,number2)
    elif option == '3':
        ans = multiply(number1,number2)
    elif option == '4':
         ans = division(number1,number2)
    print("Solution : ",ans)
    
