from vector import Vector

v1 = Vector(2, 4)
v2 = Vector(2, 1)
print(v1 + v2)
v = Vector(3, 4)
print(abs(v))
print(v * 3)
print(abs(v * 3))
print("test bool of zero vector and non-zero vector:")
print(bool(Vector(0, 0)))
print(bool(Vector(1, 1)))