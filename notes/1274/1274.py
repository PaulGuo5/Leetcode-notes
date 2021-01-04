# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        xt, yt = topRight.x, topRight.y
        xb, yb = bottomLeft.x, bottomLeft.y
        if xt < xb or yt < yb or not sea.hasShips(topRight, bottomLeft):
            return 0
        if xt == xb and yt == yb:
            return 1
        xm, ym = xb+(xt-xb)//2, yb+(yt-yb)//2
        return self.countShips(sea, topRight, Point(xm+1, ym+1)) + self.countShips(sea, Point(xm, ym), bottomLeft) + self.countShips(sea, Point(xt, ym), Point(xm+1, yb)) + self.countShips(sea, Point(xm, yt), Point(xb, ym+1)) 
