# Function decorator
# 본체 함수를 건드리지 않고 그 함수가 실행 되기 전과 후에 추가적인 로직을 덧붙이는 방식

def deco(a): # 장식 함수
    def wrapping() : # deco를 즉각 쓰는 게 아니라 나중에 쓰는 게(포장할 때) 핵심
        print("-------")
        a()
        print("-------")
    return wrapping # 나중에 포장된 채로 return

@deco
# 함수 데코레이터는 hello = deco(hello)와 동일한 기능
def hello(): # 본체 함수
    print("Hello World")

hello()