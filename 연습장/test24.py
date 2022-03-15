weight_sum = 0
height_sum = 0
cnt = 0

with open("../info.txt", "r") as file:
    for line in file:
        (name, weight, height) = line.strip().split(",")

        if (not name) or (not weight) or (not height):
            continue

        bmi = int(weight) / ((int(height) / 100) ** 2)


        cnt += 1
        weight_sum += int(weight)
        height_sum += int(height)

        result = ''

        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상 체중"
        else:
            result = "저체중"

        print('\n'.join([
            "이름 : {}",
            "몸무게 : {}",
            "키 : {}",
            "BMI : {}",
            "결과 : {}"
        ]).format(name, weight, height, bmi, result))
        print()

print("몸무게 평균 : {} \n"
      "키 평균 {} \n"
      "인원수 : {} \n".format(weight_sum / cnt , height_sum / cnt , cnt))

