# class Person():
# 	def __init__(self, newName, newAge):
# 		self.name = newName
# 		self.age = newAge

# def run(self):
# 	print("---%s正在跑---" %self.name)

# lw = Person('laowang', 100)
# print(lw.name)
# print(lw.age)

# Person.num = 100
# print(lw.num)

# lw.run = run
# lw.run(lw)

# types.MethodType(run, lw)

# class test():
# 	#类变量
# 	num = 0 

# 	# 实例方法
# 	def __init__(self):	
# 		self.name = 'test'

# 	# 类方法
# 	@classmethod
# 	def add_num(cls):
# 		cls.num = 100

# 	# 静态方法，可以没有参数
# 	@staticmethod
# 	def print_menu():
# 		print("111111")
# 		print("111111")
# 		print("111111")
# # game = test()
# # game.add_num()
# # print(test.num)
# test.add_num()
# print(test.num)

# 限制添加属性
# __slots__ = ("name", "age")

class test001(object):
	__slots__ = ("name", "test")

ccc = test001()
ccc.name = 10
ccc.age = 100

print(ccc.name)
print(ccc.age)