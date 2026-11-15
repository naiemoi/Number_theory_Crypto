def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
print("GCD:", gcd(a, b))