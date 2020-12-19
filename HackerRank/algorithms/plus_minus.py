# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
# Print the decimal value of each fraction on a new line with  places after the decimal.
# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, 
# though answers with absolute error of up to  are acceptable.
# URL: https://www.hackerrank.com/challenges/plus-minus/problem
# rank: 1,537,742

arr = [-4, 3, -9, 0, 4, 1]

def plusMinus(arr):
	total_items = len(arr)
	positive_count = 0
	negative_count = 0
	zero_count = 0
	for number in arr:
		if number > 0:
			positive_count = positive_count + 1 
		elif number < 0: 
			negative_count = negative_count + 1 
		else:
			zero_count = zero_count + 1 
	positive_values_percentage = positive_count / total_items
	negative_values_percentage = negative_count / total_items
	zero_count_percentage = zero_count / total_items
	print(positive_values_percentage)
	print(negative_values_percentage)
	print(zero_count_percentage)

plusMinus(arr)