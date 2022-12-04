# 클래스
# result = 0

# def add(num):
#     global result
#     result += num
#     return result

# print(add(3))
# print(add(4))

# result1 = 0
# result2 = 0
# def add1(num):
#     global result1
#     result1 += num
#     return result1

# def add2(num):
#     global result2
#     result2 += num
#     return result2

# print(add1(3))
# print(add1(4))
# print(add2(3))
# print(add2(7))


# class Calculator:
#     def __int__(self):
#         self.result = 0

#     def add(self, num):
#         self.result += num
#         return self.result
# cal1 = Calculator()
# cal2 = Calculator()

# print(cal1.add(3))
# print(cal1.add(4))
# print(cal2.add(3))
# print(cal2.add(7))

# 과자 틀 -> 클래스(class)
# 과자 틀을 사용해 만든 과자 -> 객체(object)

#사칙연산 클래스 만들기
# # 더하기
# class FourCal:
#     def setdata(self,first,second):
#         self.first = first
#         self.second = second
    
#     def add(self):
#         result = self.first + self.second
#         return result

# a = FourCal()
# a.setdata(4,2)

# print(a.add())


# class FourCal :
#     def setdata(self,first,second):
#         self.first = first
#         self.second = second
        
#     def mul(self):
#         result = self.first * self.second
#         return result

#     def sub(self):
#         result = self.first - self.second
#         return result

#     def div(self):
#         result = self.first / self.second
#         return result

# a = FourCal()
# a.setdata(4,2)

# b = FourCal()
# b.setdata(6,2)

# print(a.sub())
# print(b.mul())



# 생성자
# 객체에 초깃값을 설정하지 않을때 사용

# class FourCal :
#     def __init__(self,first,second):
#         self.first = first
#         self.second = second

#     def setdata(self,first,second):
#         self.first = first
#         self.second = second

#     def add(self):
#         result = self.first + self.second
#         return result

#     def mul(self):
#         result = self.first * self.second
#         return result

#     def sub(self):
#         result = self.first - self.second
#         return result

#     def div(self):
#         result = self.first / self.second
#         return result

# a = FourCal(4,2) 
# print(a.first)
# print(a.second)

# print(a.add())
# print(a.mul())


# # 클래스의 상속
# # class 클래스 이름(상속할 클래스 이름)
# class MoreFourCal(FourCal):
#     pass

# a = MoreFourCal(4,2)
# print(a.add())

# class MoreFourCal(FourCal):
#     def pow(self):
#         result = self.first ** self.second
#         return result

# a = MoreFourCal(4,2)
# print(a.pow())



# # 곱하는 값이 0일 경우 'Fail' 문자열을 출력하는 클래스 FailFourCal을 위에서 만든 FourCal 클래스를 상속하여 만드시오.

# class FailFourCal(FourCal):
#     def mul(self):
#         if self.second == 0:
#             return 0
#         else:
#             return self.first * self.second
# a = MoreFourCal(4,0)
# print(a.mul())



# 클래스 변수
class Family :
    lastname = "Big"
    
print(Family.lastname)

a = Family()
b = Family()

print(a.lastname)
print(b.lastname)
