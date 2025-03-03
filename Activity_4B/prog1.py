A = {'a', 'b', 'c', 'd', 'f', 'g'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

print("a.", A & B, "Count:", len(A & B))
print("b.", B - (A | C), "Count:", len(B - (A | C)))
print("i.", C - A)
print("ii.", A & C)
print("iii.", (A & B) | {'h'})
print("iv.", (A & C) - B)
print("v.", A & B & C)
print("vi.", B - (A | C))