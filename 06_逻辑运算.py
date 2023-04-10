"""
    py中的逻辑运算符包括：与and/或or/非not三种
    1.and
        - 两个条件同时满足返回True
        - 只要有一个条件不满足返回False
    2.or
        - 两个条件只要有一个条件成立，返回True
        - 两个条件不满足，返回False
    3.not
        - 对条件取反
        - 真就是假，假就是真
    4.elif
        - 如果希望再增加一些条件，条件不同，需要执行的代码也不同时，就可以使用elif
        - 必须与if联合使用
"""
age = int(input("请输入你的年龄："))
is_employee = False
if not is_employee:
    print("not")
if 18 <= age <= 30:
    print("OK")
print("ANYWAY")
holiday_name = "平安夜"
if holiday_name == "情人节":
    print("OK")
    print("LOVE")
elif holiday_name == "平安夜":
    print("APPLE")
else:
    print("EVERYDAY")
