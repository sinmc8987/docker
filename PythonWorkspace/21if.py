# if문
# if 조건:
# 실행 명령문

weather = "비"

if weather == "비":
 print("우산을 챙기세요")

'''
잠깐!
파이썬에서는 들여쓰기가 굉장히 중요합니다. 예를 들어서

if 만약 초코파이가 있으면:
    초코파이를 사와
오예스를 사와

이렇게 하면 초코파이가 있을 땐 초코파이+오예스를, 없을 땐 오예스만 사게 됩니다. 반면에

if 만약 초코파이가 있으면:
    초코파이를 사와
    오예스를 사와

이렇게 하면 초코파이가 있을 때만 초코파이+오예스를 사게 되며, 없을 땐 아무것도 사지 않게 됩니다.
'''

# if 조건에 맞지 않기 때문에 아무것도 출력 되지 않음
weather = "맑음" # 맑음으로 바꾸면 실행 안됨

if weather == "비":
    print("우산을 챙기세요")


# weather 변수가 "미세먼지"이므로 elif문의 print를 실행
weather = "미세먼지"

if weather == "비":
    print("우산을 챙기세요") # 1번
elif weather == "미세먼지":
    print("마스크를 챙기세요") # 2번

'''

if 조건1:
    실행 명령문1
elif 조건2:
    실행 명령문2
elif 조건3:
    실행 명령문3
else:
    실행 명령문4 # 위 모든 조건들에 해당하지 않을 때 실행
'''

# weather 변수 값이 "맑아요" 이므로 if와 elif 모두 만족하지 않아 else문의 print를 실행
weather = "맑아요"

if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

# input을 이용해 입력 값을 받고 그 입력값을 변수로 넣어 변수 출력
weather = input("오늘 날씨는 어때요? ")
print(weather) # 사용자가 입력한 값 출력

# input을 이용해 입력 값을 받고 그 입력값을 변수로 넣어 if문 실행
weather = input("오늘 날씨는 어때요? ")
# print(weather) # 사용자가 입력한 값 출력 # 주석 처리

if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")

# 위의 예제에서 조건을 변경
weather = input("오늘 날씨는 어때요? ")
# print(weather) # 사용자가 입력한 값 출력 # 주석 처리

if weather == "비" or weather == "눈": # 조건 변경
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")


# input()은 항상 문자열로 인식하기때문에 숫자를 입력받으면 int()로 감싸줘야 한다.

temp = int(input("기온은 어때요? "))
if 30 <= temp: # 30 도 이상이면
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30: # 10도 이상 30도 미만이면
    print("괜찮은 날씨에요")
elif 0 <= temp and temp < 10: # 0도 이상 10도 미만이면
# 위 비교 문장은 이렇게도 작성 가능합니다.
# elif 0 <= temp < 10:
    print("외투를 챙기세요")
else: # 그 외의 모든 경우 (0도 미만이면)
    print("너무 추워요. 나가지 마세요")