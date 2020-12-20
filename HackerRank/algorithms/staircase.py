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
	for i in range(1,n+1):
		print(" "*(n-i)+ "#"*i)

staircase(4)
