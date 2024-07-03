"""json序列化对象处理
"""


class UserTest:
    """调用类的__dict__函数，类变量不会被转化为dict
    必须是实例变量__dict__才会将变量转化dict"""

    name = "hou"
    age = 18

    def __init__(self):
        self.nickname = "user1"


class User:
    name = "hou"
    age = 18

    def __init__(self):
        self.nickname = "user1"

    def keys(self):
        # 通过dict(self)返回对象构建字典的key
        return ("name", "age", "nickname")

    def __getitem__(self, item):
        # 根据item获取对象的值
        return getattr(self, item)


user = User()
print(user["name"])
print(user["age"])
print(user["nickname"])

# dict在传入对象实例的时候会尝试构建字典
# 通过对象的keys获取对象的键值，__getitem__获取对象属性的值
dct = dict(user)
print(dct)
