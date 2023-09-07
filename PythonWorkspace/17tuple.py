# 튜플
# 튜플은 처음 정의할 때를 제외하고 데이터 변경이나 추가, 삭제 등이 불가능, 리스트보다 속도가 빠르다.
# 튜플은 소괄호() 를 이용하여 정의

menu = ("돈까스", "치즈까스")
print(menu[0]) # 돈까스
print(menu[1]) # 치즈까스

# 서로 다른 값을 가지는 변수
name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby) # 김종국 20 코딩

# 튜플 형태로 한 줄에 여러 변수 선언 가능
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby) # 김종국 20 코딩