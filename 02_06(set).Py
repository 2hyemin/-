#집합 자료형
s1 = set([1,2,3])
s2 = set("Hello")
print(s1)
print(s2)
#lHoe가 출력되는 이유
#1. 자료형은 중복을 허용하지 않음
#2. 자료형은 순서가 없음
#순서가 없기 때문에 인덱싱 지원하지 않음(딕셔너리랑 동일)

s1 = set([1,2,3])
# lsit 변환
li = list(s1)
print(li)
print(li[0])

t1 = tuple(s1)
# tuple 변환
print(t1)
print(t1[2])

s1 = set([1,2,3,4,5,6])
s2 = set([4,5,6,7,8,9])
#s1과 s2의 교집합 구하기 (&, intersection)
print(s1&s2)
print(s1.intersection(s2))

#s1과 s2의 합집합 구하기 (|, union)
print(s1|s2)
print(s1.union(s2))

#s1과 s2의 차집합 구하기 (-, difference)
print(s1-s2)
print(s1.difference(s2))

#집합 자료형 관련 함수
#값 추가 하기 (add)
s1 = set([1,2,3])
s1.add(4)
print(s1)

#값 여러개 추가하기 (update)
s1.update([4,5,6])
print(s1)

#특정 값 제거 (remove)
s1.remove(4)
print(s1)