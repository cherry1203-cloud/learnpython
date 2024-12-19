"""
将用户的姓名存到一个变量中，并向该用户显示一条消息。
显示的消息应非常简单，如“Hello Eric, would you like to learn some Python today?”
"""

name = "Eric"
print("Hello " + name +", would you like to learn some Python today?")

"""
将一个人名存储到一个变量中，再以小写、大写和首字母大写的方式显示这个人名。
"""
name = "Eric"
print(name.lower())
print(name.upper())
print(name.title())

"""
找一句你钦佩的名人说的名言，将这个名人的姓名和他的名言打印出来。输出应类似于下面这样（包括引号）：
Albert Einstein once said, “A person who never made a mistake never tried anything new.”
"""
print('Albert Einstein once said, “A person who never made a mistake never tried anything new.”')
"""
重复练习2-5，但将名人的姓名存储在变量famous_person 中，再创建要显示的消息，并将其存储在变量message 中，然后打印这条消息。
"""
famous_person = "Albert Einstein"
message = famous_person+" "+'once said, “A person who never made a mistake never tried anything new.”'
print(message)

"""
剔除人名中的空白： 
存储一个人名，并在其开头和末尾都包含一些空白字符。务必至少使用字符组合"\t" 和"\n" 各一次。
打印这个人名，以显示其开头和末尾的空白。然后，分别使用剔除函数lstrip() 、rstrip() 和strip() 对人名进行处理，并将结果打印出来。
"""
name = "\t Jim \nGreen "
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())