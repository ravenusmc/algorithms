 # Given an integer, write a function to print it out in words (e.g. given 342, print "three-hundred forty-two"

def convert_hundreds_to_words(hundreds_value):
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
	elif hundreds_value == '6':
		return 'six-hundred'
	elif hundreds_value == '7':
		return 'seven-hundred'
	elif hundreds_value == '8':
		return 'eight-hundred'
	elif hundreds_value == '9':
		return 'nine-hundred'

def convert_tens_to_words(tens_value):
	if tens_value) == '0':
		return ' '
	elif tens_value) == '1':
		#Need to write another function here to hand the tens. 
		return 'one-hundred'
	elif tens_value) == '2':
		return 'twenty'
	elif tens_value) == '3':
		return 'thirty'
	elif tens_value) == '4':
		return 'four-hundred'
	elif tens_value) == '5':
		return 'five-hundred'
	elif tens_value) == '6':
		return 'six-hundred'
	elif tens_value) == '7':
		return 'seven-hundred'
	elif tens_value) == '8':
		return 'eight-hundred'
	elif tens_value) == '9':
		return 'nine-hundred'


	
def convert_number(number):
	number_to_string = str(number)
	length_of_string = len(number_to_string)
	if length_of_string == 3:
		words_list = []
		hundreds_value = number_to_string[0]
		tens_value = number_to_string[1]
		hundreds_spot_to_words = convert_hundreds_to_words(hundreds_value)
		words_list.append(hundreds_spot_to_words)
		tens_spot_to_words = convert_tens_to_words(tens_value)

	
convert_number(325)

