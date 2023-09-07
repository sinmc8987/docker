# while문
# for문은 리스트를 반복하는 것이라면 while문은 조건이 만족될 때 까지 반복

'''
while 조건:
    실행 명령문1
    실행 명령문2
    실행 명령문3
    ....
'''

# index가 5부터 시작해서 0이될때까지 반복 출력 후 종료
customer = "토르" # 손님
index = 5 # 부르는 횟수, 총 5회

while index >= 1: # 부르는 횟수가 1 이상인 경우에만 반복 실행
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요.".format(customer, index))    
    index -= 1 # 부르는 횟수 감소
    if index == 0: # 5번 모두 불렀다면
        print("커피는 폐기처분되었습니다.")

# index가 1부터 시작해 계속 증가하여 무한루프.. ctrl + c 로 종료
# customer = "아이언맨"
# index = 1
# while True:
#    print("{0}, 커피가 준비 되었습니다. 호출 {1} 회".format(customer, index))
#    index += 1

# person이 처음엔 Unknown이고 input값을 입력받아 person이 토르일때까지 반복
customer = "토르"
person = "Unknown"

while person != customer:
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")