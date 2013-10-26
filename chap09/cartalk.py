"""Module that solves the cartalk puzzlers

Author of cartalk.py: Emily
"""

"""Puzzler 2"""
def is_palindrome(word):
    """Returnes if word is a palindrome
    t: word
    returns: Boolean"""
   
    if word[0]==word[-1]:
        if len(word)<=2:
            return True
        else:
            return is_palindrome(word[1:-1])
    else:
        return False


def puzzler2solver():
    """function that uses the four specifications in the puzzler 
    to loop through all 6 digit numbers to find the answers
    returns: list of strings that satisfy"""
    t=[]
    for i in range(100000,1000000):
        word1=str(i)
        
        if is_palindrome(word1[2:]):
            
            word2=str(i+1)
            if is_palindrome(word2[1:]):
                word3=str(i+2)
                if is_palindrome(word3[1:-1]):
                    word4=str(i+3)
                    if is_palindrome(word4):
                        t.append(word1)
                        
    return t

print puzzler2solver()
"""Either you start at 198888 or 199999"""

"""Puzzle3"""
def reverse_pair(n):
    """finds the reverse pair of a string.
    n: string
    returns: rp integer"""
    rp=n[::-1]
    """cool thing I looked up called extended slice"""
    return rp
def puzzler3solver():
    """Solves the cartalk puzzle 3 by searching for values that satisfy
    the conditions
    returns list ageboynow"""

    """Age gaps is a list of all the possible gaps between mom and boy's
    age"""
    age_gaps=range(100)
    ageboynow=[]
    for gap in age_gaps:
        mom=gap
        boy=0
        total_pair=0
        agesofpairs=[]
        for i in range(mom,100):
            if reverse_pair(str(mom))==str(boy):
                total_pair+=1
                agesofpairs.append(boy)
            mom+=1
            boy+=1
        if total_pair==7:
            ageboynow.append(agesofpairs[5])
    return ageboynow

print puzzler3solver()
"""He's 68 now"""


     

    



