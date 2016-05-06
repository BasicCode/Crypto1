#brute force transposition cipher script
from itertools import permutations
import ngram_score as ns
import math

#regular string
#cipher = "COOUSULYDUTQOHYSEELPEUTSTGTOARIDTHMWPEERDTTEFEXUTOROSECUYCOU"
#90 dec clockwise rotation
#cipher = "SATCHEFUPROETIRENIWTDLEIONNTICSOTNOUYSOOEYKOLIIHERLADIC"
#90 dec anticlockwise rotation
#cipher = "RUFYTLIAGSREETSASDDITIRRYIHERNETNSNSRRUSENIWVTOINNRNUNU"
#some sort of 2x2 block rotation
#cipher = "ICTOMSPLEDDTTOFYXETLRESTCTYTOADOHUWUEYRUTQEHESEUOPOUESUGCOUR"
#Test string
#cipher = "HITISASSTEMSTESGOAETEOSEHTFWHETSINETTSESOSWRK"
#cipher 3 regular string
#cipher = "KIWDYFAIASYQXQFGMQDZOHUQKNEFVLAZPZPCXYDJQLVGCKXPASIENMNJYNGA"
#cipher 3 backwards
cipher = "NKIOSTPZNGMEZNQTKSNXJYNWSGYUPVDMZXRRRFCVAXQJNRIEJRTVAMRPHHERRU"

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

#Sort the list of decoded texts by their scores highest to lowest.
def highestToLowest(decoded_texts, scores):
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

if __name__ == '__main__':

	fitness = ns.ngram_score("c:/Users/Tommy/OneDrive/Documents/crypto1/quadgrams.txt")

	#Build a list of all possible keys
	print("Building possible cipher keys...")
	key_list = keyList(11)
	
	#decode the cipher with all the keys above
	decoded_texts = decodeString(key_list, cipher)
	
	#Run a fitness score on each list
	print("Calculating quadgram scores for each key text...")
	scores = []
	for text in decoded_texts:
		scores.append(fitness.score(text))
		
	print("Sorting results...")
	#sorted_texts = highestToLowest(decoded_texts, scores)
	sorted_texts = estimatedBest(decoded_texts, scores)
	
	#Output the results
	for i in range(0, len(sorted_texts)):
		print(str(decoded_texts[sorted_texts[i]]) + " - " + str(key_list[sorted_texts[i]]))
		pass
		
	print("(" + str(len(sorted_texts)) + " results)")