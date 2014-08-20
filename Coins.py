coins = [200,100,50,20,10,5,2,1]

def ways(n,m):
	if n < 0 or m >= len(coins):
		return 0
	elif n == 0:
		return 1
	else:
		return ways(n-coins[m], m) + ways(n, m+1)

print ways(200,0)