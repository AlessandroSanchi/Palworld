# ESERCIZIO 5
# Write a program that asks the user for their age and prints out whether they are a child (age 0-12),
# teenager (age 13-19), adult (age 20-64), or senior (age 65+).

age = int(input("insert age: "))
if age <= 12:
    print("Child")
elif age > 12 and age <= 19:
        print("Teenager")
elif age > 19 and age <= 64:
        print("Adult")
elif age >= 65:
    print("Senior")
else:
    print("Error")
        