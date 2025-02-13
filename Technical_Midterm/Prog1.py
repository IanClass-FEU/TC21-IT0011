def is_palindrome(n):
    return str(n) == str(n)[::-1]

#
file_path = r"Technical_Midterm\numbers.txt"


try:
    with open(file_path, "r") as f:
        line_number = 1

        for line in f:
            line = line.strip()
            if not line:
                continue

            numbers = line.split(',')
            try:
                int_numbers = [int(num.strip()) for num in numbers if num.strip().isdigit()]
                total_sum = sum(int_numbers)
                
                result = "Palindrome" if is_palindrome(total_sum) else "Not a palindrome"
                print(f"Line {line_number}: {','.join(numbers)} (sum {total_sum}) - {result}")

            except ValueError:
                print(f"Line {line_number}: Error - Non-numeric value found")

            line_number += 1

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
