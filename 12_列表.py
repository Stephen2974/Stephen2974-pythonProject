"""
    列表的定义
        - list时py中使用最频繁的数据类型，在其它语言中通常叫做数组
        - 专门用于存储一串信息
        - 列表用[]定义，数据之间用 , 分隔
        - 列表索引从0开始
        - 从列表中取值时，如果超出索引范围，程序会报错
    列表方法
        - 增加
            - 列表.insert(索引，数据)       在指定位置插入数据
            - 列表.append(数据)            在末尾追加数据
            - 列表.extend(列表2)           将列表2的数据追加到列表
        - 修改
            - 列表[索引] = 数据             修改指定索引的数据
        - 删除
            - del.列表[索引]                删除指定缩影的数据
            - 列表.remove[数据]             删除第一个出现的指定数据
            - 列表.pop                     删除末尾数据
            - 列表.clear                   清空列表
        - 统计
            - len(列表)                    列表长度
            - 列表.count(数据)              数据在列表中出现的次数
        - 排序
            - 列表.sort()                     升序排序
            - 列表.sort(reserve=True)         降序排序
            - 列表.reverse                    逆序、反转
        - 取索引
            - 列表.index(数据)                 获取元素位置
<<<<<<< HEAD
    关键字、函数和方法
        - 关键字是Py内置的、具有特殊意义的标识符、关键字后面不需要括号 del
        - 一共三十三个关键字
            - ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
        - 函数封装了独立的功能，可以直接调用
        - 方法和函数类似，同样是封装了独立的功能
        - 方法需要通过对象来调用，表示针对这个对象要做的操作
=======

>>>>>>> origin/master
"""
name_list = ["curry", "green", "klay"]
name_list1 = ["james", "durant"]
print(name_list[0])
print(name_list.index("curry"))
name_list.insert(1, "looney")
print(name_list)
name_list.append("pool")
print(name_list)
name_list.extend(name_list1)
print(name_list)
name_list.pop()
print(name_list)
print(len(name_list))
name_list.remove("green")
print(name_list)
del name_list[3]
print(name_list)
name_list.sort()
number_list = [1, 7, 3, 4, 6, 8]
number_list.sort()
print(number_list)
number_list.sort(reverse=True)
print(number_list)


