#3.2 Activity for Performing String Manipulations
fname = input("Enter your first name: ")
lname = input("Enter your last name: ")

full_name = fname + " " + lname

full_nameUP = full_name.upper()
full_namelow = full_name.lower()

full_nameLen = len(full_name)   


print("\nFull Name:", full_name)
print("Full Name (Upper Case):", full_nameUP)
print("Full Name (Lower Case):", full_namelow)
print("Length of Full Name:", full_nameLen)
