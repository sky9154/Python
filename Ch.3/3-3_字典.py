lang={"早安":"Good Morning","你好":"Hello"}
print(lang)
print("[你好]的英文為>",lang["你好"])
print(lang.get("你好"))
print(lang.get("你好嗎","不在字典內"))
#新增資料
lang['學生']="Student"
print(lang)
#刪除資料
del lang['學生']
print(lang)
#清空字典
lang.clear()
print(lang)