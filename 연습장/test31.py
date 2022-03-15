import math, random as rm

ab = rm.randint(1,45)
print(ab)
randint_num = []
random_num = []

for i in range(10):
    randint_num.append(rm.randint(1 , 45)) #정수
    random_num.append(math.floor(rm.random() * 10) + 1) #실수


print(randint_num)
print(random_num)

for i in range(10):
    print(rm.randrange(1,100,1))

print()

rlist = [1,2,3,4,5]

print("choice : ",rm.choice(rlist))
print("shuffle : ", rm.shuffle(rlist))
rm.shuffle(rlist)
print(rlist)
blist = [[1,2,3],[4,5,6],[7,8,9]]
print(blist)
rm.shuffle(blist)
print(blist)
print("sample : ", rm.sample(rlist, k=2))

