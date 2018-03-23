from geom2d.point import Point

a = Point(0, 0)
b = Point(3, 4)
print(a.distance(b))
print(a == b)
print(a == Point(0, 0))