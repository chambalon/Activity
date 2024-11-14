import math


class Rectangle:
    # Initialise the Rectangle object
    def __init__(self,l,w):
        self.length = l
        self.width = w

    def rectangle_area(self):
        return self.length * self.width



class Circle:
    def __init__(self,r):
        self.radius = r

    def circle_area(self):
        return math.pi * self.radius **2
    


if __name__ == "__main__" :

    l=int(input("Enter length:"))
    w=int(input("Enter width:"))

    rectangle = Rectangle(l,w)
    rectanglearea = rectangle.rectangle_area()
    print("Rectangle area is: ",rectanglearea)


    r = int(input("Enter radius:"))
    circle = Circle(r)
    circlearea = circle.circle_area()
    print("Circle area is: ",circlearea)
