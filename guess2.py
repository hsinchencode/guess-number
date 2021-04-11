import random
count = 0

start = input('請輸入隨機開始值')
end = input('請輸入隨機結束值')
start = int(start)
end = int(end)

r = random.randint(start, end)


while True:
	count += 1
	figure = input('請輸入數字')
	figure = int(figure)
	if r == figure:
		print('恭喜你答對了')
		print('這是你猜的第', count, '次')
		break
	elif figure > r:
		print('比答案大')
	else:
		print('比答案小')
	print('這是你猜的第', count, '次')


