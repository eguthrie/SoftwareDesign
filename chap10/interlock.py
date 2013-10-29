def is_interlocked(word_list,word,n):
	for i in range(n):
		word=word[i::n]
		if not word in word_list:
			return False
	return True
		
def interlock_driver():
	word_list=[]
	for line in open('words.txt'):
		word=line.strip()
		word_list.append(word)
	for word in word_list:
		if is_interlocked(word_list,word,3):
			print word,word[0::3],word[1::3],word[2::3]
