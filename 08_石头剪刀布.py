"""
    使用随机数，首先需要导入随机数的模块
    import random
    random.randint(a, b),返回[a,b]之间的整数
"""
import random
print("1/石头 2/剪刀 3/布")
player = int(input("请输入"))
computer = random.randint(1, 3)
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("You are win")
elif player == computer:
    print("let's again")
else:
    print("You are lose")
print("电脑：%d/人类：%d" % (computer, player))
