"""
    在python中，定义变量时是不需要指定变量类型的
    在运行的时候，python解释器，会根据赋值语句等号右侧的数据自动推导出数据类型
    2.2 数据类型可以分为数字型和非数字行
        -数字型
            整形 int
            浮点型 float
            布尔型 bool
                真 True 非0数
                假 False 0
            复数型
                主要用于科学计算
        非数字型
            字符串
            列表
            元组
            字典
    type()查看变量类型
    2.3 不同类型之间变量的计算
        1.数字类型变量之间可以直接计算
            在python中，两个数字类型变量是可以直接进行算数运算
            True 对应 1
            False 对应 0
        2.字符串变量之间使用+拼接字符串
            在Python中，字符串之间可以使用 + 拼接生成新的字符串
        3.字符串变量可以和整数使用 * 重复拼接生成新的字符串
        4.数字型变量和字符串之间不能进行其他计算
    2.4 变量的输入
        1.input()函数
            用户输入的任何内容Python都认为是字符串
            input("提示信息")
        2.类型转换函数
            int(x) 将x转换为一个整数
            float(x) 将x转换为浮点数
"""
name = "小明"
age = 18
gender = "男"
weight = 75.5
print(type(weight))
print(name)
i = 10
b = True
f = 10.4
print(i+b)
print(i+f)
first = "吕"
second = "厚均"
name = first + second
print(name)
repeat = first * 5
print(repeat)
print((first + second) * 5)
# a = input("请输入：")
# print(a)
# print(type(a))
b = type(int("123"))
print(b)
