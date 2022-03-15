# import datetime
#
# now = datetime.datetime.now()
#
# year = now.year
# print(now.month)
# print(now.day)
# hour = now.hour
# print(now.minute)
# print(now.second)
#
# if hour < 12 :
#     print("현재 시간은 {}시로 오전 입니다.".format(hour))
# else:
#     print("현재 시간은 {}시로 오후 입니다.".format(hour))

# 키보드로 부터 생일 입력을 받아 맨 뒷자리가 0 , 5 는 월요일 쉽니다
# 01234 56789 16 화요일 쉽니다
#
# birthday = input("생일 입력 : ")
# if birthday[3] in ('0','5'):
#     print('월요일은 쉽니다')
# elif birthday[3] in ('1','6'):
#     print('화요일은 쉽니다')
# elif birthday[3] in ('2','7'):
#     print('수요일은 쉽니다')
# elif birthday[3] in ('3','8'):
#     print('목요일은 쉽니다')
# elif birthday[3] in ('4','9'):
#     print('금요일은 쉽니다')

# score = input("점수 입력 : ")
# score = int(score)
#
# if score >= 90 and score <= 100:
#     print('A학점')
# elif score >= 80 and score < 90:
#     print('B학점')
# elif score >= 70 and score < 80:
#     print('C학점')
# elif score >= 60 and score < 70:
#     print('D학점')
# elif score < 60 and score >= 0:
#     print('F학점')
# else:
#     print("잘못된 점수입니다")


# if score:
#     print(True)
# else:
#     print(False)

a = 3 % 3
print(a)





