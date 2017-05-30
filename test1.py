import svgwrite

draw = svgwrite.Drawing(filename="test1.svg")

draw.add(draw.circle(center=(100,100), r=100))

draw.save()
