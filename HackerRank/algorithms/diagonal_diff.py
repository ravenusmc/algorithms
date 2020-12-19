# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
# For example, the square matrix arr  is shown below:
# URL https://www.hackerrank.com/challenges/diagonal-difference/problem?h_r=next-challenge&h_v=zen
# Rank: 1,670,172

arr = [
[1, 2, 3],
[4, 5, 6],
[9, 8, 9]
]

# arr = [
# [1, 2, 3, 4],
# [4, 5, 6, 7],
# [9, 8, 9, 6],
# [4, 5, 6, 7],
# ]

def diagonalDifference(arr):
	left_to_right_sum = 0
	count_left = 0
	while count_left < len(arr):
		left_to_right_sum = arr[count_left][count_left] + left_to_right_sum
		count_left  += 1
	right_to_left_sum = 0
	count_up = 0
	count_right = len(arr) - 1
	while count_right >= 0:
		right_to_left_sum = arr[count_up][count_right] + right_to_left_sum
		count_up += 1
		count_right -= 1
	absolute_difference = abs(left_to_right_sum - right_to_left_sum)
	return absolute_difference

absolute_difference = diagonalDifference(arr)
print(absolute_difference)

