# Q1.다음 코드의 결과값은 무엇일까?
# need
# a = "Life is too short, you need python"
# if "wife" in a : print("wife")
# elif "python" in a and "you" not in a :
#     print("python")
# elif "shirt" in a :
#     print("shirt")
# elif "need" in a :
#     print("need")
# else :
#     print("none")


# Q2.while문을 사용해 1 ~ 1000까지의 자연수 중 3의 배수의 합을 구해보자
# result = 0
# i = 1
# while i <= 1000:
#     if i % 3 == 0:
#         result += i
#     i += 1
# print(result)



# # Q3. while 문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해보자.
# # *
# # **
# # ***
# # ****
# # *****
# i = 0
# while True:
#     i += 1
#     if i > 5 : break
#     print('*' * i)

# # Q4. for 문을 사용해 1부터 100까지의 숫자를 출력해보자.
# for i in range(1,101):
#     print(i)

# Q5. for 문을 사용하여 A 학급의 평균 점수를 구해보자.
# A = [70, 60, 55, 75, 95, 90, 80, 85, 100]
# total = 0
# for score in A :
#     total += score
# average = total / len(A)
# print(int(average))

# # Q6. 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음과 같은 코드가 있다
# numbers = [1,2,3,4,5]

# result = []
# for n in numbers :
#     if n % 2 == 1:
#         result.append(n*2)
# 위 코드를 리스트 내포를 사용하여 표현해 보자.

# numbers = [1,2,3,4,5]
# result = [n*2 for n in numbers if n%2 == 1]
# print(result)

# Q7-1. '주머니에 카드가 없다면 걸어가고, 있다면 버스를 타고 가라'는 문장을 조건문으로 말들어보자.
# pocket = ['card','money','keys']
# if 'card' in pocket:
#     print('버스타고 가')
# else :
#     print('걸어가')


# # Q7-2. 1부터 10까지 숫자중에서 3의 배수를 뺀 나머지 값을 출력해보자.
# a = 0
# while a < 10:
#     a = a + 1
#     if a % 3 == 0 : continue
#     print(a)



# Q7-3. for 문과 range 함수를 사용하여 1부터 100까지 더해보자.
# a = 0
# for i in range(1,101):
#     a += i
#     print(a)
