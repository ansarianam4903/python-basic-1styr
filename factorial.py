
num = int(input("Enter a number: "))

factorial = 1

if num < 0:
    print("factorial not defined for negative numbers")

else:
    for i in range(1, num + 1):
        factorial *= i

        print("Factorial =", factorial)