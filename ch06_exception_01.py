try :
    number_input = int(input("enter a number: "))
    # print
    print("반지름 : ", number_input)
    print("원의 둘레 : ", number_input * 2 * 3.14)
    print("원의 넓이 : ", 3.14 * number_input ** 2)
except Exception as exception:
    print("type(exception): ", type(exception))
    print("exception : ", exception)
