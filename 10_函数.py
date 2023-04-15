"""
    def 函数名():
        函数封装的代码
    1.def是英文define的缩写
    2.函数名称应该能够表达函数封装代码的功能
    3.符合标识符的命名规则
        可以由字母、下划线和数字的组成
        不能以数字开头
        不能与关键字重名
    如果不主动调用函数，函数不会主动执行
    不能在函数定义前调用函数
    在函数调用位置，使用快捷键CTRL+Q可以查看函数的说明信息
    参数：
        - 形参：定义函数时，小括号中的参数，是用来就收参数的，在函数内部作为变量使用
        - 实参：调用函数时，小括号中的函数，是用来把数据传递到函数内部用的
    返回值：
        - 在函数中使用return关键字可以返回结果
        - 调用函数一方，可以使用变量来接收函数的返回结果
        - return下方的代码不会被执行
    函数的嵌套调用
        -
"""


def last1():
    print("*" * 50)


def last2():
    print("-" * 50)
    last1()


last2()


def print_line(char, times):
    """

    :param char:分割字符
    :param times:重复的次数
    :return:
    """
    print(char * times)


def print_lines(char, times):
    row = 1
    while row <= 5:
        print_line(char, times)
        row += 1


print_lines("-", 4)
