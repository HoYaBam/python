example_dictionart = {
    "키A": "값A",
    "키B": "값B",
    "키C": "값C"
}

print("#딕셔너리의 items() 함수")
print("items() : ", example_dictionart.items())
print()

print("# 딕셔너리의 items() 함수와 반복문 조합하기")

for key, element in example_dictionart.items():
    print("dictionary[{}] = {} ".format(key, element))

print()

for ele in example_dictionart:
    print("dictionary[{}] = {}".format(ele, example_dictionart[ele]))

print()

array = [i*i for i in range(0, 20, 2)]
print(array)

print()

str = (
"첫번째 줄입니다."
"두번째 줄입니다."
"세번째 줄입니다.")
print(str)

print()

no1 = '1234565'
no2 = '9876543'

print("-".join([no1,no2]))
no = ['1','abc','23','def', '678']
no_str = "-".join(no)
print(no_str)

print()

numbers = [1,2,3,4,5,6]
print(numbers)
r_num = reversed(numbers)
print(r_num)
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))

print()

output = [i for i in range(1,101) if "{:b}".format(i).count("0") == 1]

for i in output:
    print("{} : {}".format(i,"{:b}".format(i)))

print("합계:", sum(output))



