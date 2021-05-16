a=[1,2,3,4,5]
#len() 查詢串列長度
print("串列a的長度為",len(a))
#修改單獨元素
a[1]="a"
print(a)
#append()加入元素到最後
a.append(6)
print(a)
#insert()加入元素到指定位置
a.insert(1,2)
print(a)
#remove()移除指定元素
a.remove('a')
print(a)
#sort()排序串列元素
a=[5,4,3,2,1]
a.sort()
print(a)
#for 讀取串列元素
for i in a:
    print(i)
#split()產生串列
print("2002/5/4".split('/'))