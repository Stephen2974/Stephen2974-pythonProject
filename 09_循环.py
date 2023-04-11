"""
    顺序：从上向下，顺序执行代码
    分支：根据条件判断，决定执行代码的分支
    循环：让特定代码重复执行
    while循环
        - while 条件(判断 计数器 是否达到 目标次数)：
            条件满足时，做的事情1
            .....
            处理条件(计数器+1)
    死循环
        忘记修改循环的判断条件
    赋值运算符
        =
        +=
        —=
        *=
        /=
        //=     取整除赋值运算符
        %=      取余数赋值运算符
        **=     幂赋值运算符
    break
        某条件满足时，退出循环，不再执行后续重复的代码
    continue
        某条件满足时，不执行后续重复的代码
    while循环嵌套
    如果不希望末尾增加换行，可以在print函数输出内容后增加 , end=""
"""
i = 1
while i <= 5:
    print("dou dou")
    i += 1
print("it's over")
j = 0
k = 0
while j <= 100:
    k += j
    j += 1
print("%d" % k)
m = 0
result = 0
while m <= 100:
    if m % 2 == 0:
        result += m
    m += 1
print("%d" % result)
i = 0
while i < 10:
    if i == 3:
        i += 1
        break
    print(i)
    i += 1
row = 1
while row <= 5:
    print("*" * row, end="---\n")
    row += 1
# for i in range(1,10):
#     for j in range(1,i+1):

# for i in range(1,10):
#     for j in range(1,i+1):

