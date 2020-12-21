# Given five positive integers, find the minimum and maximum values that can be calculated by 
# summing exactly four of the five integers. Then print the respective minimum and maximum values as a 
# single line of two space-separated long integers.
# URL: https://www.hackerrank.com/challenges/mini-max-sum/problem
# Rank: 1,338,720

# arr = [1, 2, 3, 4, 5]
# arr = [1, 3, 5, 7, 9]
arr = [769082435, 210437958, 673982045, 375809214, 380564127]
#expected_output = 1640793344 2199437821

def miniMaxSum(arr):
	index = 0
	max_sum = 0
	min_sum = sum(arr)
	while index < len(arr):
		changed_list = arr.copy()
		changed_list.pop(index)
		temp_max_sum = sum(changed_list)
		temp_min_sum = sum(changed_list)
		if temp_max_sum > max_sum:
			max_sum = temp_max_sum
		if temp_min_sum < min_sum:
			min_sum = temp_min_sum
		index += 1 
	print(min_sum, max_sum)

miniMaxSum(arr)