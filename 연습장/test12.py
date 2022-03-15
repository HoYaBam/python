key_list = ["name", "hp", "mp", "level"]
value_list = ["기사", 200, 30, 5]

character = {}
for i in range(len(key_list)):
    character[key_list[i]] = value_list[i]
print(character)

limit = 10000
i = 1
sum_value = 0
while True:
    sum_value += i
    i = i+ 1
    if sum_value > limit:
        break
print("{}를 더할 때 {}을 넘으면 그때의 값은 {}입니다.".format(i-1, limit, sum_value))

max_value = 0
a = 0
b = 0

for i in range(101):
    j = 100 - i

    if i * j > max_value:
        max_value = i * j
        a, b= i,j
print("최대가 되는 경우 : {} * {} = {}".format(a,b,max_value))