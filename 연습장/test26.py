with open("../3.1절 연설.txt", 'r') as file:
    list31 = file.read().strip().split(' ')
    list_temp = []
    for list in list31:
        list = list.replace(',', '')
        list = list.replace('.', '')
        list = list.replace("’", '')
        list = list.replace("‘", '')
        list = list.replace('”', '')
        list_temp.append(list)

word_list = filter(lambda word : len(word) >= 2, list_temp)

list_count = {}
for word in word_list:
    if word in list_count:
        list_count[word] += 1
    else:
        list_count[word] = 1

for key, value in list_count.items():
    if value > 3:
        print("{} : {} ".format(key, value))
