list_a = [1,2,3,4,5,6]
list_b = [2,3,5,7,8,9]
list_c = list_a + list_b
print(list_c)
list_d = list_a * 3
print(list_d)
print(len(list_d))
list_e = len(list_a) - len(list_b)
print(list_e)
list_a.append('abc')
print(list_a)
list_a.insert(1, 'cbe')
print(list_a)
list_a.append(list_b)
print(list_a[-1][2])
print('list_d : ', list_d)
#del list_d[:5]
list_d.pop()
print('pop :    ', list_d)
list_d.remove(6)
print('remove : ', list_d)
list_d.clear()
print('clear :  ',list_d)