#Program 3a - nested for statement
def pattern_a(n):
    for i in range(1, n+1):
        print(" " * (n - i) + "".join(str(x) for x in range(1, i + 1)))

#Program 3b - nested while statement
def pattern_b(n):
    count = 1
    while count <= n:
        if count % 2 == 1:
             print(str(count) * (2 * count - 1))
        count += 1

n_a = int(input("enter the number of rows for pattern a: "))
pattern_a(n_a)
n_b = int(input("enter the number of rows for pattern b: "))
pattern_b(n_b)

