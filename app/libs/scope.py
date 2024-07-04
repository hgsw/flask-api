class AdminScope:
    allow_api = ["v1.super_get_user"]


class UserScope:
    allow_api = []


def is_in_scope(scope, endpoint):
    class_scope = globals().get(scope)
    scope = class_scope()
    if scope:
        if endpoint in scope.allow_api:
            return True
    return False
