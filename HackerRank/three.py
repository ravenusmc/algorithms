# The provided code stub reads two integers, a and b, from STDIN.
# Add logic to print two lines. The first line should contain the result of integer division,  
# // . The second line should contain the result of float division,  / .
# No rounding or formatting is necessary.

# url: https://www.hackerrank.com/challenges/python-division/problem

def division_problem(a,b):
	integer_division = a // b 
	float_division = a / b 
	print(integer_division)
	print(float_division)

division_problem(3,5)