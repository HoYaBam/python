import random
bingo = []
def make_pan(bingo):
    for i in range(5):
        temp = []
        for j in range(5):
            temp.append((i * 5) + j + 1)
        bingo.append(temp)

def suff_pan(bingo):
    for t in range(100):
        temp = bingo[0][0]
        x = random.randint(0, 4)
        y = random.randint(0, 4)
        bingo[0][0] = bingo[x][y]
        bingo[x][y] = temp

def bingo_rept(bingo):
    result = ''
    number = int(input('숫자 입력'))
    for i in range(5):
        for j in range(5):
             if bingo[i][j] == number:
                bingo[i][j] = 0
    result = chk_bingo(bingo)
    return result

def chk_bingo(bingo):
    # 빙고 체크(가로)
    result=''
    for i in range(5):
        sum = 0
        for j in range(5):
            sum += bingo[i][j]
        if sum == 0:
            result = 'Bing Go'

    # 빙고 체크(세로)
    for i in range(5):
        sum = 0
        for j in range(5):
            sum += bingo[j][i]
        if sum == 0:
            result = 'Bing Go'
    # 빙고 체크(대각선-왼쪽에서 오른쪽)
    sum = 0
    for i in range(5):
        sum += bingo[i][i]
    if sum == 0:
        result = 'Bing Go'
    # 빙고 체크(대각선-오른쪽에서 왼쪽)
    sum = 0
    for i in range(5):
        sum += bingo[i][4 - i]
    if sum == 0:
        result = 'Bing Go'
    return result

def prt_bingo(bingo):
    for i in range(5):
        for j in range(5):
            print("{:3d}".format(bingo[i][j]), end=' ')
        print()

# 빙고판 초기화
make_pan(bingo)
# 빙고판 섞기
suff_pan(bingo)
# 숫자입력(반복)
result = ' '
while result != 'Bing Go' :
    result = bingo_rept(bingo)
print('Bingo!!!')
# 빙고판 출력
prt_bingo(bingo)