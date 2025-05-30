print("1 _ add")    
print("2 _ subtract")
print("3 _ multiply")
print("4 _ divide")                 
result = 0 
option = input("Choose an operation: ")

if option in ["1", "2", "3", "4"]:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if option == "1":
        result = num1 + num2 
    elif option == "2":
        result = num1 - num2 
    elif option == "3":
        result = num1 * num2 
    elif option == "4":
         result = num1 // num2 
        
else: 
    result = "Invalid option entered"

print("The result of the operation is:", result)
