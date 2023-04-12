def multiple_table():
    row = 1
    while row <= 9:
        col = 1
        while col <= row:
            print('{0}*{1}={2}'.format(row, col, row * col), end="\t")
            col += 1
        row += 1
        print("")


name = "小明"


def say_Hello():
    """打招呼"""
    print("hello1")
    print("hello2")
    print("hello3")


def sum_sum():
    num1 = int(input("数值1："))
    num2 = int(input("数值2："))
    result3 = num1 + num2
    print("%d + %d = %d" % (num1, num2, result3))


def sum_2_sum(num1, num2):
    """对两个数字的求和"""
    result2 = num1 + num2
    print("%d + %d = %d" % (num1, num2, result2))
    return result2


sum_2_sum(50, 21)
result = sum_2_sum(50, 20)


def test1():
    print("*")


def test2():
    print("-")
    test1()


test2()