import math
n = input("Enter Value of N ")
for i in range(1,n+1):
    print((n-i)*" "),
    print("1"),
    for j in range(1, i+1):
        print(math.factorial(i)/(math.factorial(j)*(math.factorial(i-j)))),
    print
