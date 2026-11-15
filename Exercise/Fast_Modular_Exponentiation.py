def mod_exp(b, e, m):
    result = 1
    b = b % m
    while e > 0:
        if e % 2 == 1:
            result = (result * b) % m
        b = (b * b) % m
        e //= 2
    return result

b = int(input("Enter base (b): "))
e = int(input("Enter exponent (e): "))
m = int(input("Enter modulus (m): "))
print("Result (b^e mod m):", mod_exp(b, e, m))