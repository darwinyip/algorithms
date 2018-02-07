import math

def primeFactorization(x):
	primes = []
	if x <= 1:
		return primes

	for i in range(2, x+1):
		while x % i == 0:
			primes.append(i)
			x //= i
	return primes


if __name__ == '__main__':
	for i in range(20):
		print(primeFactorization(i))
