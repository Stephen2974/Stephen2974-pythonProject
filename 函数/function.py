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
