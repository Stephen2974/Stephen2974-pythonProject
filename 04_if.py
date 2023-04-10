"""
    if和else语句以及缩进块是一个完整的代码
    if 要判断的条件：
        条件成立语句
    else:
        条件不成立语句
    ...   这个语句无论什么条件都会执行
"""
age = 15
if age >= 18:
    print("it's OK")
print("not ok")
age = int(input("请输入你的年龄"))
if age > 18:
    print("OK")
else:
    print("not OK")
print("anyway")
