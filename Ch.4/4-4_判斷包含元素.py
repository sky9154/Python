# 判斷tuple
a=(1,2,3,4)
print("1在tuple a中" if 1 in a else "1不在tuple a中")
#判斷串列
a=[1,2,3,4]
print("5在串列a中" if 5 in a else "5不在串列 a中")
#判斷字典
a={'你好':'hello','嗨':'hi'}
print("'你好'在字典a中" if '你好' in a else "'你好'不在字典 a中")
#判斷集合
a=set('1234')
print("'5'在集合a中" if '5' in a else "'5'不在集合 a中")