class Women:

    def __init__(self, name):

        self.name = name
        self.__age = 18

    def __secret(self):
        # 在对象的方法内部，是可以访问对象的私有属性的
        print("%s 的年龄是 %d" % (self.name, self.__age))


xiaofang = Women("小芳")

'''
Python 中，并没有 真正意义 的 私有
在给 属性、方法 命名时，实际是对 名称 做了一些特殊处理，使得外界无法访问到
处理方式：在 名称 前面加上 _类名 => _类名__名称
'''
# 伪私有属性，在外界不能够被直接访问(加上 _类名就可以访问了)
print(xiaofang._Women__age)
# 伪私有方法，同样不允许在外界直接访问(加上 _类名就可以访问了)
xiaofang._Women__secret()
