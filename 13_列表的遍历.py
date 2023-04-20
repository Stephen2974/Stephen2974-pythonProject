"""
    循环遍历
        - 遍历就是从头到尾依次从列表中获取元素
        - 再Py中为了提高列表的遍历效率。专门提供的迭代iteration遍历
            - 使用for循环能够实现迭代遍历
    应用场景
        - 列表存储相同类型的数据
        - 通过迭代遍历，再循环体内部，针对列表中的每一项元素，执行相同的操作
"""
name_list = ["curry", "klay", "green", "looney"]

for name in name_list:
    print("My name is %s" % name)

