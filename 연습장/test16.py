import random

bingo = []
for i in range(5):
    temp = []
    for j in range(5):
        temp.append((i*5) + j +1)

    bingo.append(temp)

for i in range(5):
    for j in range(5):
        print("{:3d}".format(bingo[i][j]), end=" ")
    print()


for t in range(1000):
    temp = bingo[0][0]
    x = random.randint(0,4)
    y = random.randint(0,4)
    bingo[0][0] = bingo[x][y]
    bingo[x][y] = temp

print("\n")

for i in range(5):
    for j in range(5):
        print("{:3d}".format(bingo[i][j]), end=" ")
    print()

print("\n")
count = 0
result = ''
while result != 'Bing Go':
    z = int(input("번호 입력 : "))
    for i in range(5):
        for j in range(5):
           if bingo[i][j] == z:
               bingo[i][j] = 0

    #빙고 체크(가로)
    for i in range(5):
        sum = 0
        for j in range(5):
            sum += bingo[i][j]
        if sum == 0:
            result = 'Bing Go'
            print(result)
            break

    #빙고 체크(세로)
    for i in range(5):
        sum = 0
        for j in range(5):
            sum += bingo[j][i]
        if sum == 0:
            result = 'Bing Go'
            print(result)
            break

    sum = 0
    #빙고 체크(대각선)
    for i in range(5):
        sum += bingo[i][i]
    if sum == 0:
        result = 'Bing Go'
        print(result)
        break

    sum = 0
    # 빙고 체크(대각선)
    for i in range(5):
        sum += bingo[i][5-i]
    if sum == 0:
        result = 'Bing Go'
        print(result)
        break

    for i in range(5):
        for j in range(5):
            print("{:3d}".format(bingo[i][j]), end=" ")
        print()

    count += 1
    print("{}회차------------\n".format(count))

