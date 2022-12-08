# 내장 함수
# abs 절대값
print(abs(-3))

# all(x)
# x가 모두 참이면 True, 거짓이 하나라도 있으면 False
# 반복 가능한 자료형에서 사용 가능 list, tuple, str, dictionary..
print(all([1,2,3]))
print(all([1,2,3,0]))

# any(x)
# x가 하나라도 참이면 True, 모두 거짓이면 False
print(any([1,2,3]))
print(any([0,1]))
print(any([0]))

# chr 아스키 코드 > 문자열 변환
print(chr(97))

# dir
# 객체가 가지고 있는 변수나 함수를 보여줌
print(dir([1,2,3])) # list가 가지고 있는 메소드를 보여줌
print(dir({'1':'a'})) # 딕셔너리가 가지고 있는 메소드를 보여줌

# divmod(a,b)
# a를 b로 나눈 몫과 나머지를 tuple 형식으로 노출
print(divmod(4,2))

# enumerate (=열거하다)
# 순서가 있는 자료형을 인덱스값을 포함하는 enum 객체로 전달
for i, name in enumerate(['bar','foo','body']):
    print(i, name)

# eval (expression)
# 실행 가능한 문자열(1+2, 'hi'+'a' 같은것)을 입력으로 받아 문자열을 실행한 결괏값을 돌려주는 함수
# 입력 받은 문자열로 함수나 클래스를 동적으로 실행하고 싶을 때 사용
print(eval('1+2'))
print(eval("'hi'+' '+'a'"))

# filter
# 참인 것만 묶어서 돌려준다.
def postive(x):
    return x > 0

print(list(filter(postive,([1,-3,2,0,-5,6]))))

print(list(filter(lambda x : x>0, [1,-3,2,0,-5,6])))

# hex
# 정수를 16진수로 변환
print(hex(244))

# id
# 객체를 입력 받아 객체의 고유 주소 값을 돌려주는 함수
a = 9
print(id(a))
print(id(9))

# input
# 사용자에게 입력 받는 함수
# a = input()
# print(a)

# int
# 정수로 변환해주는 함수
print(int(3.3))

# isinstance
# 첫번째 인수로 인스턴스, 두번째 인수로 클래스 이름을 받는다
# 인스턴스가 그 클래스의 인스턴스인지 판단하여 참이면 True, 거짓이면 False

class Person : pass # 아무 기능 없는 Person 클래스 생성
a = Person() # Person 클래스의 인스턴스 a 생성
print(isinstance(a,Person)) # a가 Person 클래스의 인스턴스인지 확인

b = 3
print(isinstance(b,Person))


# len
# 입력값의 길이를 돌려주는 함수
print(len("Python"))

# list
# 입력값을 리스트로 돌려주는 함수
print(list("python"))
print(list((1,2,3)))
a = (1,2,3)
b = list(a)
print(b)

# map 
# 함수(f)와 반복 가능한(interable) 자료형을 입력으로 받아 f가 수행한 결과값을 묶어서 돌려주는 함수
# 일반 함수를 사용한 경우
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result
result = two_times([1,2,3,4])
print(result)

# map 함수를 이용한 경우
def two_times(x) : return x *2
print(list(map(two_times, [1,2,3,4])))

# lambda 함수를 이용한 경우
print(list(map(lambda a: a* 2, [1,2,3,4])))

# max
# 인수로 반복 가능한 자료형을 입력받아 그 최댓값을 돌려주는 함수
print(max([1,2,3,4]))
print(max("python"))

# min
# 인수로 반복 가능한 자료형을 입력받아 그 최솟값을 돌려주는 함수
print(min([1,2,3,4]))
print(min("python"))

# oct
# 정수 형태의 숫자를 8진수 문자열로 돌려주는 함수
print(oct(32123))

# open
# '파일 이름'과 '읽기 방법'을 입력받아 파일 객체로 돌려주는 함수
# '읽기 방법'을 생략하면 읽기 전용 모드(r)로 파일 객체를 만들어 돌려준다.
# w 모드 = 쓰기 모드로 파일 열기
# r 모드 = 읽기 모드로 파일 열기
# a 모드 = 추가 모드로 파일 열기
# b 모드 = 바이너리 모드로 파일 열기
# f = open("binary_file", 'rb') -> 바이너리 읽기 모드

# ord
# 문자의 아스키 코드 값을 돌려주는 함수
print(ord('a'))

# pow
# pow(x,y)는 x의 y 제곱 값을 돌려주는 함수
print(pow(2,2))

# range
# range([start,] stop [,stop])
# for 문과 함께 자주 사용하는 함수
# 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 돌려준다.

# 인수가 하나인 경우
print(list(range(5)))

# 인수가 두개인 경우
# 0부터 시작하기때문에 9까지 출력
print(list(range(5, 10)))

# 인수가 세개인 경우
# 1부터 9까지의 2간격으로 출력
print(list(range(1,10,2)))

# round
# round(number[,ndigits])
# 숫자를 입력받아 반올림 해주는 함수
print(round(4.6))
print(round(4.2))

# sorted
# sorted(iterble)
# 입력값을 정렬하여 리스트로 출력
print(sorted([23,4,1,2]))
print(sorted("zero"))

# str
# str(object)
# 문자열 형태로 객체를 변환하여 출력
print(str(123))
print(str('hi'))

# sum
# sum(interable)
# 리스트나 튜플의 모든 요소를 합하여 출력
print(sum([1,2,3]))

# tuple
# tuple(interable)
# 반복 가능한 자료형을 입력 받아 tuple 형태로 변환하여 출력
print(tuple("abc"))
print(tuple([1,2,3]))

# type
# type(object)
# 입력값의 자료형이 무엇인지 알려주는 함수
print(type("abc"))
print(type([1,2,3]))

# zip
# 동일한 개수로 이루어진 자료형을 묶어주는 함수
print(list(zip([1,2,3],[4,5,6])))
print(list(zip("ab","cd")))