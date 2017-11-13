# 装饰器
# 如虎添翼
# def outFunc(func):
# 	def innerFunc():
# 		func()
# 	return innerFunc

# # f1 = outFunc(f1)
# @outFunc
# def f1():
# 	print("---f1---")

# @outFunc
# def f2():
# 	print("---f2---")

# f2()

def makeBold(func):
	print("正在装饰makebold...")
	def wrapper():
		print('正在执行makebold')
		return "<b>" + func() + "</b>"
	return wrapper

def makeItalic(func):
	print("正在装饰makeItalic")
	def wrapper():
		print('正在执行makeItalic')
		return "<i>" + func() + "</i>"
	return wrapper

@makeBold
@makeItalic
def test():  
	print('正在执行test')
	return "Facing the sea"

ret = test()
print(ret)