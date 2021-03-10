#在符號之間需要有空格
name = "1 quartet night"
print(name.title()) #只有開頭大寫
#.title()用於描述前面的name，"."就是類似於"指代"的意思

name = "2 Quartet Night"
print(name.upper()) #全大寫

name = "3 Quartet Night"
print(name.lower()) #全小寫

first_name = "quartet"
last_name = "night"
full_name = first_name + " " + last_name

print(full_name)

message = ("\n\tHello, " + full_name.title() + "!")
print(message)

#\t是制表符，相等於空白
#\n是換行符

print("\nQuartet Night:\nReiji\nRanmaru\nAi\nCamus")

favorite_language = '\n python '
print(favorite_language)
print(favorite_language.rstrip())
#rstrip, lstrip, strip可以在print的時候將文字旁邊的空格去除
#沒搞懂

#單﹑雙引號
message = "\nRan's favorite fruit is banana."
print(message)
#如果選用單引號的話，python就會因為不知道字符串的結東位置而出現error
#i.e. 'Ran's favorite fruit is banana.'

print("\nChapter 2.4")

age = 23
message = "\nHappy" + str(age) + "rd Birthday!"
print(message) #如果只打23的話，python會因為不知道23應該識別為字符還是數字而出錯

print(" ")
print(7+4)
print(11-4)
print(20/5)
print(2.5*4)
print(10/3)

