# 문자열 처리 함수

# lower : 소문자로 변환
# upper : 대문자로 변환
# isupper : 대문자인지 확인
# islower : 소문자인지 확인
# replace : 문자열 바꾸기
# index : 찾으려는 문자열의 인덱스 (없으면 에러)
# find : 찾으려는 문자열의 인덱스 (없으면 -1 반환)
# count : 문자열이 나온 횟수

python = "Python is Amazing"

print(python.lower()) # python is amazing
print(python.upper()) # PYTHON IS AMAZING
print(python[0].isupper()) # True : 0 번째 인덱스의 값이 대문자인지 확인
print(len(python)) # 17 : 띄어쓰기를 포함한 문자열의 전체 길이 (length)
print(python.replace("Python", "Java")) # Java is Amazing

index = python.index("n") # 처음으로 발견된 n 의 인덱스
print(index) # 5 : Python 의 n
index = python.index("n", index + 1) # 6 번째 인덱스 이후에 처음으로 발견된 n 의 인덱스 
print(index) # 15 : Amazing 의 n

find = python.find("n") # 처음으로 발견된 n 의 인덱스
print(find) # 5 : Python 의 n
find = python.find("n", find + 1) # 6 번째 인덱스 이후에 처음으로 발견된 n 의 인덱스 
print(find) # 15 : Amazing 의 n

# print(python.index("Java")) # Java 가 없기 때문에 에러가 발생하며 프로그램 종료
print(python.find("Java")) # Java 가 없으면 -1 을 반환(출력)하며 프로그램 계속 수행