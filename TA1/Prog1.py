#A program that will display the number of vowels, consonants, spaces, and other characters given an input string
def count_chars(s):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    spaces  = 0
    vowels_count = 0
    consonants_count = 0
    others = 0
    
    for char in s:
        if char in vowels:
            vowels_count += 1
        elif char in consonants:
            consonants_count += 1
        elif char == " ":
            spaces += 1
        else:
            others += 1
    
    print("Vowels:", vowels_count)
    print("Consonants:", consonants_count)
    print("Spaces:", spaces)
    print("Others:", others)

input_string = input("Enter a string: ")
count_chars(input_string)
