#!/usr/bin/env python

import math

class Point:
   def __init__( self, xValue = 0, yValue = 0 ):
      self.x = xValue
      self.y = yValue

class Circle( Point ):
   def __init__( self, x = 0, y = 0, radiusValue = 0.0 ):
      Point.__init__( self, x, y )
      self.radius = float( radiusValue )

   def area( self ):
      return math.pi * self.radius ** 2

print 'Point bases:', Point.__bases__
print 'Circle bases:', Circle.__bases__

print '\nCircle is a subclass of Point:', issubclass(Circle, Point)
print 'Point is a subclass of Circle:', issubclass(Point, Circle)

point = Point( 30, 50 ) 
circle = Circle( 120, 89, 2.7 )   

print '\ncircle is a Point object:', isinstance(circle, Point)
print 'point is a Circle object:', isinstance(point, Circle)

print '\npoint members:\n\t', point.__dict__
print 'circle members:\n\t', circle.__dict__

print '\nArea of circle:', circle.area()

