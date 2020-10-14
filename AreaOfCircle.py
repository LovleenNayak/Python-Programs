#Finding out area of circle

class area():
    def __init__(self,radius):
        self.radius = radius
        pi = 3.14
        area = pi * (radius**2)
        print("Area of Circle : {}".format(area))

r = float(input("Radis of Circle : "))
area = area(r)
