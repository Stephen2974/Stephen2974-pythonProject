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
name = "黑马程序员"
