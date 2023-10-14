print("Select any one in given operation:")
print("1 Addition")
print("2 Subtraction")  
print("3 Multiplication")
print("4 Division")

operation = input()

if operation == "1":
    num1 = input("Enter the first value:")
    num2 = input("Enter the second value:")
    print("The sum is " + str(int(num1) + int(num2)))
elif operation == "2":
    num1 = input("Enter the first value:")
    num2 = input("Enter the Second Value:")
    print("The difference is " + str(int(num1) - int(num2)))
elif operation == "3":
    num1 = input("Enter the first value:")
    num2 = input("Enter the Second Value:")
    print("The difference is " + str(int(num1) * int(num2)))
elif operation == "4":
    num1 = input("Enter the first value:")
    num2 = input("Enter the Second Value:")
    print("The difference is " + str(int(num1) / int(num2)))   
else:
    print("Invalid operation")   
