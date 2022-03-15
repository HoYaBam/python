def print_3_times(n, value):
    for i in range(0,n):
        print(value)

print_3_times(5, "안녕하세요")

print()

def print_n_times(*values,n=3):
    for i in range(n):
        for value in values:
            print(value)

        print()

print_n_times("안녕하세요", "즐거운", "잠자는시간")


print()

a = 'abc'
b = 'def'
c = 'ghi'

print(a, end='')
print(b)
print(c)

print()

list_a = ['abc' ,'def' ,'ghi']
list_b = ['789', '456', '123']
for i in list_a:
    for j in list_b:
        print(i , j , sep='-',end=" ")


print('\n')

def test(a, b=10, c=100):
    print('a : ', a)
    print('b : ', b)
    print('c : ', c)
    return a+b+c

print(test(1))
print(test(3,30))
print(test(5,50,500))

def f(x):
    return 2 * x + 1

print(f(10))

def f2(x):
    return (x*x) + (2* x) + 1

print(f2(10))

print("\n")

def mul(*values):
    sum = 1
    for i in values:
        sum *= i

    return sum

print(mul(5,7,9,10))

