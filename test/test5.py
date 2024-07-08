"""类继承初始化方法的一些技巧"""


class BaseUser:
    # 类变量
    name = "base user"
    age = 18

    # 实例变量
    def __init__(self):
        print(">>>>>base user")

    def print_user_info(self):
        print(self.name)


class User(BaseUser):
    name = "hou"
    age = 18

    def __init__(self):
        #! 如果子类有初始化方法，此时也想要父类执行初始化方法，必须手动调用
        # super(User, self).__init__()
        # 否则不会执行父类的构造方法
        pass


# user = User()
# user.print_user_info()
# hou


# 子类不写初始化方法会调用父类的初始化方法
class User2(BaseUser):
    name = "hou2"
    age = 18

    def print_user_info(self):
        print(">>>>>重写基类方法")
        print(self.name)


# user2 = User2()
# user2.print_user_info()
# >>>>>base user
# hou2


class BaseUser2:
    # 类变量
    name = "base user"
    age = 18

    # 实例变量
    def __init__(self):
        print(">>>>>base user")
        self.print_user_info()

    def print_user_info(self):
        print(self.name)


#! 重写父类的某一个方法
class User3(BaseUser2):
    name = "hou3"
    age = 18

    def print_user_info(self):
        print(">>>>>重写基类方法")
        print(self.name)


# 父类中初始化方法会调用子类重写的print_user_info方法
user3 = User3()
# >>>>>base user
# >>>>>重写基类方法
# hou3
