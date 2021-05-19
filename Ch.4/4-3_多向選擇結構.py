# 評語判斷
a=int(input())
if a>=80:
    print("非常好")
elif a>=60:
    print("不錯喔")
else:
    print("要加油")
# 郵資計算
import math
a=int(input())
print("郵資為%d元"%((50+(math.ceil(a/5)-1)*20)) if a<=20 else "無法配送")