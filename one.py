 # Given an integer, write a function to print it out in words (e.g. given 342, print "three-hundred forty-two"

def convert_hundreds_to_words(hundreds_value):
	print(hundreds_value)
	if hundreds_value == '1':
		return 'one-hundred'
	elif hundreds_value == '2':
		return 'two-hundred'
	elif hundreds_value == '3':
		return 'three-hundred'
	elif hundreds_value == '4':
		return 'four-hundred'
	elif hundreds_value == '5':
		return 'five-hundred'

	
def convert_number(number):
	number_to_string = str(number)
	length_of_string = len(number_to_string)
	if length_of_string == 3:
		words_list = []
		hundreds_value = number_to_string[0]
		hundreds_spot_to_words = convert_hundreds_to_words(hundreds_value)
		words_list.append(hundreds_spot_to_words)
		print(words_list)
	
convert_number(325)

