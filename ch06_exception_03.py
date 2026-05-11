list_numbers = [11, 23, 234, 29, 66, 642, 48]

try :
    number_input = int(input("enter a number: "))
    print("{}번째 요소 : {}".format(number_input, list_numbers[number_input]))

except ValueError as VE:
    print("정수를 입력하세요")
    print("exception : ", VE)

except IndexError as IE:
    print("입력한 값이 리스트 인덱스 범위를 벗어났습니다")
    print("exception : ", IE)