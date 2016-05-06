str = "ayiipsaadauwhasfotfgfocscbafoastwaeotmohtcaadswakatlauicstwweotaucscstsiaiwettawfsatphygwittoyaocaltsitucctfcosual"
chars = [18,120,118,18,84,116,22,61,121]
offset = 1

for i in range(1, 13):
	test_str = ""
	for k in range(0, i):
		count = i
		for j in range(0, len(str)):
			test_str = test_str + str[count:count+1]
			count = count + i
		print(test_str)

