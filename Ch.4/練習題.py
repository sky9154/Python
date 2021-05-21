# BMI常用來判斷肥胖程度，BMI 等於體重（KG）除以身高（M）的平方，會有一個分類標準，
# 假設BMI 與肥胖分級如下。請寫一個程式讓使用者輸入身高與體重，顯示BMI 值與肥胖程度。
m,k=map(float,input("輸入身高(M)及體重(KG)").split())
bmi=k/(m**2)
print("BMI為:",bmi)
if bmi<18:
    print("體重過輕")
if 18<=bmi and bmi<24:
    print("體重正常")
if 24<=bmi and bmi<27:
    print("體重過重")
if bmi>=27:
    print("體重肥胖")