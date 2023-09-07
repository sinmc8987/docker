# 자료구조의 변경

# 세트를 만들고 여러 타입으로 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu)) # menu 의 type 정보 : set

# 세트를 리스트로 변경
menu = list(menu) # 리스트 형태로 변환
print(menu, type(menu)) # menu 의 type 정보 : list

# 리스트를 튜플로 변경
menu = tuple(menu) # 튜플 형태로 변환
print(menu, type(menu)) # menu 의 type 정보 : tuple

# 튜플을 세트로 변경
menu = set(menu) # 세트 형태로 변환
print(menu, type(menu)) # menu 의 type 정보 : set