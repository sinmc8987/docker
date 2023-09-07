# 사전
# 중괄호{} 로 둘러싸 정의, key와 value는 콜론:으로 구분 key:value

cabinet = {3: "유재석", 100: "김태호"}

print(cabinet[3]) # 유재석 -> key 3 에 해당하는 value
print(cabinet[100]) # 김태호 -> key 100 에 해당하는 value

# 대괄호[]가 아닌 get을 이용하는 방법
print(cabinet.get(3)) # 유재석 -> key 3 에 해당하는 value

# 대괄호[] 를 이용했을 때 에러 발생 시 프로그램 종료, get 이용했을 때 에러 발생 시 None 반환

# print(cabinet[5]) # key 가 5 인 값이 없을 땐 에러 발생 후 프로그램 종료 (hi 출력 안됨)
# print("hi")

print(cabinet.get(5)) # key 가 5 인 값이 없을 땐 None 반환 후 계속 진행 (hi 출력됨)
print("hi")

# 5가 사전에 있을 경우에는 5에 해당하는 value가 출력, 없을 경우에는 "사용 가능" 출력
print(cabinet.get(5, "사용 가능")) # key 에 해당하는 값이 없는 경우 기본 값을 사용

# key값이 사용중인지는 in을 통해서 확인 가능
# 사전 자료형에 값이 있는지 여부 확인
print(3 in cabinet)  # True
print(5 in cabinet)  # False

# key는 정수형이 아닌 문자열도 가능
cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"]) # 유재석
print(cabinet["B-100"]) # 김태호

# 업데이트 또는 추가
print(cabinet) # {'A-3': '유재석', 'B-100': '김태호'}
cabinet["A-3"] = "김종국" # key 에 해당하는 값이 있는 경우 업데이트
cabinet["C-20"] = "조세호" # key 에 해당하는 값이 없는 경우 신규 추가
print(cabinet) # {'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}

# 삭제
del cabinet["A-3"] # key "A-3" 에 해당하는 데이터 삭제
print(cabinet) # {'B-100': '김태호', 'C-20': '조세호'}

# key 들만 출력
print(cabinet.keys()) # dict_keys(['B-100', 'C-20'])

# value 들만 출력
print(cabinet.values()) # dict_values(['김태호', '조세호'])

# key, value 쌍으로 출력
print(cabinet.items()) # dict_items([('B-100', '김태호'), ('C-20', '조세호')])

# 전체 삭제
cabinet.clear()
print(cabinet) # {}