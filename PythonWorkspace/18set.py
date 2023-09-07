# 세트
# 세트(set, 집합), 중복을 허용하지 않으며 데이터의 순서도 보장하지 않는다. 중괄호{} 를 사용하여 선언

my_set = {1, 2, 3, 3, 3} # 중복을 허용하지 않으므로 3은 1번만 들어감
print(my_set) # {1, 2, 3}

# 정수, 문자열 등 다양한 형태의 값을 선언할 수 있다. 중괄호{} 대신 set() 을 사용할 수 있다.
java = {"유재석", "김태호", "양세형"} # 자바 개발자 집합
python = set(["유재석", "박명수"]) # 파이썬 개발자 집합

# 집합의 성질을 이용하여 두 집합 중 공통되는 값들만 뽑아내는 & 또는 intersection() 사용할 수 있다.
# 교집합 (java 와 python 을 모두 할 수 있는 개발자)
print(java & python) # {'유재석'}
print(java.intersection(python)) # {'유재석'}

# 합집합은 | 또는 union()을 사용할 수 있다.
# 합집합 (java 또는 python 을 할 수 있는 개발자)
# 유재석은 공통이지만 중복이 허용되지 않아 한번만 출력
print(java | python) # {'박명수', '유재석', '김태호', '양세형'}
print(java.union(python)) # {'박명수', '유재석', '김태호', '양세형'}

# 차집합은 - 또는 difference()를 사용할 수 있다.
# 차집합 (java 는 할 수 있지만 python 은 할 줄 모르는 개발자)
print(java - python) # {'양세형', '김태호'}
print(java.difference(python)) # {'양세형', '김태호'}

# 집합에 추가는 add()를 사용할 수 있다.
# python 개발자 추가 (기존 개발자 : 박명수, 유재석)
python.add("김태호")
print(python) # {'박명수', '유재석', '김태호'}

# 집합에서 제외는 remove()를 사용할 수 있다.
# java 개발자 삭제 (기존 개발자 : 유재석, 김태호, 양세형)
java.remove("김태호")
print(java) # {'유재석', '양세형'}