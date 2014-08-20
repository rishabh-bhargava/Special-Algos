def coin_partition(x):
	print ways(x,x)

d = {}

def ways(n,m):
	if n<0 or m < 1:
		return 0
	elif n ==0:
		return 1
	else:
		return ways(n-m, m) + ways(n, m-1)

coin_partition(6)