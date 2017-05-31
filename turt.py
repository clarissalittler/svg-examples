import svgwrite
import math

class SVGTurtle:
    def __init__(self,fileName):
        self.pic = svgwrite.Drawing(filename=fileName)
        self.angle = 0
        self.x = 0
        self.y = 0

    def moveTo(self,x,y):
        self.x = x
        self.y = y

    def forward(self,len):
        endX = self.x + len * math.cos(self.angle)
        endY = self.y + len * math.sin(self.angle)
        self.pic.add(self.pic.line(start=(self.x,self.y),
			           end=(endX,endY),stroke="black"))
        self.x = endX
        self.y = endY

    def turn(self,angle):
        self.angle = self.angle+(angle * math.pi/180)

    def end(self):
        self.pic.save()
