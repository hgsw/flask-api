class Scope:
    allow_module = []
    allow_api = []
    forbidden = []

    def __add__(self, other):
        self.allow_api = self.allow_api + other.allow_api
        self.allow_api = list(set(self.allow_api))

        self.allow_module = self.allow_module + other.allow_module
        self.allow_module = list(set(self.allow_module))

        self.forbidden = self.forbidden + other.forbidden
        self.forbidden = list(set(self.forbidden))

        return self


class AdminScope(Scope):
    # allow_api = ["v1.user+super_get_user", "v1.user+super_delete_user"]
    allow_module = ["v1.user"]

    def __init__(self):
        # allow_api方式访问，需要加上其他可访问的视图函数
        # self + UserScope()

        # 访问整个视图函数文件
        pass


class UserScope(Scope):
    # allow_api = ["v1.user+get_user", "v1.user+delete_user"]
    # 100个视图函数，只有两个不能访问，反向操作
    forbidden = ["v1.user+super_get_user", "v1.user+super_delete_user"]

    def __init__(self):
        # allow_api方式访问，需要加上其他可访问的视图函数
        self + AdminScope()


def is_in_scope(scope, endpoint):
    # 默认是蓝图.视图函数名，如v1.super_get_user
    # 自定义endpoint 蓝图.view_func => 蓝图.module_name+view_func
    # blueprint.redprint+view_func
    class_scope = globals().get(scope)
    scope = class_scope()
    module_name = endpoint.split("+")
    # 禁止访问的视图函数集
    if endpoint in scope.forbidden:
        return False

    # 允许访问单个视图函数
    if endpoint in scope.allow_api:
        return True

    # 允许访问整个视图函数文件
    if module_name[0] in scope.allow_module:
        return True

    return False


# s = AdminScope()
# print(s.allow_api)
# print(s.allow_module)
# ['v1.super_get', 'a_user', 'b.user', 'v1.super_get_user', 'a_user', 'b.user']
