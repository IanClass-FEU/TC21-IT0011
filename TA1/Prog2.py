#PROGRAM 2: A program that will count the sum of the digits from a given input string digits.
def sum(s):
    total = 0
    for char in s:
        if char.isdigit():
            total += int(char)
    print("Sum:", total)

input_string = input("Enter string: ")
sum(input_string)