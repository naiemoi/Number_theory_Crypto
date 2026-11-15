def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))
print("LCM:", lcm(a, b))