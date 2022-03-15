#with open('test.txt', 'w') as file:
#    file.write("Hello Python Programming....!")

#with open('c:\\HTML\\test.txt', 'w') as file_a:
#    file_a.write("Hello Python Programming....!")

#with open('test.txt', 'r') as readfile:
#    contents = readfile.read()
with open('test.txt', 'a') as file_a:
    file_a.write('환영합니다. 파이썬 나쁘지않다')

fo = open("test.txt", 'rw+')

seq = ["This is 6th list\n", "this is 7th list"]
list =fo.writelines(seq)

fo.seek(0,0)
for index in range(7):
    line = fo.next()
    print("Line No %d - %s" % (index, list))

