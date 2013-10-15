"""Emily Guthrie
Homework 5 Software Design"""

def rotchar(l,n):
	if l.isupper():
		new=ord(l)+n
		if new/90>0:
			new=new%90+64
		elif new/65==0:
			new=90+(new-64)
	if l.islower():
		new=ord(l)+n
		if new/122>0:
			new=new%122+96
		elif new/97==0:
			new=122+(new-96)
	return chr(new)

def rotword(word,n):
	rotated=''
	for letter in word:
		rotated=rotated+ rotchar(letter,n)
	return rotated
print rotword('melon',-10)