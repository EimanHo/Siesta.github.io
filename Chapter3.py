print("Chapter 3")

QN = ['reiji', 'ranmaru', 'ai', 'camus']
print(QN) #這樣的話它只會照將QN的內容print出來，包括括號

print(QN[0]) #0是指括號內的元素位置，python的索列從0開始
print(QN[1]) #這樣就會將ranmaru print出來
print(QN[2].title()) #會生成帶大寫的ai

message = "My favorite person in Quartet Night is " + QN[0].title() + "."
print(message)

print("修改列表元素")
QN = ['reiji', 'ranmaru', 'ai', 'camus']
print(QN)

QN[1] = 'ran'
print(QN) #修改列表元素
 
print("append命令添加列表元素")
starish = ['oto', 'masa', 'natsu', 'toki', 'syo', 'ren']
print(starish)

starish.append('cecil')
print(starish)

print("動態地創建列表")
QN = [] #可以先創建，然後再一個一個手動加

QN.append('reiji')
QN.append('ran')
print(QN)
QN.append('ai')
QN.append('camus')

print(QN)

print("insert命令插入元素")
QN = ['ran', 'ai', 'camus']
print(QN)

QN.insert(0, 'reiji') #0指的是在第一個位置插入
print(QN)

del QN[2]
print(QN) #這樣就删掉本來在第三位的ai

print("將删除的元素移入另一個列表中")
Lost_alice = ['natsu', 'reiji', 'masa', 'ran']
print(Lost_alice)

Lost_alice_3 = Lost_alice.pop()
print(Lost_alice)
print(Lost_alice_3) #pop輸出的是最後一個元素，所以ran從四人輸出到一人列表中
Lost_alice = ['natsu', 'reiji', 'masa', 'ran']
Lost_alice_3 = Lost_alice.pop(2) #也可以用pop來指定輸出哪一個元素
print(Lost_alice)
print('The one that is not my favorite is ' + Lost_alice_3.title() + '.')

#del和pop最大的區別在於，如果使用了del就不能再使用該元素，但是用pop的話還可以輸出到另一個列表中繼續使用

#如果不知道要删除的值的位置，就直接用remove
print("直接用remove删除元素")
QN = ['reiji', 'ran', 'ai', 'camus']
print (QN)
QN.remove('ran')
print(QN)

QN = ['reiji', 'ran', 'ai', 'camus']
should_not_be_in_there = 'ran'
print("\n" + should_not_be_in_there.title() + " should not be in there.")

print("對列表進行排序（一但排序就是永久性）")
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True) #用reverse可以將排序方向反過來
print(cars)

print("非永久性排序")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

print("reverse永久性將列表反過來輸出")
QN = ['reiji', 'ran', 'ai', 'camus']
print(QN)
QN.reverse()
print(QN)





