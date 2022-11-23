# 함수
# 함수의 구조
# def 함수 이름(매개변수):
# 수행할 문장 1 ~n

def add(a,b):
    return a + b

a = 3
b = 4
c = add(a,b)
print(c)

print(add(3,4))

a = add(3,4)
print(a)

# 입력값이 없는 함수
# 결과값을 받을 변수 = 함수 이름()
def say():
    return 'Hi'

a = say()
print(a)


# 결괏값이 없는 함수
# 함수 이름(매개변수1, 매개변수2...)
def add(a,b):
    print("%d, %d의 합은 %d 입니다." % (a, b, a+b))

print(add(3,4))

# 입력값, 결괏값이 없는 함수
# 함수 이름()
def say():
    print('Hi')
say()

#매개변수 지정하여 호출하기
def add(a,b):
    return a+b

result = add(a=3,b=7)
print(result)


# 입력값이 몇개인지 모를때
# def 함수 이름(*매개변수):
#   수행할 문장...

# 여러개의 입력값을 받는 함수 만들기
# args는 매개변수(arguments의 약자)
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result
print(result)

result = add_many(1,2,3)
print(result)


def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul" :
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add',1,2,3,4,5)
print(result)

result = add_mul('mul',1,2,3,4,5)
print(result)


# 키워드 파라미터
# **kwargs(keyword arguaments)
# print_kwargs 함수는 kwargs를 출력하는 함수

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)
print_kwargs(name='foo',age=3)


# 함수의 결괏값은 언제나 하나이다
def add_and_mul(a,b):
    return a+b, a*b
result = add_and_mul(3,4)
print(result) # tuple 형태로 출력됨


# 결괏값처럼 받고 싶으면
result1, result2 = add_and_mul(3,4)
print(result1,result2)

# 매개변수에 초깃값 미리 설정하기
def say_myself(name, old, man = True):
    print("나의 이름은 %s 입니다" % name)
    print("나의 나이는 %d 입니다" % old)
    if man:
        print("나는 남자입니다.")
    else :
        print("나는 여자입니다.")

say_myself("영식이",32, True)
print(say_myself)

# 함수 안에서 선언한 변수의 효력 범위
# vartest.py
a = 1
def vartest(a):
    a = a +1

# return
a = 1
def vartest(a):
    a = a + 1
    return a

a = vartest(a)
print(a)

# global
a = 1
def vartest():
    global a
    a = a +1
vartest()
print(a)

# lambda
# def와 동일한 예약어
# lambda 매개변수 1, 매개변수2....

add = lambda a, b : a+b
result = add(3,4)
print(result)
