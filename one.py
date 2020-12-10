 # Given an integer, write a function to print it out in words (e.g. given 342, print "three-hundred forty-two"

def convert_hundreds_to_words(hundreds_value):
	if hundreds_value == '1':
		return 'one-hundred '
	elif hundreds_value == '2':
		return 'two-hundred '
	elif hundreds_value == '3':
		return 'three-hundred '
	elif hundreds_value == '4':
		return 'four-hundred '
	elif hundreds_value == '5':
		return 'five-hundred '
	elif hundreds_value == '6':
		return 'six-hundred '
	elif hundreds_value == '7':
		return 'seven-hundred '
	elif hundreds_value == '8':
		return 'eight-hundred '
	elif hundreds_value == '9':
		return 'nine-hundred '

def convert_tens_to_words(tens_value):
	if tens_value == '0':
		return 'and '
	elif tens_value == '1':
		teens_value_check = True
		return teens_value_check
	elif tens_value == '2':
		return 'twenty-'
	elif tens_value == '3':
		return 'thirty-'
	elif tens_value == '4':
		return 'fourty-'
	elif tens_value == '5':
		return 'fifty-'
	elif tens_value == '6':
		return 'sixty-'
	elif tens_value == '7':
		return 'seventy-'
	elif tens_value == '8':
		return 'eighty-'
	elif tens_value == '9':
		return 'ninety-'

def convert_ones_to_words(ones_value):
	if ones_value == '0':
		return 'and'
	elif ones_value == '1':
		return 'one'
	elif ones_value == '2':
		return 'two'
	elif ones_value == '3':
		return 'three'
	elif ones_value == '4':
		return 'four'
	elif ones_value == '5':
		return 'five'
	elif ones_value == '6':
		return 'six'
	elif ones_value == '7':
		return 'seven'
	elif ones_value == '8':
		return 'eight'
	elif ones_value == '9':
		return 'nine'

def convert_tens_to_words(ones_value):
	if ones_value == '0':
		return 'and ten'
	elif ones_value == '1':
		return 'and eleven'


def convert_number(number):
	number_to_string = str(number)
	length_of_string = len(number_to_string)
	if length_of_string == 3:
		words_list = []
		hundreds_value = number_to_string[0]
		tens_value = number_to_string[1]
		ones_value = number_to_string[2]
		hundreds_spot_to_words = convert_hundreds_to_words(hundreds_value)
		words_list.append(hundreds_spot_to_words)
		tens_spot_to_words = convert_tens_to_words(tens_value)
		if tens_spot_to_words == True:
			teens_word_value = get_teens_value(ones_value)
			words_list.append(teens_word_value)
		else:
			words_list.append(tens_spot_to_words)
			ones_spot_to_words = convert_ones_to_words(ones_value)
			words_list.append(ones_spot_to_words)
		print(words_list)
		# final_word = ""
		# print(final_word.join(words_list))

	
convert_number(310)

