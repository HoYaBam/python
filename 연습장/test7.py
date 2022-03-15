# list_a = ['홍길동','개똥이', '집','에','가','고','싶','다']
# if '제발' not in list_a:
#     print('집에가고싶다')
# else:
#     print('그런거 없음')

for i in range(1, 10):
    print(i)

list_a = ['a','b','c','d','e','f','g']

for i in list_a:
    print(i)

for i in range(0,len(list_a)):
    print(list_a[i])

for i in range(9, 1 , -1):
    print('*' * i)

n = 10
print(n // 2)
for i in range(n // 2):
  print(' '.join([ ' ' ] * i + [ '*' ] * (n // 2 - i) + [ ' ' ] * (n // 2 - (i + 1)) + [ '*' ] * (i + 1)))
for i in range(n // 2):
  print(' '.join([ '*' ] * (n // 2 - i) + [ ' ' ] * i + [ '*' ] * (i + 1) + [ ' ' ] * (n // 2 - (i + 1))))

numbers = [273,103,5,32,65,9,72,800,99]

for number in numbers:
    if number >= 100:
        print('- 100 이상의  수', number)

for number in numbers:
    if number % 2 == 0:
        print(number,' 는 짝수 입니다.')
    else:
        print(number,' 는 홀수 입니다.')


for number in numbers:
    print(number, '는 {} 자릿수입니다.'.format(len(str(number))))

list_of_list = [[1,2,3], [4,5,6,7],[8,9]]


for i in range(0,len(list_of_list)):
    for j in range(0,len(list_of_list[i])):
        print(list_of_list[i][j])

numbers2 = [1,2,3,4,5,6,7,8,9]
output = [[],[],[]]

for number in numbers2:
    output[(number %3) -1].append(number)

print(output)


#국어 영어 수학 반복해서 값을 받는다 번호가 0 이면 종료 받은 내용을 score list에 받는다

scores = []
while True:
    no = int(input("No : "))
    if no == 0:
        break;
    name = input("Name : ")
    kor = int(input("kor : "))
    eng = int(input("eng : "))
    mat = int(input("mat : "))

    score = [no,name,kor,eng,mat]
    scores.append(score)

print(scores)

for score in scores:
    tot = score[2] + score[3] + score[4]
    score.append(tot)
    score.append(tot/3)

for score in scores:
    print(score)