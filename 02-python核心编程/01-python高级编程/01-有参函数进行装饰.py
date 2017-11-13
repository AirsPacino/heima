# 对有参函数进行装饰
def test(func):
	def wrapper(a, b):
		print("=====1======")
		func(a, b)
	return wrapper

@test
def test1(a, b):
	print("a=%d, b=%d" %(a, b))

test1(2, 3)


# 可变参数
number = [1, 2, 3]
def calc(*number):
	pass

def person(name, age, **kw):
	print('name', name, 'age', age, 'other', kw)

# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
def person(name, age, *, city, job) 或者
def person(name, age, *args, city, job)