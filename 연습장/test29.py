list_number = [52, 273, 32, 72, 100]
try:
    number_input = int(input('정수 입력 >'))
    print("{}번째 요소 : {}".format(number_input, list_number[number_input]))
except ValueError as e:
    print('정수를 입력하시오: ')
except IndexError as e:
    print('리스트 인덱스 범위 에러')
except Exception as e:
    print('기타 에러!@!!')


