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
add = 0
for i in range(1, 11):
    add = add + i
    print(add)


marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] <60:continue
    print("%d학생 축" % (number+1))

# for문과 range 함수를 사용해 1부터 100까지 더해보자.
add = 0
for i in range(1,101):
    add = add + i
    print(add)