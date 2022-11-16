# Bool 자료형
# True/False

# type 출력
a = True
b = False
print(type(a))

# true/false 확인
print(1 == 1)
print(2 < 1)

# while 조건문
a = [1,2,3,4]
while a : #a이가 참인 동안
    print(a.pop()) #a 값을 꺼내라

#####자료형 참/거짓#####
# [리스트] 안에 비었기 때문에 거짓을 출력한다
if[]:
    print("참")
else:
    print("거짓")

# [리스트] 안에 값이 있기 때문에 참을 출력한다
if[1,2,3] :
    print("참")
else:
    print("거짓")

#####Bool 연산#####
# bool 안에 문자열이 있기 때문에 참을 출력한다
print(bool('python'))
# bool 안에 문자열이 없기 때문에 거짓을 출력한다
print(bool(''))

print(bool([1,2,3]))
print(bool([]))
print(bool(0))
print(bool(1))