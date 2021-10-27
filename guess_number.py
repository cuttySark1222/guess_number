import random

answer = random.randint(1, 100)
user_try = 0

while True:
	guess = input("请猜一个数字（1~100）： ")
	guess = int(guess)
	user_try += 1
	if guess == answer:
		print("恭喜你，你猜对了！")
		print(f'你一共猜了{user_try}次!')
		break
	elif guess > answer:
		print("不对，答案要比你猜的小！")
	elif guess < answer:
		print("不对，答案要比你猜的大！")