"""Author Emily Guthrie
Searches through a list of words and determines if word has a
reverse pair in the list"""
def reverse_pair(word_list,word):
	reverse=word[::-1]
	for words in word_list:
		if words==reverse:
			print word,words

def reverse_pair_driver():
	word_list=[]
	for line in open('words.txt'):
		word=line.strip()
		word_list.append(word)
	for word in word_list:
		reverse_pair(word_list,word)

reverse_pair_driver()

