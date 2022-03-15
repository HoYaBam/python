import random
hangus = list('강김이박주차백임')
subname = list('가나다라마바사아차카타하이동하치키게크호헤나경영현연재현동수일근영태동은일경근')

with open("../info.txt", "w") as file:
    for i in range(1000):
        name = random.choice(hangus) + random.choice(subname)
        weight = random.randrange(40 ,100)
        height = random.randrange(140,200)

        file.write("{}, {}, {}\n".format(name, weight, height))

