#tuple()可將串列轉換成tuple
a=[1,2,3,4]
print(tuple(a))
#可用" , "串接
b=1,2,3,4
print(b)
#可用變數取出tuple中的元素
c=(1,2,3)
x,y,z=c
print("x=",x,"y=",y,"z=",z)
#可交換變數
print("交換前\nx=",x,"y=",y)
x,y=y,x
print("交換後\nx=",x,"y=",y)