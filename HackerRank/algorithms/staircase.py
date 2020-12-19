# Staircase detail
# This is a staircase of size :
#   #
#  ##
# ### 
# Its base and height are both equal to . It is drawn using #symbols and spaces. The last line is not preceded by any spaces.
# Write a program that prints a staircase of size .
# URL: https://www.hackerrank.com/challenges/staircase/problem
# rank: 1,429,203

def staircase(n):
	count = 0
	while count <= n:
		print('#').rjust(5)
		count += 1 

staircase(4)
