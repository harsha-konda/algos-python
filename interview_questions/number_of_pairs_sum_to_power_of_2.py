# https://www.geeksforgeeks.org/number-of-pairs-whose-sum-is-a-power-of-2/
# uber

def countPairs(arr):
    arr = sorted(arr,reverse = True)
	dic = {}
	for ele in arr:
		if ele not in dic:
			dic[ele] = 0
		dic[ele] +=1

	count = 0
	for ele in arr:
		cur = 1
		while(cur<ele):
			cur <<= 1

		if cur - ele in dic and dic[cur-ele]>0:
			count+=1
			dic[cur-ele] -= 1
	return count

if __name__ == '__main__':
	assert(countPairs([ 3, 11, 14, 5, 13 ])==2)
