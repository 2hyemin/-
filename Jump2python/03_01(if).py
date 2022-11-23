# if 문
# if 문 뒤에는 항상 세미콜론(:)이 붙는다
money = True
if money :
    print("택시를 타고 간다")
else :
    print("걸어간다")


#만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어가라
money == 2000
if money >= 3000 :
    print("택시")
else :
    print("걸어")


#돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어가라
money == 2000
card = True
if (money >=3000 or card == True):
    print("택시")
else :
    print("걸어")

# in, not in
print(1 in [1,2,3])
print(5 in {1,2,3})
print(2 in (1,2,3))

#만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어가라
pocket = ['money','cell']
if 'money' in pocket :
    print("택시")
else :
    print("걸어")

#주머니에 돈이 있으면 가만히 있고 주머니에 돈이 없으면 카드를 꺼내라 (조건문에서 아무 동작하지 않게)
pocket = ['card','cell']
if 'money' in pocket:
    pass
else :
    print('카드꺼내')

# elif
# 주머니에 돈이 있으면 택시를 타고, 주머니에 돈은 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어가라

pocket = ['cell']
if 'money' in pocket :
    print("택시")
elif 'card' in pocket :
    print("택시")
else :
    print("걸어")