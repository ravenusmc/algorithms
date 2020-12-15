# The provided code stub reads and integer, , from STDIN. For all non-negative integers i < n, print i^2.
# https://www.hackerrank.com/challenges/python-loops/problem?h_r=next-challenge&h_v=zen

def print_squares(integer):
	count = 0
	while count < integer: 
		squared = count ** 2 
		print(squared)
		count += 1

print_squares(integer)		
print_squares(4)
