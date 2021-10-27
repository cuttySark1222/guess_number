import random

answer = random.randint(1, 100)

while True:
	guess = input("请猜一个数字： ")
	guess = int(guess)
	if guess == answer:
		print("恭喜你，你猜对了！")
		break
	elif guess > answer:
		print("不对，答案要比你猜的小！")
	elif guess < answer:
		print("不对，答案要比你猜的大！")