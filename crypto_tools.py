#A package of crypto tools that I have developed along the way.
#Here for easy re-use.

class crypto_tools(object):
	def __init__(self):
		import math

	#Make a sequence of all possible integer permutations within range
	def keyList(self, length):
		from itertools import permutations
		this_key = [0] * length
		for j in range(0, length):
			this_key[j] = j
		key_list = list(permutations(this_key))
		
		return key_list
	
	#Returns an array of Merkle keys based on a supplied word and desire length
	def merkleKeys(self, word, length):
		from itertools import combinations_with_replacement
		key_list = list(combinations_with_replacement(word, length))
		
		#Convert to strings
		ret_list = []
		for i in key_list:
			ret_list.append(''.join(i))
		
		return ret_list	

	#Decode a string according to a list of numeric keys
	def decodeString(self, key_list, cipher):
		return_list = []
		for key in key_list:
			this_text = ""
			counter = 0
			cycles = 0
			for i in range(0, len(cipher)):
				this_text = this_text + cipher[key[counter]+cycles:key[counter]+1+cycles]
				counter = counter + 1
				if counter == len(key):
					counter = 0
					cycles = cycles + len(key)
			return_list.append(this_text)
		
		return return_list

	#Sort the list of decoded texts by their scores highest to lowest.
	def highestToLowest(self, decoded_texts, scores):
		for i in range(0, len(scores)):
			for j in range(0, len(scores) - 1):
				temp_val = scores[j + 1]
				temp_str = decoded_texts[j + 1]
				if temp_val < scores[j]:
					decoded_texts[j + 1] = decoded_texts[j]
					scores[j + 1] = scores[j]
					decoded_texts[j] = temp_str
					scores[j] = temp_val
		return decoded_texts

	#Take a rough estimate of the top 50 results
	def estimatedBest(self, decoded_texts, scores):
		#first find the max and min values
		min = 0
		for i in range(0, len(scores)):
			if scores[i] < scores[min]:
				min = i
		max = min
		for i in range(0, len(scores)):
			if scores[i] > scores[max]:
				max = i
		#get the top results within 'range' of the maximum
		ret_val = []
		distance = 5
		for i in range(0, len(scores)):
			if scores[i] > (scores[max] - distance):
				ret_val.append(i)
		
		#Now sort the short list in highest to lowest quality
		for i in range(0, len(ret_val)):
			for j in range(0, len(ret_val) - 1):
				temp_val = ret_val[j + 1]
				if scores[temp_val] < scores[ret_val[j]]:
					ret_val[j + 1] = ret_val[j]
					ret_val[j] = temp_val
		
		return ret_val
		
		#checks letter frequency of each character
	#returns an array of 26 letters of the alphabet representing their % requency
	def characterFrequency(self, text):
		text = text.upper()
		frequency = [0] * 26
		#first add up all the letters in to an array
		for character in text:
			character = ord(character) - 65
			frequency[character] = frequency[character] + 1
		#now work out the relative frequency as a percentage
		for i in range(0, 26):
			frequency[i] = (frequency[i] / len(text)) * 100
		return frequency
		
	#Calculate the coincidence index of a string
	def coincidenceIndex(self, text):
		text = text.upper()
		frequency = [0] * 26
		#first add up all the letters in to an array
		for character in text:
			character = ord(character) - 65
			frequency[character] = frequency[character] + 1
		#Now add the probability of each letter occuring
		sum = 0
		for letter in frequency:
			sum = sum + ((letter * (letter - 1)) / (len(text) * (len(text) - 1)))
		return sum

	#perform frequency analysis and return "nice" looking frequencies
	def niceFrequencies(self, decoded_list):
		frequency_list = []
		for test in decoded_list:
			frequency_list.append(self.characterFrequency(test))
		#Look for "nice" frequency distributions matching english
		nice_frequencies = []
		for i in range(0, len(frequency_list)):
			#check enough Es and not many Cs
			if frequency_list[i][25] < 2:
				if frequency_list[i][4] > 10:
					nice_frequencies.append(i)
		return nice_frequencies
	
	#Vigenere decode the string with a particular word
	def vigenereDecode(self, word, encoded_txt):
		#work in all upper case
		word = word.upper()
		#loop counter
		x = 0
		#string to return
		ret_str = ""
		for character in encoded_txt:
			#convert to alphabet number
			character = ord(character) - 65
			cipher = ord(word[x:x+1]) - 65
			letter = (character - cipher)%26
			#convert back to ASCII
			letter = letter + 65
			ret_str = ret_str + chr(letter)
			#x should only count the cipher word length and then repeat
			x = x + 1
			if x == len(word):
				x = 0
				
		return ret_str
		
	#make a word list of all words in the file, of any length > 2 letters
	def simpleWordList(self, file, key_length):
		word_list = []
		with open(file, "r") as f:
			for line in f:
				this_word = line.strip().upper()
				if len(this_word) > key_length:
					#this_word = removeDuplicateChars(this_word)
					word_list.append(this_word)
		return word_list
	
	#Build a string containing every Nth character of the text
	def everyNthChar(self, n, offset, text):
		ret_str = ""
		for i in range(1, int(len(text) / n)):
			ret_str = ret_str + text[(i*n)-1+offset:(i*n)+offset]
		return ret_str