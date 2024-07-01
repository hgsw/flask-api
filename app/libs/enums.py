from enum import Enum


class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    USER_MINA = 200
    USER_WX = 201

# 测试枚举
# data = ClientTypeEnum.USER_EMAIL
# print(type(data))
# client = ClientTypeEnum(100)
# print(type(client))
# print(client.name)