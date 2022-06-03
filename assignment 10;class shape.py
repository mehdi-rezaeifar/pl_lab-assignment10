from subprocess import CREATE_NEW_CONSOLE
import math

class Shape:

    def __init__(self) :
        self.mohit = 0
        self.masahat = 0

class Rectangle(Shape) :

    def __init__(self , length , width):
        Shape.mohit = (length + width)* 2
        Shape.masahat = length * width
    def mohit(self):
        return Shape.mohit
    def masahat(self):
        return Shape.masahat

class Circle(Shape):

    def __init__(self , shoa) :
        Shape.mohit = (shoa * 2)* math.pi
        Shape.masahat = (shoa * shoa)* math.pi
    def mohit(self) :
        return Shape.mohit
    def masahat(self) :
        return Shape.masahat

A = Rectangle(5,8)
B = Circle(3)

print(f"mohit mostatil: {A.mohit()} masahat: {A.masahat()}")

print(f"mohit dayere: {B.mohit()} masahat: {B.masahat()}")