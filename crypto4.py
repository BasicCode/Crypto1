import crypto_tools as crypto
import hashlib

word_file = "C:/Users/Tom/OneDrive/Documents/crypto1/sowpods.txt"
#The has file provided by the program to test against
test_hash = "8f6c0b7f7815781195a3f2663835ee70"

#Crypto tools class
ctools = crypto.crypto_tools()

#Load the word list
word_list = ctools.simpleWordList(word_file, 2)

#build a mega sentence list... Surely this is a bad idea
print("Build a sentence list...")
sentence = []
letter = "a"
for word in word_list:
	#Just to show where we're up to in the list
	if word[:1] != letter:
		letter = word[:1]
		print(letter)
	test_word = "test"
	message = "Username:" + test_word + ":Admin:False"
	part1 = hashlib.md5(message.encode("utf-8")).hexdigest()[:15]
	final = hashlib.md5(part1.encode("utf-8") + word.encode("utf-8")).hexdigest()
	if final == test_hash:
		print(final)
		print(phrase)
