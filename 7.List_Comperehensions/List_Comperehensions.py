x = int(input("Please enter a number :"))
y = int(input("Please enter a number :"))
z = int(input("Please enter a number :"))
n = int(input("Please enter a number :"))
print(
    list([i,j,k]
    for i in range ( x + 1)
    for j in range ( y + 1)
    for k in range ( z + 1)
 if i+j+k != n   ))



