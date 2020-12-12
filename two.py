# Task: Out the integers from 1 to 100. For each multiple of three, print Tree. 
# For each multiple of five, print 'house'. for multiples of both three and five 
# print 'Treehouse'. This is basically a version of Fizz Buzz 

def main():
	count =  0
	while count <= 100: 
		if count % 5 == 0 and count % 3 == 0:
			print('Treehouse')
		elif count % 5 == 0:
			print('House')
		elif count % 3 == 0:
			print('Tree')
		else:
			print(count)
		count += 1

main()