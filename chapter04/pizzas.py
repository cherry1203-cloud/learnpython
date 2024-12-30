"""
4-1 比萨 ：想出至少三种你喜欢的比萨，将其名称存储在一个列表中，再使用for 循环将每种比萨的名称都打印出来。
修改这个for 循环，使其打印包含比萨名称的句子，而不仅仅是比萨的名称。对于每种比萨，都显示一行输出，如“I like pepperoni pizza”。
在程序末尾添加一行代码，它不在for 循环中，指出你有多喜欢比萨。输出应包含针对每种比萨的消息，还有一个总结性句子，如“I really love pizza!”。
"""

"""
4-2 动物动物 ：想出至少三种有共同特征的动物，将这些动物的名称存储在一个列表中，再使用for 循环将每种动物的名称都打印出来。
修改这个程序，使其针对每种动物都打印一个句子，如“A dog would make a great pet”。
在程序末尾添加一行代码，指出这些动物的共同之处，如打印诸如“Any of these animals would make a great pet!”这样的句子。

"""
"""
4-10 切片切片 ：选择你在本章编写的一个程序，在末尾添加几行代码，以完成如下任务。
打印消息“The first three items in the list are:”，再使用切片来打印列表的前三个元素。
打印消息“Three items from the middle of the list are:”，再使用切片来打印列表中间的三个元素。
打印消息“The last three items in the list are:”，再使用切片来打印列表末尾的三个元素。
"""
my_foods = ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
print("The first three items in the list are:"+str(my_foods[:3]))
print("Three items from the middle of the list are:"+str(my_foods[1:4]))
print("The last three items in the list are:"+str(my_foods[-3:]))

"""

4-11 你的比萨和我的比萨你的比萨和我的比萨 ：在你为完成练习4-1而编写的程序中，创建比萨列表的副本，并将其存储到变量friend_pizzas 中，再完成如下任务。
在原来的比萨列表中添加一种比萨。
在列表friend_pizzas 中添加另一种比萨。
核实你有两个不同的列表。为此，打印消息“My favorite pizzas are:”，再使用一个for 循环来打印第一个列表；打印消息“My friend's favorite pizzas are:”，再使用一
个for 循环来打印第二个列表。核实新增的比萨被添加到了正确的列表中。
4-12 使用多个循环使用多个循环 ：在本节中，为节省篇幅，程序foods.py的每个版本都没有使用for 循环来打印列表。请选择一个版本的foods.py，在其中编写两个for 循环，将各
个食品列表都打印出来。
"""