
# ESERCIZIO 6
# 1. Ask the user for two numbers
# 2. Convert the user's input to integers
# 3. Use if-else statements and logical operators to determine whether the numbers are both even, both odd, or one even and one odd
# 4. Print out the result

number1 = int(input("Insert first number: "))
number2 = int(input("Insert second number: "))

if number1 % 2 == 0 and number2 % 2 == 0:
    print("both even") 

elif number1 % 2 == 1 and number2 % 2 == 1:
    print("both odd") 

elif number1 % 2 == 1 and number2 % 2 == 0:
    print("one number is even and one is odd")

elif number2 % 2 == 1 and number1 % 2 == 0:
    print("one number is even and one is odd")
    
else:
    print("Error")