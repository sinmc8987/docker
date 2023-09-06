# 탈출 문자

print("백문이 불여일견 백견이 불여일타")
# 이 문장을 두줄로
# 백문이 불여일견
# 백견이 불여일타
# 이렇게 하려면 탈출문자를 써야 한다.

print("백문이 불여일견\n백견이 불여일타")

# 백문이 불여일견
# 백견이 불여일타

# print("저는 "나도코딩"입니다.") 에러발생

print("저는 '나도코딩'입니다.") # 저는 '나도코딩'입니다.
print('저는 "나도코딩"입니다.') # 저는 "나도코딩"입니다.

# 탈출문자 \를 활용
print("저는 \"나도코딩\"입니다.") # 저는 "나도코딩"입니다.
print("저는 \'나도코딩\'입니다.") # 저는 '나도코딩'입니다.

# print("C:\Users\Nadocoding\Desktop\PythonWorkspace>") # 에러 발생

print("C:\\Users\\Nadocoding\\Desktop\\PythonWorkspace>") # C:\Users\Nadocoding\Desktop\PythonWorkspace>

# 참고로 문자열을 있는 그대로 출력하고 싶을 때 문자열 앞에 r 을 넣는 방법도 있습니다. 
# 그러면 문자열 내에서 어떤 값이 포함되어 있던지 개의치 않고 그대로 출력한답니다. 
# 탈출문자가 포함되어 있어도 말이죠. 즉 다음 문장은 올바르게 경로를 잘 출력하게 됩니다.
print(r"C:\Users\Nadocoding\Desktop\PythonWorkspace>") # raw string

# 자주 사용되지는 않지만 탈출문자 중에는 \r 과 \b 도 있습니다.
# \r 은 커서를 맨 앞으로 이동시키는 역할을 하는데요. 
# 다음과 같은 문장이 있을 때 "Pine" 의 P 를 출력하기 이전에 커서를 맨 앞으로, 
# 즉 "Red " 앞으로 이동시켜서 마치 "Red " 를 덮어쓰는 효과를 내게 됩니다. 
# 그래서 출력결과는 PineApple 이 되는 것이죠.
print("Red Apple\rPine") # PineApple

# \b 는 키보드의 백스페이스와 같은 역할을 합니다. 
# 즉 앞 글자 하나를 삭제해주는 것이죠. 예제에서는 "Redd" 중 마지막 "d" 를 없앤 값이 출력됩니다.

print("Redd\bApple") # RedApple

# 마지막으로 \t 도 있습니다. 
# 키보드의 탭 (Tab) 과 같이 여러 칸 (보통 8칸 단위) 을 띄어주는 역할을 한답니다.

print("Red\tApple") # Red     Apple