def genPrimes():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last
## 모든 수는 소수의 배수인 것을 활용


def isprime(number):
	temp = []
	for n in range(1, number+1):
		if number % n == 0:
			temp.append(n)
	if len(temp) == 2:
		return True
	else:
		return False

def genPrime():
	n = 1
	while True:
		if isprime(n):
			yield n
		n += 1
## 소수 찾는 함수 따로 구현
