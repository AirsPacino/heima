1.
import time
start_time = time.time()
for a in range(0, 1001):
	for b in range(0, 1001):
		c = 1000 - a - b
		if a**2 + b**2 == c**2:
			print("a=%d, b=%d, c=%d" %(a, b, c))
end_time = time.time()
print("time:%d" %(end_time - start_time))

# 基本运算数量。。
# 的和就是“时间复杂度”
T = 1000 * 1000 * 1000 * 2
a+b+c=N(N是规模)
T = N * N * N * 2

T(n) = n^3 * 2 # 这就是时间复杂度
并不需要分析的太细致。。
So。。。
T(n): N^3 * k
# 大O表示法
g(n) = N^3	# 就是他，N是规模
T(n) = k g(n)

2.
最优时间复杂度	# 最理想情况下。。。
最坏时间复杂度	# 提供了一个保证，一般说的就是这种
平均时间复杂度

	1.基本步骤，只有常数项，即 O(1)
	2.顺序结构	加法
	3.循环结构	乘法
	4.分支结构	取最大值
O(1) < O(logn) < O(n) < O(nlogn) < O(n^2) < O(n^3)
< O(2^n) < O(n!) < O(n^n)

