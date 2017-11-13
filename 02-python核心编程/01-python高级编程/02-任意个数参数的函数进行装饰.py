# 对任意个数参数的函数进行装饰

# def func(func):
# 	def wrapper(*argv, **kw):
# 		func(*argv, **kw)
# 	return wrapper

# @func
# def test(a, b, c, d):	# 这里参数个数还是要手动改的，装饰器的就不用动了，可以传任意参数
# 	print("a=%d, b=%d, c=%d, d=%d" %(a, b, c, d))

# test(11, 22, 33, 44)

# 带有参数的装饰器
# @func("hahh")
# 在原有装饰器的基础上，设置外部变量

def func_arg(pre="hello"):
	def func(fun):
		def wrapper(*argv, **kw):
			if pre == 'haha':
				print("this is haha")
				print("pre=%s" %pre)
				fun(*argv, **kw)
			else:
				print("this is no haha")
				print("pre=%s" %pre)
				fun(*argv, **kw)
		return wrapper
	return func

@func_arg("haha") #这里就相当于@func,即func_ard("haha")=func
def test():
	print("1111")

@func_arg("lala")
def test2():
	print("2222")

test()
test2()