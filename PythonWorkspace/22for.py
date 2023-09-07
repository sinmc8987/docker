# for 반복문

print("대기번호 : 2")
print("대기번호 : 3")
print("대기번호 : 4")
# 여러 반복적인 처리가 필요할 때

'''
for 변수 in 반복대상:
    실행 명령문1
    실행 명령문2
    ...
'''

for waiting_no in [0,1,2,3,4]:
 print("대기번호 : {0}".format(waiting_no)) # {0} 위치에는 waiting_no 의 값이 들어가요
# 두 줄로 4개의 반복적인 출력을 처리

for waiting_no in range(1, 6): # 1부터 6직전까지 (1~5)
    print("대기번호 : {0}".format(waiting_no))
# 위의 예제와 같으 내용

# startbuct에 손님 리스트를 넣고, 그 리스트를 custom 변수에 하나씩 넣은 후 출력
starbucks = ["아이언맨", "토르", "아이엠 그루트"] # 손님 리스트
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다".format(customer))