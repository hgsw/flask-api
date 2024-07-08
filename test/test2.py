"""json序列化对象处理
调用类的__dict__函数，类变量不会被转化为dict
必须是实例变量__dict__才会将变量转化dict"""

import json


class UserTest:
    # 类变量
    name = "hou"
    age = 18

    # 实例变量
    def __init__(self):
        self.nickname = "user1"


user = UserTest()

# print(json.dumps(user))
# 直接序列化一个对象是会报错的
# TypeError: Object of type UserTest is not JSON serializable

dct = user.__dict__
print(json.dumps(dct))
# {"nickname": "user1"}


class User:
    name = "hou"
    age = 18

    def __init__(self):
        self.nickname = "user1"

    def keys(self):
        # keys函数可以通过dict(self)返回对象构建字典的key集合
        # 重写keys函数，类的属性也可以通过dict的形式进行访问
        # 返回值必须是一个可迭代的对象
        return ("name", "age", "nickname")

    def __getitem__(self, item):
        # 根据item获取对象属性的值
        return getattr(self, item)


user = User()
print(user.name)  # 对象.属性访问
print(user["name"])  # 字典形式访问
print(user["age"])
print(user["nickname"])

# dict在传入对象实例的时候会尝试构建字典
# 通过对象的keys获取对象的键值，__getitem__获取对象属性的值
dct = dict(user)
print(dct)
# {'name': 'hou', 'age': 18, 'nickname': 'user1'}


# 根据传参自定义dict变量
class User:
    name = "hou"
    age = 18

    def __init__(self):
        self.nickname1 = "user1"
        self.nickname2 = "user2"
        self.nickname3 = "user3"
        self.nickname4 = "user4"
        self.nickname5 = "user5"
        # self.fields = ["name", "age", "nickname1", "nickname2", "nickname3", "nickname4", "nickname5"]
        self.fields = []

    def keys(self):
        return self.fields

    def __getitem__(self, item):
        return getattr(self, item)

    def to_dict(self, *keys):
        for key in keys:
            self.fields.append(key)


user = User()
user.to_dict("nickname1", "nickname3")
dct = dict(user)
print(dct)
# {'nickname1': 'user1', 'nickname3': 'user3'}
