"""
3-8 放眼世界放眼世界 ：想出至少5个你渴望去旅游的地方。
将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的。
按原始排列顺序打印该列表。不要考虑输出是否整洁的问题，只管打印原始Python列表。
使用sorted() 按字母顺序打印这个列表，同时不要修改它。
再次打印该列表，核实排列顺序未变。
使用sorted() 按与字母顺序相反的顺序打印这个列表，同时不要修改它。
再次打印该列表，核实排列顺序未变。
使用reverse() 修改列表元素的排列顺序。打印该列表，核实排列顺序确实变了。
使用reverse() 再次修改列表元素的排列顺序。打印该列表，核实已恢复到原来的排列顺序。
使用sort() 修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了。
使用sort() 修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了。

"""
travel_list = ['Hongkong','Iceland','England','Korea','America']
print(travel_list)
print(sorted(travel_list))
print(travel_list)
print(sorted(travel_list,reverse=True))
print(travel_list)
travel_list.reverse()
print(travel_list)
travel_list.reverse()
print(travel_list)
travel_list.sort()
print(travel_list)
travel_list.sort(reverse=True)
print(travel_list)

"""
3-9 晚餐嘉宾晚餐嘉宾 ：在完成练习3-4~练习3-7时编写的程序之一中，使用len() 打印一条消息，指出你邀请了多少位嘉宾来与你共进晚餐。
"""
guests_list = ['Mary','Chenming','David','WangQin','Lilu']
print("邀请了" + str(len(guests_list)) +"位嘉宾与我共进晚餐。" )
"""
3-10 尝试使用各个函数 ：想想可存储到列表中的东西，如山岳、河流、国家、城市、语言或你喜欢的任何东西。编写一个程序，在其中创建一个包含这些元素的列
表，然后，对于本章介绍的每个函数，都至少使用一次来处理这个列表。
"""

city_list = ['Shanghai','Beijing','Shenzhen','Hongkong','Wuhan']
city_list.append('Hangzhou')
print(city_list)
city_list.remove('Hongkong')
print(city_list)
del city_list[0]


