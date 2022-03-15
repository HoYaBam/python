with open("../우크라이나.txt", 'r') as file:
    word_list = file.read().strip().split(' ')
    word_temp = []
    for word in word_list:
        word = word.replace('\n', '')
        word = word.replace('(', ' ')
        word = word.replace(')', '')
        word = word.replace('\'', '')
        word = word.replace('<', '')
        word = word.replace('>', '')
        word = word.replace('.', '')
        word = word.replace('\\n', '')
        word = word.replace('/', '')
        word_temp.append(word)

word_list = word_temp


print(word_list)

print(word_list)
print(len(word_list))

word_list = filter(lambda word : len(word) >= 2 and len(word) <= 7,
                   word_list)

word_lists = list(word_list)
print(word_lists)
print(len(word_lists))

for word in word_lists:
    print(word)
    print(len(word))

word_count = {}

for word in word_lists:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

for key, value in word_count.items():
    print("{} : {} ".format(key , value))