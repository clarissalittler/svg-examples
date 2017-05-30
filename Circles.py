import svgwrite
import random
from random import randint

img = svgwrite.Drawing(filename="circles.svg")

numtimes = randint(10,50)

for i in range(0,numtimes):
    posx = randint(0,500)
    posy = randint(0,500)
    rad = randint(10,50)
    c = img.circle(center=(posx,posy),r=rad)
    img.add(c)

img.save()
