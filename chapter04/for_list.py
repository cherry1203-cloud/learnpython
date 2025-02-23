"""
4-3 数到数到20 ：使用一个for 循环打印数字1~20（含）。
"""
for value in range(1,21):
    print(value)
"""
4-4 一百万 ：创建一个列表，其中包含数字1~1 000 000，再使用一个for 循环将这些数字打印出来（如果输出的时间太长，按Ctrl + C停止输出，或关闭输出窗口）。
"""
# numbers = list(range(1,1000001))
# for number in numbers:
#     print(number)
"""
4-5 计算计算1~1 000 000的总和的总和 ：创建一个列表，其中包含数字1~1 000 000，再使用min() 和max() 核实该列表确实是从1开始，到1 000 000结束的。另外，对这个列表
调用函数sum() ，看看Python将一百万个数字相加需要多长时间。
"""
numbers = list(range(1,1000001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
"""
4-6 奇数 ：通过给函数range() 指定第三个参数来创建一个列表，其中包含1~20的奇数；再使用一个for 循环将这些数字都打印出来。
"""
numbers = list(range(1,20,2))
for num in numbers:
    print(num)
"""
4-7 3的倍数的倍数 ：创建一个列表，其中包含3~30内能被3整除的数字；再使用一个for 循环将这个列表中的数字都打印出来。
"""

"""
4-8 立方立方 ：将同一个数字乘三次称为立方。例如，在Python中，2的立方用2**3 表示。请创建一个列表，其中包含前10个整数（即1~10）的立方，再使用一个for 循
环将这些立方数都打印出来。
4-9 立方解析立方解析 ：使用列表解析生成一个列表，其中包含前10个整数的立方。

"""
numbers = [value**2 for value in range(1,11)]
print(numbers)