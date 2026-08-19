from collections import namedtuple
Point = namedtuple('Point', 'x,y')
pt=Point(1, -4)
print(pt)  #It returns a named tuple with the values of x and y.
print(pt.x, pt.y)  #It returns the values of x and y in the named tuple.
