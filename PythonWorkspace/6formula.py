# 간단한 수식

print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20

number = 2 + 3 * 4 # 14
print(number)

# 변수의 값에 2를 더해서 저장 후 출력
number = number + 2 # 16
print(number)
# 위와 동일한 내용
number += 2 # number = number + 2 와 동일
print(number) # 18

number *= 2 # number = number * 2 와 동일
print(number) # 36

number /= 2 # number = number / 2 와 동일
print(number) # 18

number -= 2 # number = number - 2 와 동일
print(number) # 16

number %= 2 # number = number % 2 와 동일
print(number) # 0