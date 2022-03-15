dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자항색소"],
    "origin": "필리핀"
}

print(dictionary["name"])

dictionary["name"] = "8D 건조 망고"
print(dictionary["name"])

numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1

print(counter)
dact_a = {};
dact_a['name'] = '구름'
print(dact_a)
del dact_a["name"]
print(dact_a)

pets = [ {"name" : "구름", "age": 5},
         {"name" : "초코", "age": 3},
         {"name" : "아지", "age": 1},
         {"name" : "호랑이", "age": 1}]

print("# 우리 동네 애완 동물들")
for i in pets:
    print('{} {}살'.format(i["name"], i["age"]))

character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이드"
    },
    "skill": ["베기", "세게 베게", "아주 세게 베기"]
}

for key in character:
    if type(character[key]) is str or type(character[key]) is int:
        print(key + " : ", character[key])
    elif type(character[key]) is list:
        for skill in character[key]:
            print(key + " : ", skill)
    elif type(character[key]) is dict:
          for item in character[key]:
              print(item + " : " , character[key][item])





