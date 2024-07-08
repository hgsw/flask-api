class MyClass1:
    def __init__(self):
        self.message = "This is MyClass1"


class MyClass2:
    def __init__(self):
        self.message = "This is MyClass2"


def instance_class(class_name):

    class_def = globals().get(class_name)

    if class_def:
        return class_def()
    else:
        raise ValueError(f"Class {class_name} not found.")


# 使用字符动态实例化类
try:
    instance = instance_class("MyClass1")
    print(instance.message)
    # This is MyClass1
except ValueError as e:
    print(e)
