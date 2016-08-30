#Merkle decode python script

import crypto_tools as crypto
import hashlib

word = "merkle"
length = 10
hash_list = "c:/Users/tommy/OneDrive/Documents/crypto1/merkle_list.txt"
s256_hash = "0449f93d9bb16b9657d7c6350ec77d7f577d276743b714af0272c503a2eb01cc"

#Opens the file of hashes and salts. Returns an array [[salt, hash]]
def openHashFile(file):
	ret_list = []
	with open(file, "r") as f:
		for line in f:
			this_item = []
			salt_pos = line.find("salt:") + 5
			this_item.append(line[salt_pos:salt_pos + 20])
			hash_pos = line.find("hash:") + 5
			this_item.append(line[hash_pos:hash_pos + 40])
			
			ret_list.append(this_item)
	
	return ret_list
	
ctools = crypto.crypto_tools()

merkle_list = ctools.merkleKeys(word, length)

hash_list = openHashFile(hash_list)

#Build the full list of merkle + hash
full_list = []
for i in merkle_list:
	for j in hash_list:
		full_list.append("COMP3441{" + str(i) + ":" + str(j[0]) + "}")
		
#Look for a hash matching the sha256 hash
print("Checking for SHA256 hash match...")
counter = 0
for i in range(0, len(full_list)):
	s256_result = hashlib.sha256(full_list[i].encode('utf-8')).hexdigest()
	if s256_result == s256_hash:
		print("* Found a match at #" + str(i) + " with " + full_list[i])

	print(s256_result)