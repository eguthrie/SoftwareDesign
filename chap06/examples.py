""" Author Emily Guthrie
"""

def ispower(a,b):
    """returns if a is a power of b
    a= float
    b=float
    return is True or False"""
 
    if a==0 or not isinstance(a,float):
        print a,' is not a valid entry for a, a must be a floating point number not equal to 0'
    if b==0 or not isinstance(b,float):
        print b,' is not a valid entry for b, b must be a floating point number not equal to 0'
    if a%b==0 and a==b:
        return True
    if a%b==0:
        return ispower(a/b,b)
    else:
        return False 

ispower(24.0,4.0)
ispower(24,4)
ispower(0,4.0)
ispower(4.0,5.0)
ispower(16.0,4.0)

def gcd(a,b):
    """finds the greatest common denominator of a and b
    a=float
    b=float
    result Boolean"""
