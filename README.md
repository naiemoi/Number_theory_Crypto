MD. Naiem 
IT-23025
Part 1: Number Theory & Cryptography (Day 1.pdf)
Euclid's Algorithm (GCD): gcd(a, b) = gcd(b, a mod b) for a >= b > 0[cite: 56]. Runs in at most log₂(a) + log₂(b) iterations.
Extended Euclid's Algorithm: Finds integers x, y such that a*x + b*y = gcd(a, b)[cite: 50].
LCM: lcm(a, b) = (a * b) / gcd(a, b).
Diophantine Equations: a*x + b*y = c has integer solutions iff gcd(a, b) | c[cite: 87]. From one solution (x₀, y₀), all solutions are x = x₀ + t*q and y = y₀ - t*p (where a = d*p, b = d*q, d = gcd(a, b))[cite: 102, 111].
Modular Inverse & Division: Inverse exists iff gcd(a, n) = 1[cite: 133]. Using n*t + a*s = 1, modular division is b / a ≡ b * s (mod n).
Chinese Remainder Theorem (CRT): If gcd(a, b) = 1 and a*x + b*y = 1, the unique solution n (mod a*b) to n ≡ r_a (mod a) and n ≡ r_b (mod b) is n = r_a * b*y + r_b * a*x[cite: 194, 209].
Fast Modular Exponentiation: Computes b^e (mod m) using binary representation of e and repeated squaring in at most 2 * log₂(e) multiplications.
Fermat's Little Theorem: If prime p does not divide a, a^(p - 1) ≡ 1 (mod p)[cite: 256].
Euler's Totient & Theorem: φ(n) counts integers in [0, n - 1] coprime to n (φ(p) = p - 1, φ(p*q) = (p - 1)(q - 1))[cite: 287, 292, 294]. If gcd(a, n) = 1, then a^φ(n) ≡ 1 (mod n).
Part 2: Prime Numbers (Day 2.pdf)
Infinitude of Primes: Proved via Euclid's proof (∏pᵢ + 1)[cite: 311], n! + 1, harmonic series divergence, Fermat numbers (2^(2^n) + 1), and Filip Saidak's proof.
Distribution:
Dirichlet's Theorem: Infinitely many primes of form a*k + b iff gcd(a, b) = 1[cite: 316].
Prime Number Theorem: Asymptotically, π(x) = x / log x.
Conjectures: Goldbach (even > 3 = p₁ + p₂)[cite: 318], Waring (odd > 3 is prime or sum of 3 primes), Twin Primes, and a prime between n² and (n + 1)².
Primality Testing:
Sieving & Trial Division: Check primes <= √n (optimized with Wheeling)[cite: 322].
Fermat's Test & Carmichael Numbers: Composite numbers where a^n ≡ a (mod n) for all a (e.g., 561, 1105, 1729).
Lucas' & n - 1 Tests: n is prime if for prime factors q of n - 1, a^(n - 1) ≡ 1 (mod n) and a^((n - 1)/q) ≢ 1 (mod n).
Lucas-Lehmer Test: Tests 2^p - 1 using l(1) = 4, l(n) = l(n - 1)² - 2[cite: 330].
Special Numbers:
Mersenne Primes (2^n - 1) & Perfect Numbers (6, 28, 496, 8128).
Antiprimes: Numbers with more divisors than any smaller positive integer; total divisors d(n) = (a₁ + 1)(a₂ + 1)...(aₖ + 1)