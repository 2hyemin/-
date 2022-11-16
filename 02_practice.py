#Q1. 홍길동씨의 과목별 점수는 다음과 같다.
#    홍길동씨의 평균 점수를 구해보자
#    국어 80, 영어 75, 수학 55
han = 80
english = 75
math = 55

hong_avg = (han+english+math)/3
print(hong_avg)


#Q2. 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법에 대해 말해보자
a = 13%2
if a == 0:
    print("짝수")
else :
    print("홀수")


#Q3. 홍길동씨의 주민번호는 881120-1068234이다.
# 홍길동씨의 주민번호를 연월일 (YYYMMDD)부분과 그 뒤의 숫자 부분으로 나누어 출력해보자.
ju = {'연월일':881120, '성별':1068234}
print(ju.values())

pin = "881120-1068234"
print(pin[:6],pin[7:])

#Q4. 주민번호 뒷자리의 맨 첫번째 숫자는 성별은 나타낸다. 주민번호에서 성별을 나타내는 숫자를 출력해보자.
pin = "881120-1068234"
print(pin[7])

#Q5. 다음과 같은 문자열 a:b:c:d가 있다. 문자열의 replace 함수를 사용하여 a#b#c#d로 바꿔서 출력해보자
a = "a:b:c:d"
print(a.replace(":",'#'))

#Q6. [1,3,5,4,2] 리스트를 [5,4,3,2,1]로 만들어보자
a = [1,3,5,4,2]
b = reversed(sorted(a))
print(list(b))

#Q7. ['Life','is','too','short'] 리스트를 Life is too short 문자열로 만들어 출력해보자
a = ['Life','is','too','short']
print(" ".join(a))

# Q8. (1,2,3) 튜플에 값 4를 추가하여 (1,2,3,4)로 만들어 출력
a = (1,2,3)
b = 4,
print(a+b)

# Q10. 딕셔너리 a에서 'B'에 해당되는 값을 추출
a = {'A':90,'B':80,'C':70}
print(a.pop('B'))

# Q11. a 리스트에서 중복 숫자를 제거
a = [1,1,1,2,2,3,3,3,4,4,5]
print(list(set(a)))
