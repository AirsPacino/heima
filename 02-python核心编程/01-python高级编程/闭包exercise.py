def createLine(a, b):
	'''内部函数不执行'''
	def calYpoint(x):
		print(a * x + b)

	return calYpoint

line1 = createLine(1, 0)
line2 = createLine(3, 4)

line1(2)
line2(5)