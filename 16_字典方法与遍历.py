"""
    字典的方法
        - 字典.keys()
            所有key列表
        - 字典.values()
            所有value列表
        - 字典.items()
            所有(key.value)元组列表
        - 字典[key]
            可以从字典中取值，key不存在会报错
        - del 字典[key]
            删除指定键值对，key不存在会报错
        - 字典.pop(key)
            删除指定键值对，key不存在会报错
        - 字典.popitem()
            随即删除一个键值对
        - 字典.clear()
            清空字典
        - 字典[key] = value
            如果key存在，不会修改数据
            如果key不存在，新建键值对
        - 字典.setdefault(key,value)
            如果key存在，不会修改数据
            如果key不存在，新建键值对
        - 字典.update(字典二)
            将字典二的数据合并到字典一
"""
warriors_dict = {"name": "curry",
                 "champion": 4
                 }
for k in warriors_dict:
    print("%s - %s" % (k, warriors_dict[k]))

