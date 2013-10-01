"""Module that provides is_palindrome.

Author of is_palindrome: you
"""

def first(word):
    """Returns the first character of a word.

    word: string

    returns: length 1 string
    """
    return word[0]


def last(word):
    """Returns the first character of a word.

    word: string

    returns: length 1 string
    """
    return word[-1]


def middle(word):
    """Returns all but the first and last character of a word.

    word: string

    returns: string
    """
    return word[1:-1]


def is_palindrome(word):
    """Returnes if word is a palindrome
    word: string
    returns: Boolean"""
   
    if first(word)==last(word):
        if len(word)<=2:
            return True
        else:
            return is_palindrome(middle(word))
    else:
        return False
    


    # TODO: fill in the body of this function



