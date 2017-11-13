# 循环导入

# == 和 is 不一样...

0b1010	bin()
0o1234	oct()
0x2332	hex()

# 私有化
class Test(object):
	def _init_(self):
		'''这就是私有化，两个短下划线'''
		self.__num = 100
t = Test()
t.num = 200
print(t.num)

1. xx 		公有变量
2. _x  		无法被导入到其他的模块内，只能import moudle整体导入。
3. __xx 	私有属性，也无法被导入（名字重整_class__object）
4. __xx__	内置的，名字空间
5.xx_ 		避免和python关键词冲突

# property	
class Test:
	def __init__(self):
		self.__num = 100

	def setNum(self, num):
		self.__num = num

	def getNum(self):
		return self.__num

	num = property(setNum, getNum)

t = Test()
t.num = 100
print(t.num)

class Test:
	def __init__(self):
		self.__num = 100
	# 下面两个函数名字是一样的，这个名字可以直接用
	@property
	def money(self):
		return self.__num
	@money.setter
	def money(self, newNum):
		self.__name = newNum

for a in "abc":
	print(a)



# 需要一个特别大的列表，但是不用现在生成。。
# 生成器
# 保存的是计算每一个元素的方式。。

1. t = (x * x for x in range(10))

# yield出现，函数不会执行。。。
2.	def creatNum():
		a, b = 0, 1
		for i in range(5):
			yield b
			a, b = b, a+b
	creatNum()