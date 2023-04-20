"""
    完整语法
        for 变量 in 集合:
            循环体
        else:
            没用通过break退出循环，循环结束后，会执行的代码
    应用场景
        - 在迭代遍历嵌套的数据类型时，例如一个列表包含多个字典
        - 需求：要判断某一个字典中是否存在指定的值
            - 如果存在，提示并退出循环
            - 如果不存在，在循环整体结束后，希望得到一个统一的提示
"""
warriors = [{"name": "klay",
             "age": 18,
             "weight": 180,
             "height": 190},
            {"name": "curry",
             "age": 19,
             "weight": 200,
             "height": 210}
            ]
no1 = "green"
for player_list in warriors:
    print(player_list)
    if player_list["name"] == no1:
        print("找到了 %s" % no1)
        break
else:
    print("抱歉没有找到 %s" % no1)
print("循环结束")
