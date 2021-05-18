#set用法
a=set(('a',1,'b',2,'c',3))
print(a)
a=set(['apple','banana','apple'])
print(a)
a=set('apple')
print(a)
a.add('s')
print(a)
a.remove('s')
print(a)
#集合運算
a=set("abcde")
b=set("bcde")
print(a|b) #聯集
print(a&b) #交集
print(a-b) #差集
print(a^b) #互斥或
#集合比較
print(a>=b)
print(a>b)
print(a<=b)
print(a<b)