# 这种方式不推荐使用，因为函数重名并没有任何的提示，出现问题不好排查
from hm_01_测试模块1 import *
from hm_02_测试模块2 import *

print(title) #模块2
say_hello()

wangcai = Dog()
print(wangcai)
