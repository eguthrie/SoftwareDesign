from swampy.TurtleWorld import *
from math import *
world=TurtleWorld()
bob= Turtle()
print bob

""" excercise 4.3"""


def square(t,length):
    for i in range(4):
        fd(t,length)
        lt(t)

"""square(bob,30)"""


def polygon(t,length,n):
    for i in range(n):
        fd(t,length)
        lt(t, 360.0/n)

"""polygon(bob,30,7)"""

def circle(t,r):
    bob.delay=.01
    polygon(t,1,6*r)

"""circle(bob,40)"""

def arc(t,r, angle):
    bob.delay=.01
    for a in range(angle):
        fd(t,1)
        lt(t,1)

arc(bob,40, 60)
    



wait_for_user()
