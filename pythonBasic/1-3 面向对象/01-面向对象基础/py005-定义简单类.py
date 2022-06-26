# coding: utf-8


class Cat:
    def __init__(self, name, num=0):
        self.name = name
        self.num = num

    def add(self):
        self.num = self.num + 1

    def eat(self):
        print("%s 爱吃鱼" % self.name)

    def drink(self):
        print("%s 要喝水" % self.name)


# 创建猫对象
tom = Cat("tom2")
tom.eat()
tom.drink()

print(tom)
tom.add()
tom.add()
print(tom.num)
