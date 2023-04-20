"""
    元组
        - Tuple(元组)与列表相似，不同之处在于元组的元组不能修改
            - 元组表示多个元素组成的序列
            - 元组再Python开发中，有特定的应用场景
        - 用于存储一串 信息、数据之间使用 ，分隔
        - 元组用()定义
        - 元组的索引从0开始
        - 元组中只包含一个元素时，需要在元素后面添加逗号
            - info_tuple = (50, )
        - .count  .index
        - 可以通过for循环遍历元组
            -   但因为元组内数据类型不同，所以遍历并不常见
        - 应用场景
            - 函数的参数和返回值，一个函数可以接受任意多个参数，或者一次返回多个数据
            - 格式化字符，格式化字符串后面的()本质上就是一个元组
            - 让列表不可以被修改，以保护数据安全 tuple(列表)

"""
info_tuple = ("curry", 30, 2974)
print(info_tuple[0])
print(info_tuple.count("curry"))
print(len(info_tuple))
for a in info_tuple:
    print(a)
print("我叫 %s 我的号码是 %d 我投进了 %d 个三分" % info_tuple)
