def num_primes(num: int) -> int:
    num_primes = 0
    for i in range(2, num):
        is_prime = True
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                is_prime = False
        if is_prime:
            num_primes += 1
    return num_primes

assert num_primes(1) == 0
assert num_primes(2) == 0
assert num_primes(3) == 1
assert num_primes(4) == 2
assert num_primes(5) == 2
assert num_primes(6) == 3
assert num_primes(100) == 25
assert num_primes(1000) == 168
assert num_primes(10000) == 1229
