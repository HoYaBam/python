from math import sin, floor, ceil, pi,log, sqrt, radians


dre = radians(90)

print(sin(dre))
#print(math.sin(math.pi * (각도 / 180))
print(sin(pi * (90 / 180)))
degree = [i for i in range(0,360,10)]
print(degree)
for i in degree:
    print(i ,' : ',round(sin(pi * (i / 180))), 2)

print(ceil(5.3))
print(ceil(-5.3))
print(floor(5.3))
print(floor(-5.3))
print(sqrt(144))
print(log(2,3))
