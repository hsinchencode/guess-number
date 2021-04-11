import random
r = random.randint(1, 100)

while True:
	figure = input('猜猜是什麼數字？')
	figure = int(figure)
	if figure == r:
		print('終於猜對了')
		break
	elif figure > r:
		print('比答案大')
	else:
		print('比答案小')

