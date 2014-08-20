# 10001st prime

def nthprime(n):
	if n == 1:
		return 2
	else:
		count = 2
		number = 3
		while True:
			if prime(number):
				count += 1
				if count > n:
					break
			number += 2
		return number

def prime(number):
	if number <= 1:
		return False
	i = 2
	while i <= number** 0.5:
		if number%i == 0:
			return False
		i += 1

	return True

print nthprime(10001)

## 10001st prime is 104743