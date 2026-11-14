# Number Theory and Cryptography

These notes introduce key ideas from elementary number theory, modular
arithmetic, and prime numbers.

## Part 1: Number Theory and Cryptography

### 1. Euclidean Algorithm (GCD)

The Euclidean algorithm finds the greatest common divisor (GCD) of two
integers by repeatedly replacing the pair with the divisor and remainder:

$$
\gcd(a,b)=\gcd(b,\;a\bmod b)
$$

Repeat until the remainder is zero. The last nonzero remainder is the GCD.

### 2. Extended Euclidean Algorithm

The extended Euclidean algorithm finds the GCD and integers $x$ and $y$ such
that:

$$
ax+by=\gcd(a,b)
$$

These coefficients are useful for finding modular inverses and solving
Diophantine equations.

### 3. Least Common Multiple (LCM)

The least common multiple is the smallest positive integer divisible by both
integers. For nonzero $a$ and $b$:

$$
\operatorname{lcm}(a,b)=\frac{|ab|}{\gcd(a,b)}
$$

### 4. Linear Diophantine Equations

A linear Diophantine equation has the form $ax+by=c$, where integer solutions
are required. A solution exists exactly when $\gcd(a,b)$ divides $c$.

If $(x_0,y_0)$ is one solution, let $d=\gcd(a,b)$. All integer solutions are:

$$
x=x_0+t\frac{b}{d},\qquad
y=y_0-t\frac{a}{d},\qquad t\in\mathbb Z
$$

### 5. Modular Inverse and Division

The modular inverse of $a$ modulo $n$ is an integer $s$ satisfying:

$$
as\equiv1\pmod n
$$

It exists exactly when $\gcd(a,n)=1$. When it exists, division by $a$ modulo
$n$ means multiplying by its inverse:

$$
\frac{b}{a}\equiv bs\pmod n
$$

### 6. Chinese Remainder Theorem (CRT)

The Chinese Remainder Theorem combines congruences with pairwise-coprime
moduli. It guarantees a unique solution modulo the product of those moduli.

For two coprime moduli $a$ and $b$, choose $x$ and $y$ such that $ax+by=1$.
The solution to $n\equiv r_a\pmod a$ and $n\equiv r_b\pmod b$ is:

$$
n\equiv r_a\,by+r_b\,ax\pmod{ab}
$$

### 7. Fast Modular Exponentiation

Fast modular exponentiation computes $b^e\bmod m$ using the binary
representation of $e$ and repeated squaring. It needs only
$O(\log e)$ modular multiplications, making it practical for very large
exponents.

### 8. Fermat's Little Theorem

If $p$ is prime and $p$ does not divide $a$, then:

$$
a^{p-1}\equiv1\pmod p
$$

The theorem is useful in modular arithmetic and in probabilistic primality
tests.

### 9. Euler's Totient Function and Theorem

Euler's totient function $\varphi(n)$ counts the positive integers up to $n$
that are relatively prime to $n$. For example, $\varphi(p)=p-1$ for a prime
$p$, and $\varphi(pq)=(p-1)(q-1)$ for distinct primes $p$ and $q$.

Euler's theorem states that, when $\gcd(a,n)=1$:

$$
a^{\varphi(n)}\equiv1\pmod n
$$

## Part 2: Prime Numbers

### 1. Infinitude of Primes

A prime number is an integer greater than $1$ whose only positive divisors are
$1$ and itself. Euclid's proof shows that there are infinitely many primes.

### 2. Prime Distribution

Prime distribution studies how primes occur among the natural numbers.

- **Dirichlet's theorem:** If $\gcd(a,b)=1$, the arithmetic progression
  $a k+b$ contains infinitely many primes.
- **Prime Number Theorem:** The number $\pi(x)$ of primes up to $x$ is
  approximately:

  $$
  \pi(x)\sim\frac{x}{\ln x}
  $$

### 3. Famous Prime Number Conjectures

- **Goldbach's conjecture:** Every even integer greater than $2$ is the sum
  of two primes.
- **Weak Goldbach theorem:** Every odd integer greater than $5$ is the sum
  of three odd primes. This statement was historically known as the weak
  Goldbach conjecture and is now proven.
- **Twin prime conjecture:** There are infinitely many pairs of primes that
  differ by $2$.
- **Legendre's conjecture:** There is at least one prime between every pair
  of consecutive perfect squares.

### 4. Primality Testing

Primality tests determine whether a number is prime or composite. Common
methods include:

- **Trial division:** Checks possible divisors up to the square root of the
  number.
- **Sieve of Eratosthenes:** Finds all primes within a specified range.
- **Fermat's test:** Uses Fermat's Little Theorem to identify probable primes.
  Some composite numbers pass the test; Carmichael numbers, such as $561$,
  pass for every base coprime to the number.
- **Lucas primality test:** Uses the prime factors of $n-1$ and suitable
  modular congruences to prove that $n$ is prime.
- **Lucas-Lehmer test:** Tests whether a Mersenne number
  $M_p=2^p-1$ is prime. For an odd prime $p$, start with $s_1=4$ and
  repeatedly calculate $s_{k+1}=s_k^2-2$ modulo $M_p$; $M_p$ is prime exactly
  when $s_{p-1}\equiv0\pmod{M_p}$.

### 5. Special Numbers

- **Mersenne primes:** Primes of the form $2^p-1$. If $2^p-1$ is prime, then
  $p$ must also be prime.
- **Perfect numbers:** Positive integers equal to the sum of their proper
  divisors. Examples include $6$, $28$, $496$, and $8128$. Every even perfect
  number has the form $2^{p-1}(2^p-1)$ for a Mersenne prime $2^p-1$.
- **Antiprimes (highly composite numbers):** Positive integers with more
  divisors than any smaller positive integer.

If the prime factorization of $n$ is
$n=p_1^{a_1}p_2^{a_2}\cdots p_k^{a_k}$, its number of positive divisors is:

$$
d(n)=(a_1+1)(a_2+1)\cdots(a_k+1)
$$
