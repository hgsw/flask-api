class Scope:
    def add(self, other):
        self.allow_api = self.allow_api + other.allow_api
        return self


class AdminScope(Scope):
    allow_api = ["v1.super_get_user"]

    def __init__(self):
        self.add(UserScope())


class UserScope(Scope):
    allow_api = ["a_user", "b.user"]


class SuperScope(Scope):
    allow_api = ["v1.super_get"]

    def __init__(self):
        self.add(UserScope()).add(AdminScope())


def is_in_scope(scope, endpoint):
    class_scope = globals().get(scope)
    scope = class_scope()
    if scope:
        if endpoint in scope.allow_api:
            return True
    return False


s = SuperScope()
print(s.allow_api)
# ['v1.super_get', 'a_user', 'b.user', 'v1.super_get_user', 'a_user', 'b.user']
