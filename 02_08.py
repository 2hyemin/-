# 자료형의 값을 저장하는 공간, 변수
# 변수 = 변수 값(객체)
# 변수 값(객체)은 메모리 주소를 가지게 된다
a = [1,2,3]
print(id(a))

# a를 b에 복사하면 같은 메모리 주소를 가지게 된다
b = a
print(id(b))
print(a is b)

# a 리스트 1을 4로 대체해도 a와 b의 값은 동일하게 된다
a[1] = 4
print(a)
print(b)

# 슬라이싱 [:] 사용
a = [1,2,3]
b = a[:] # b의 값은 a를 슬라이싱한 값을 가진다
a[1] = 4
print(a)
print(b) # a를 슬라이싱한 값을 가지기 때문에 a에 1을 4로 대체해도 b에 영향이 없다

# copy 모듈 사용
# copy(a) = a[:]
from copy import copy
a = [1,2,3]
b = copy(a)

# 같은 값으로 변수를 생성해도 다른 값을 가진다
a = [1,2,3]
b = [1,2,3]
print(a is b)

# 변수 여러개 만들기
a, b = ('python','Life')
print(a,b)

# 리스트 여러개 만들기
[a,b] = ['python','Life']
print([a,b])

# 여러개의 변수에 값 넣기
a = b = 'python'
print(a,b)

# 여러개의 변수 변경하기
a = 3
b = 5
a,b = b,a
print(a,b)