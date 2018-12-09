# algorithm Эвклида
a = int(input('Введите люое число '))
b = int(input('Введите второе люое число '))
while b>0 :
	a, b = b, a%b
print('Наибольший общий делитель равен ' + str(a))
