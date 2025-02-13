def is_palindrome(n):
    return str(n) == str(n)[::-1]

f = open("./Technical_Midterm/numbers.txt", "r")

line_number = 1
line = f.readline()

while line:
    numbers = line.strip().split(',')
    int_numbers = [int(num) for num in numbers if num.strip()]
    total_sum = sum(int_numbers)

    if is_palindrome(total_sum):
        result = "Palindrome"
    else:
        result = "Not a palindrome"
    print(f"Line {line_number}: {','.join(numbers)} (sum {total_sum}) - {result}")

    line_number += 1
    line = f.readline()

f.close()