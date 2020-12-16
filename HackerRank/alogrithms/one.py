# Given an array of integers, find the sum of its elements.
# For example, if the array ar = [1,2,3], 1 + 2 + 3 = 6 , so return 6.
# https://www.hackerrank.com/challenges/simple-array-sum/problem

def simpleArraySum(ar):
	count = 0
	for a in ar: 
		count = a + count 
	return count


ar = [1, 2, 3, 4, 10, 11]
list_sum = simpleArraySum(ar)
print(list_sum)