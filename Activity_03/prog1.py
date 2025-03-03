#3.1 Activity for performing String Manipulations
fname = input("Enter your first name: ")
lname = input("Enter your last name: ")
age = input("Enter your age: ")


full_name = fname + " " + lname


nickname = fname[:3]

greeting = f"Hello, {nickname}! Welcome. You are {age} years old."


print("\nFull Name:", full_name)
print("Nickname:", nickname)
print (greeting)
