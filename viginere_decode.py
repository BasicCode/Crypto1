#Python Vigenere cipher decoder

from multiprocessing import Process, Queue
from itertools import permutations
import ngram_score as ns

#cipherTxt = "WJHZRDIAKZTMCYSOMLVYHISNFBNZRPOESFJRVLWLMIPOALJAKDSQWLHKYSCNRMHPBOQNQQMNBXCCACJNBOVVTLAUWJRNISIFFBJOWZWIVNCWQMAUEEXTNOMRJIIYHISNWDY"
#cipherTxt = "IHAKEGRVXMHDAHVVIMWKOOXHIOKWAWWPNVAYABVUTDWUNMGWXOFAOKFUZIFYYCIUTCLDUOEGXFLZAKFUSLAKPWJVJFXAYWVQITZWMIZFZBJGSBWRMJMELSURKEJLDSCDOYVGC"
#cipherTxt = "LLKJMLSKMOGPXLWWVDILKSKGKSLWWMHDCOAYIPVVXVWGTPTMAGRKJAHJCMPXGHJJIEKPRSFHKWXAWOSTUPBKLMUJYYXAGKVRMLZISLMVCTVQNRYGPNWDTXVGZGIXAWDEBPHHY"
#cipher 3 text
cipherTxt = "KIWDYFAIASYQXQFGMQDZOHUQKNEFVLAZPZPCXYDJQLVGCKXPASIENMNJYNGAODJPJYNTCFRJUITECGGSPVEABSTKTNBJOHZOKDHASGHPRLAEFUOSKRWANNLGRTZTTKPYABQGLQH"

#common statics
key_length = 2
SOWPODS_file = "c:/Users/tommy/OneDrive/Documents/crypto1/sowpods2.txt"
common_words_file = "c:/Users/tommy/OneDrive/Documents/crypto1/commonwords.txt"

#Perform a decode of the string with a particular word
#returns the result of the decryption without checking the result.
def tryDecode(word, encoded_txt):
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
def simpleWordList(file):
	word_list = []
	with open(file, "r") as f:
		for line in f:
			this_word = line.strip().upper()
			if len(this_word) > key_length:
				#this_word = removeDuplicateChars(this_word)
				word_list.append(this_word)
	return word_list

#checks letter frequency of each character
#returns an array of 26 letters of the alphabet representing their % requency
def characterFrequency(text):
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

#perform frequency analysis and return "nice" looking frequencies
def niceFrequencies(decoded_list):
	frequency_list = []
	for test in decoded_list:
		frequency_list.append(characterFrequency(test))
	#Look for "nice" frequency distributions matching english
	nice_frequencies = []
	for i in range(0, len(frequency_list)):
		#check enough Es and not many Cs
		if frequency_list[i][25] < 2:
			if frequency_list[i][4] > 9:
				nice_frequencies.append(i)
	return nice_frequencies

#Take a rough estimate of the top 50 results
def estimatedBest(decoded_texts, scores):
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

#Make a sequence of all possible permutations within range
def keyList(length):
	this_key = [0] * length
	for j in range(0, length):
		this_key[j] = j
	key_list = list(permutations(this_key))
	
	return key_list

#Decode a string according to a list of keys
def decodeString(key_list, cipher):
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

if __name__ == '__main__':
	
	#Construct the word list for this attempt
	print("Build word list...")
	word_list = simpleWordList(SOWPODS_file)

	#Build a list of all possible keys
	key_list = keyList(6)
	
	#decode the cipher with all the keys above
	decoded_texts = decodeString(key_list, cipherTxt)
	
	#Just gotta add this *word* in case it's what he is using
	word_list.append("GEEGB")
	word_list.append("GEB")
	
	#Vigenere decode the using SOWPODS file
	print("Vigenere decoding " + str(len(decoded_texts)) + " candidates with " + str(len(word_list)) + " key words...\n(Good luck!)")
	vig_decode = []
	counter = 0
	for word in word_list:
		print(str((counter / len(word_list)) * 100) + "%")
		for item in decoded_texts:
			vig_decode.append(tryDecode(word, item))
		counter = counter + 1
	
	#Check the decoded results for any words matching the list of common words
	print("Calculate quadgram scores for " + str(len(vig_decode)) + " strings...")
	fitness = ns.ngram_score("c:/Users/Tommy/OneDrive/Documents/crypto1/quadgrams.txt")
	scores = []
	for items in vig_decode:
		scores.append(fitness.score(items))
	
	print("Sorting results...")
	sorted_texts = estimatedBest(vig_decode, scores)
	
	#use this for threading
	#q1 = Queue()
	#t1 = Process(target=findEnglishWords, args=(decoded_list_1, common_words_file, 0, q1)).start()
	#word_hits_1 = q1.get()
	
	#Output the results
	for i in range(0, len(sorted_texts)):
		print(str(vig_decode[sorted_texts[i]]))
		pass
		
	print("(" + str(len(sorted_texts)) + " results)")
	