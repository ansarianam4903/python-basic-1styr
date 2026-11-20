# 7.find the largest among three number.

a = float(input("Enter first Number: "))
b = float(input("Enter second Number: "))
c = float(input("Enter third Number: "))

if a >= b and a >= c:
    largest = a
elif b>=a and b >= c:
    largest = b
else:
    largest = c

print("larget number =", largest)
