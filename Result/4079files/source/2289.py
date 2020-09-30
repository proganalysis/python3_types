import collections
n = 1000
def isTriangle(a, b, c):
    return a+b>c and a+c>b and b+c>a
def isStraightTriangle(a, b, c):
    if not isTriangle(a, b, c):
        return False
    x = a*a
    y = b*b
    z = c*c
    return x+y==z or x+z==y or z+y==x
#print(isTriangle(3,4,5))
#print(isStraightTriangle(3,4,5))
#count = 0
perimeterCounter = collections.Counter()
for x,y,z in zip(range(1,n),range(1,n),range(1,n)):
    print(x)
for x in range(1, n):
    print(x)
    for y in range(1, n):
        for z in range(1, n):
            #if isStraightTriangle(x, y, z):
                perimeter = x + y + z
                if perimeter <= 1000:
                    perimeterCounter[perimeter] += 1

#print("Всего пифагоровых троек {}".format(count))
print(perimeterCounter.most_common(3))

