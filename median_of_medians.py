def median_of_medians(arr, index):
	
	# compute the median of medians using the helper function given below
	mom =  get_median_of_medians(arr)
	
	# partition aroun the median of medians calculated. Thhis sould be done in place, but we have done 
	# this using O(n) space. This is also O(n) time.
	new_arr = []
	for el in arr:
		if el < mom:
			new_arr.append(el)
	k = len(new_arr)
	new_arr.append(mom)
	for el in arr:
		if el > mom:
			new_arr.append(el)

	# Cases we could have
	if k == index:
		return mom
	elif k > index:
		return median_of_medians(new_arr[0:k], index)
	else:
		return median_of_medians(new_arr[k+1: len(new_arr)], index - k)

def get_median_of_medians(arr):

	# Base case: lenght of array is 1
	if len(arr) == 1:
		return arr[0]

	#Otherwise break array into chunks of n/5 and calculate for each o them separately
	else:
		medians = []
		for i in xrange((len(arr)-1)/5 +1):
			if i*5+5 > len(arr):
				b = arr[i*5:len(arr)]
			else:
				b = arr[i*5:i*5+5]

			b.sort()
			medians.append(b[len(b)/2])

		return get_median_of_medians(medians)

# Test case
a = [2,4,7,10,1,3,5,9,8,6]
print a
print median_of_medians(a, 0)