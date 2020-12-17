
# In this challenge, you are required to calculate and print the sum of the elements in an array, keeping in 
# mind that some of those integers may be quite large.
# URL: https://www.hackerrank.com/challenges/a-very-big-sum/problem
# Rank: 1,885,438

ar = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

def aVeryBigSum(ar):
	count = 0
	for value in ar: 
		count = value + count 
	return count 

count = aVeryBigSum(ar)
print(count)