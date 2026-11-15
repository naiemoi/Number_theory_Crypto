def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    d, p, q = extended_gcd(b, a % b)
    x = q
    y = p - (a // b) * q
    return d, x, y

a = int(input("Enter a: "))
b = int(input("Enter b: "))
d, x, y = extended_gcd(a, b)
print(f"GCD: {d}, x: {x}, y: {y} ({a}*{x} + {b}*{y} = {d})")