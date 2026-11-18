# Ask the user to input their age
age = int(input("Please enter your age: "))
# Creating the if, elif and else statements in logical order. 
if age > 100: 
    print("Sorry, you are dead")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hill.")
elif age == 21:
    print("Congrats on your 21st!")
elif age < 13:
    print("You qualify for the kiddie discount.")
else:
    print("Age is but a number.")