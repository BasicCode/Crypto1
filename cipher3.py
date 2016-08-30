#attempts at solving cipher 3.
from itertools import permutations
import ngram_score as ns
import math
import crypto_tools as crypto

cipherTxt = "KIWDYFAIASYQXQFGMQDZOHUQKNEFVLAZPZPCXYDJQLVGCKXPASIENMNJYNGAODJPJYNTCFRJUITECGGSPVEABSTKTNBJOHZOKDHASGHPRLAEFUOSKRWANNLGRTZTTKPYABQGLQHFVDTQQORNBZDOCRSMQVVQXYVCQNVNEBXKAJHHBWJTPVMVFEQXQQKAWPEHVQFGMVPUOSGGGKAKYQNARZMAKIOSPBZSGKCWWWPPNBEMQMBBZMCHZQSJRWRWPEZRTCFTANBOHXBSMCKJNNTCOGCKZDSWIKIPWGPUYMNNCLXDMAXNNHLWECKCAWHIVLNWAORGACTWQPHKHRIPRWRZRNSYQXQFGMQDZOHZSKDHNEGQHZPNPFVTHCFENWXMJXYAASHBMSYWRUAPAEZMWCMRPPEZECAGSBFVLQQTKSNZEREBSLHVBYAWQVSMGEJOWSOKDGMEREXSKDHTJHQQPQTNNSQTSSJSBQJLRTLSNKPVQAXSAIAFVLETRFIPAGWYYVUMVNGQASVKPQKIQXQAGXHAZIMXAOAFPVGHXSKRUWWDMXRADBPGSEBFMQNFEWPQVOTANESNRRRGCWHWHZCFANKIWBQTKDAPWXRMPVNWVDQTSZSAUVBWBSYQTKPEZNOZTTNXZSRNZTYGRJHEUCVRAPJNSSPXHJQZSRWBZJGSBOABZOGGIEOHEQKBJHYHWYCONWLZXMXRPNWBYAWQVKJNBYQSKRRNKPGDNSYGYGRJHEUCVRTFSOWSOKDGMDGUQCFTARWEIOMKAPIVVMVRNLCDLGYQVOAPAEZNPSGSLPWXMXSGYUPVGHHKRRTXGOWGLNLASYVIQQGQNBJSVAMKDAUGPTNZTBHQZXTQBSQJSJQXYCOGHAZIMXAAHLIGOSWBZJGSEZNTCFNLBYSZQPQMVPYJZGLKSNBYAWQVLSIMWHRTNHRTPGPDXOABWPYQNWCFAPFCGIJZASQXQWQZCFAPVVWMTBETMHZPHGCLQHFSTSSGFNLOEZRXZOJGPSSEXSGYUPVXEWXAPHQSPDXOAQEFQVNWCFAPFCGIJZASAVEZNPSGSLPEZRXZONKPGZRMXKSAFEOIJZSKHXSQXYVASHNVOKGJNTGLEZRXZSPVZZUNJZKVHKIWQXBONEPVQMZCRIHEMQSKRGQAIUASGPZMVFELMHZOQQLYUMHXAPHQWXSBPAHLIGOSWBZJGSYVQSZWYMNJDSKBOMVPSQRXRWNPKZDVTXRRKFCVNYVMYWVWXEUCFNAKYQNARZMTVMVYKBPNNVCWKYAKJGLSPPQVASWFVLEAXRRUPGQASYOGHAZIMXAOGHFSDVAXOTGLWXBYVURELJDQARGSAKIOSXSKQNFEWPQVOTAKGENLISMRPLOVZROGHVXLQYQKTPNEDDYTADQKLOHTPOWHWGPUQLENLFMDNXSKDHNSSEORKYEFEZNABOTLFQHNYAASTBFGSKBSMGEJQBCRZRNPDPBQUHNWKSQXGAGDIIUWHXLANALWQTSQCTZRJEQQXAPHQSPDXSRNHNVDSQBURZWWRNWAAZZNPWMTCFANDYDNXSKQNFEWPQVOTAPYDAXPHDGTJUNPBJQHKIWBQTKDAPWXRTIWWHQXGUGALWMPCTSKQKNQXYVQSLLVQXZUIQMMMVQJWYGTLQQEZVMXNELNBGWNKBHYHLSQENRGSGLGOHOPWYWVHWBXNAZNBJLMHZOQQKZDNYAMMGMZSYSCFNWPKOPMJKQGMSQRXRWNPKSQXYCGDHHZKNJNORRPEHVQMJMJLHHERBEKHKIWNZAKSNNYVSWZXOQXEPDGVUAPNVXMTZONAPAENTGKRZPPWHXAKALBWXTKZXGENRZSKBHYHLCTRPGLJHLEUVXOLMVFSNRJJORNFQABSMGWQHZQAUPRNKPVPHQPQMVPUZRMXKSQLRQXQVOGHXEOSQFKSNKIOSTPZNGMEZNQTKSNXJYNWSGYUPVDMZXRRRFCVAXQJNRIEJRTVAMRPHHERRU"
#cipherTxt = "KIWDYFAIASYQXQFGMQDZOHUQKNEFVLAZPZPCXYDJQLVGCKXPASIENMNJYNGAODJPJYNTCFRJUITECGGSPVEABSTKTNBJOHZOKDHASGHPRLAEFUOSKRWANNLGRTZTTKPYABQGLQHFVDTQQORNBZDOCRSMQVVQXYVC"
#testText = "SureyoucancomputetheCoincidenceindexbycountingthenumberofoccurrencesofeachletterinthealphabetusingaprogramandcomputingtheformuladirectlycheckoutmrgooglefortheformulaeifyouwanttoinvestigatethatbutthereisafastmanualtrickdevelopedintheprecomputerdaysforroughlyestimatingtheCoincidenceIndexofatextThetrickPrintouttheciphertextandlineitupwithacopyofitselfshiftedafewplacesorbyawholelinesayThencountthenumberoftimestheletterinthefirstcopymatchestheletteritisalignedwithinthesecondcopyThenumberofsuchcoincidencesdividedbythelengthofthemessageisanothopelessestimateofthecoincidencerateofthetextMultiplythatnumberbytogetanestimateoftheCoincidenceIndex"
if __name__ == '__main__':
	#Reference to the crypto tools class
	ctools = crypto.crypto_tools()

	#build an array of Nth character strings
	print("Build list of candidate texts...")
	char_arrays = []
	
	for i in range(2, 10):
		for j in range(0, i):
			char_arrays.append(ctools.everyNthChar(i, j, cipherTxt))
	
	#Calculate coincidence index of each
	CIs = []
	good_strings = []
	for i in range(0, len(char_arrays)):
		temp_ci = ctools.coincidenceIndex(char_arrays[i])
		#only keep the good ones
		if temp_ci > 0.06:
			CIs.append(temp_ci)
			good_strings.append(char_arrays[i])
	
	
	fitness = ns.ngram_score("c:/Users/Tommy/OneDrive/Documents/crypto1/quadgrams.txt")

	#Build a list of all possible keys
	print("Calculating possible cipher keys...")
	key_list = ctools.keyList(9)
	
	#decode the cipher with all the keys above
	print("Decoding " + str(len(good_strings)) + " strings with " + str(len(key_list)) + " keys...")
	decoded_texts = []
	for text in good_strings:
		decoded_texts.append(ctools.decodeString(key_list, text))
	
	#Run a fitness score on each list
	print("Calculating quadgram scores for " + str(len(decoded_texts) * len(key_list)) + " candidates...")
	all_scores = []
	for arrays in decoded_texts:
		scores = []
		for text in arrays:
			scores.append(fitness.score(text))
		all_scores.append(scores)
	
	#Sort the results of the scores
	print("Sorting results...")
	sorted_texts = []
	for arrays in all_scores:
		sorted_texts.append(ctools.estimatedBest(decoded_texts, arrays))
	
	#Output the results
	for j in range(0, len(sorted_texts)):
		arrays = sorted_texts[j]
		this_texts = decoded_texts[j]
		for i in range(0, len(arrays)):
			print(this_texts[arrays[i]])
			pass
		
	print("(" + str(len(sorted_texts)) + " results)")
	
	'''
	for i in range(0, len(CIs)):
		print(str(CIs[i]) + " : " + char_arrays[i])
	'''