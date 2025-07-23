class Solution:
    def countNumbers(self, n):
        import math

        # Use a reasonable limit for prime generation
        LIMIT = int(n ** 0.5) + 1
        is_prime = [True] * (LIMIT + 1)
        is_prime[0] = is_prime[1] = False
        primes = []

        for i in range(2, LIMIT + 1):
            if is_prime[i]:
                primes.append(i)
                for j in range(i * i, LIMIT + 1, i):
                    is_prime[j] = False

        count = 0
        numbers = set()

        # Case 1: p^8
        for p in primes:
            val = p ** 8
            if val <= n:
                numbers.add(val)
            else:
                break

        # Case 2: p^2 * q^2
        for i in range(len(primes)):
            for j in range(i + 1, len(primes)):
                val = (primes[i] ** 2) * (primes[j] ** 2)
                if val <= n:
                    numbers.add(val)
                else:
                    break

        return len(numbers)
