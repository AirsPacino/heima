print("this is a test line")

print("this is a test line")
print("this is a test line")
print("this is a test line")
print("this is a test line")
print("this is a test line")
print("this is a test line")
print("this is a test line")
print("this is a test line")
print("this is a test line")

# 新式类 横向。。
class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass

def Test(object):
    def __init__(self):
        pass

    """当在类和对象的__dict__()方法中都没有找到所请求的属性时，就会调用这个函数"""
    def __getattr__(self):
        pass

    """定义了查找属性的行为，就是.的行为==> Test().test ==>只要有.操作，就会执行这个方法"""
    def __getattribute__(self):
        pass
