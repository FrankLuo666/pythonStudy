# coding: utf-8


class Cat:
    def __init__(self, name):
        self.name = name
        print("%s 来了" % self.name)

    def __del__(self):
        print("%s 去了" % self.name)

    def __str__(self):
        # 可以打印对象，必须要返回一个字符串
        return "我是小猫【%s】" % self.name


# 创建猫对象
tom = Cat("tom2")
print(tom)
