magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician) #將magicians列表的每一個元素儲存在變量magician中
	print(magician.title() + ',that was a great trick!')
	print("I can't wait to see your next trick," + magician.title() + ".\n")
print("Thank you,everyone. That was a great magic show!")
#只有縮進的內容才是循環的一部份

print("創建數值列表")
for value in range(1,5):
	print(value)
#因為這樣的range並非真正的列表，要輸出數字列表的話需要用list	
numbers = list(range(1,6))
print(numbers)		

print("輸出偶數")
even_numbers = list(range(2,11,2))
print(even_numbers) #這裏指的是從2開始數，一直到11，間隔為2

print("創建一個列表，裏面包含1~10的平方，**代表^")
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
print(squares)

#更簡潔的方法：
squares = []
for value in range(1,11):
	squares.append(value**2)
print(squares)

#將代碼合成一行：
squares = [value**2 for value in range(1,11)]
print(squares)

print("從列表中提取其中幾個元素")
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])#這樣會輸出martina, michael和florence
print(players[2:])#這樣會由第三個元素開始輸出，直到最後
print(players[-2:])#只要最後2個

print("Here are the first three players in the team:")
for player in players[:3]:
	print(player.title())#會一個一個輸出，直到第三個
	
print("用:來複制列表")
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("My friend's favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("My friend's favorite foods are:")
print(friend_foods)

print("元組")
dimensions = (200,50)#用圖括號的就是不能改，range用的是方括號
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
	print(dimension)
	
print("雖然不能直接修改元組，但是可以給予存儲元組的變量賦值")
dimensions = (200, 50)
print("Original dimensions")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("modified dimensions")
for dimension in dimensions:
	print(dimension)#其實就是從新打修改一遍，好坑


