# Q1. 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해보자
# number = 3
# def is_odd(number):
#     if number % 2 == 0:
#         return True
#     else :
#         return False
# print(is_odd(3))

# # Q2. 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자. (단 입력으로 들어오는 수의 개수는 정해져있지 않다)
# def avg_numbers(*args):
#     result = 0
#     for i in args:
#         result += i
#     return result / len(args)
# print(avg_numbers(1,2,3))


# Q3. 다음 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다.
#     오류를 수정해라

# input1 = input("첫번째 숫자를 입력하세요")
# input2 = input("두번째 숫자를 입력하세요")

# print(int(input1) + int(input2))