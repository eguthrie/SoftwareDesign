from swampy.TurtleWorld import *
from math import *
world=TurtleWorld()
bob= Turtle()

def koch(t,length):
	if length<3:
		fd(t,length)
		return
		
	angle=60
	koch(t,length/3)
	lt(t,angle)
	koch(t,length/3)
	rt(t,angle*2)
	koch(t,length/3)
	lt(t,angle)
	koch(t,length/3)
bob.delay=.01
"""koch(bob,1000)
"""
def snowflake(t,length):
	for i in range(3):
		koch(t,length)
		rt(t,120)
snowflake(bob,120)





