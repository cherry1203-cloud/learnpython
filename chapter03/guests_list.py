"""
3-4 嘉宾名单嘉宾名单 ：如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的），你会邀请哪些人？请创建一个列表，其中包含至少3个你想邀请的人；然后，使用
这个列表打印消息，邀请这些人来与你共进晚餐。
"""
guests_list = ['Mary','Chenming','David','WangQin','Lilu']
message = "invite " + guests_list[0] + " to dinner!"
print(message)
message = "invite " + guests_list[1] + " to dinner!"
print(message)
message = "invite " + guests_list[2] + " to dinner!"
print(message)
message = "invite " + guests_list[3] + " to dinner!"
print(message)
message = "invite " + guests_list[4] + " to dinner!"
print(message)
"""
3-5 修改嘉宾名单修改嘉宾名单 ：你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。
以完成练习3-4时编写的程序为基础，在程序末尾添加一条print 语句，指出哪位嘉宾无法赴约。
修改嘉宾名单，将无法赴约的嘉宾的姓名替换为新邀请的嘉宾的姓名。
再次打印一系列消息，向名单中的每位嘉宾发出邀请。
"""
print(guests_list[2] +" have no time. ")
guests_list[2] = 'Alex'
message = "invite " + guests_list[0] + " to dinner!"
print(message)
message = "invite " + guests_list[1] + " to dinner!"
print(message)
message = "invite " + guests_list[2] + " to dinner!"
print(message)
message = "invite " + guests_list[3] + " to dinner!"
print(message)
message = "invite " + guests_list[4] + " to dinner!"
print(message)

"""
3-6 添加嘉宾添加嘉宾 ：你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾。
以完成练习3-4或练习3-5时编写的程序为基础，在程序末尾添加一条print 语句，指出你找到了一个更大的餐桌。
使用insert() 将一位新嘉宾添加到名单开头。
使用insert() 将另一位新嘉宾添加到名单中间。
使用append() 将最后一位新嘉宾添加到名单末尾。
打印一系列消息，向名单中的每位嘉宾发出邀请。
"""
print("I found a bigger table!")
guests_list.insert(0,'Lily')
guests_list.insert(3,'HuMing')
guests_list.append('Zhaoqian')
print(guests_list)
message = "invite " + guests_list[0] + " to dinner!"
print(message)
message = "invite " + guests_list[1] + " to dinner!"
print(message)
message = "invite " + guests_list[2] + " to dinner!"
print(message)
message = "invite " + guests_list[3] + " to dinner!"
print(message)
message = "invite " + guests_list[4] + " to dinner!"
print(message)
message = "invite " + guests_list[5] + " to dinner!"
print(message)
message = "invite " + guests_list[6] + " to dinner!"
print(message)
message = "invite " + guests_list[7] + " to dinner!"
print(message)
"""
3-7 缩减名单缩减名单 ：你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。
以完成练习3-6时编写的程序为基础，在程序末尾添加一行代码，打印一条你只能邀请两位嘉宾共进晚餐的消息。
使用pop() 不断地删除名单中的嘉宾，直到只有两位嘉宾为止。每次从名单中弹出一位嘉宾时，都打印一条消息，让该嘉宾知悉你很抱歉，无法邀请他来共进
晚餐。
对于余下的两位嘉宾中的每一位，都打印一条消息，指出他依然在受邀人之列。
使用del 将最后两位嘉宾从名单中删除，让名单变成空的。打印该名单，核实程序结束时名单确实是空的。
"""
print('Because the table cannot arrives on time, so I only invite 2 guests')
guest = guests_list.pop()
print(guest + ", I'm sorry that i cannot invite you to have dinner together. ")
guest = guests_list.pop()
print(guest + ", I'm sorry that i cannot invite you to have dinner together. ")
guest = guests_list.pop()
print(guest + ", I'm sorry that i cannot invite you to have dinner together. ")
guest = guests_list.pop()
print(guest + ", I'm sorry that i cannot invite you to have dinner together. ")
guest = guests_list.pop()
print(guest + ", I'm sorry that i cannot invite you to have dinner together. ")
guest = guests_list.pop()
print(guest + ", I'm sorry that i cannot invite you to have dinner together. ")
print(guests_list[0] + ", I hope you can have dinner with me. ")
print(guests_list[1] + ", I hope you can have dinner with me. ")
del guests_list[0]
del guests_list[1]
print(guests_list)