a = "19891125Rainy"
date = a[:8]
weather = a[8:]
print(weather)
print(date)


print("{0:!^12}".format("python"))

a = [1,2,3,['a','b','c']]
print(a[-1][0])

a = [1,2,['a','b',['Life','is']]]
print(a[-1][-1][0])

a = [1,2,3,4,5]
print(a[1:3])

a = [1,2,3,['a','b','c'],4,5]
print(a[2:5])
print(a[3][:2])

t1 = 1, 2, 3
print(t1 +(4,))

a = {1:'a'}
a[2] = 'b'
print(a)

dic = {'name':'pey', 'phone':'01051188254', 'birth':'1125'}
print(dic['name'])
print(dic.items())
print(dic.get('name'))
print(dic.values())
print(dic.get('monkey'))
print(a.get('foo','bar'))
print('name' in dic)
print('age' in dic)

a = {'name':'홍길동', 'birth':'1125', 'age':'30'}