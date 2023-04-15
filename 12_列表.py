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

