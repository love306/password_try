password = '123456'
x = 3
while True:	
	key = input('請輸入密碼 ')
	if key == password:
		print('不行啦你作弊啦')
		break
	else:		
		x = x - 1		
		print('剩下', x, '次機會')
		if x == 1:
			break
		

