# 可以被next()调用，称为迭代器
# lsit, dict, str都是iterable，而不是iterator
# iter(list)可以使列表调用next()函数

	闭包：在函数内部定义一个函数，并且内部函数用到了外部的变量，
那么外部变量和内部函数统称为闭包

def test(number):
	def test_in(number_in):
		print(number + number_in)	# 此处number是上层函数传入的number

	 return test_in

ret = test(100)	#此处ret是test_in函数的引用
# 外部函数不会被销毁
ret(1) # 相当于调用test_in 函数
ret(100)

def test(a, b):
	def test_in(x):
		print(a * x + b)
	return test_in
# 相当于两条直线。。
line1 = test(1, 1)
line2 = test(3, 4)
# 计算出纵坐标的值。。
line1(5)
line2(2) 