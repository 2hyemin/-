# for 문
# test_list = ['one','two','three']
# for i in test_list :
#     print(i)

# a = [(1,2),(3,4),(5,6)]
# for (first, last) in a :
#     print(first+last)


# 총 5명의 학생이 시험을 보았는데 시험 점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다.
# 합격인지 불합격인지 결과를 보여주시오.
# marks = [90, 25, 67, 45, 80]
# number = 0
# for mark in marks :
#     number = number + 1
#     if mark >= 60 :
#         print("%d번째 학생은 합격입니다." % number)
#     else :
#         print("%d번째 학생은 불합격입니다." % number)

# for, continue
# # 60점 이상인 사람에게 축하 메시지를 보내라.
# marks = [90, 25, 67, 45, 80]
# number = 0
# for mark in marks :
#     number = number + 1
#     if mark < 60: continue
#     print("%d번째 학생 합격을 축하해요" % number)


# for, range
# add = 0
# for i in range(1, 11):
#     add = add + i
#     print(add)


# marks = [90, 25, 67, 45, 80]
# for number in range(len(marks)):
#     if marks[number] <60:continue
#     print("%d학생 축" % (number+1))

# for문과 range 함수를 사용해 1부터 100까지 더해보자.
# add = 0
# for i in range(1,101):
#     add = add + i
#     print(add)

# 99단
# for i in range(1,10):
#     for j in range(1,10):
#         print(i*j, end = " ")
#     print(' ')

# 리스트 내포(List comprehension) 사용하기
a = [1,2,3,4]
result = []
for num in a :
    result.append(num*3)
print(result)

# 위 와 같음
a = [1,2,3,4]
result = [num * 3 for num in a]
print(result)

# a 값 중 짝수만 3을 곱하고 싶다.
# [표현식 for 항목 in 반복 가능 객체 if 조건]
a = [1,2,3,4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)

#구구단 리스트 내포
result = [x*y for x in range(1,10)
    for y in range(1,10)]
print(result)



