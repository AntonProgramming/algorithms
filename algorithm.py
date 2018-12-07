# algorithm Эвклида
a = int(input('Ââåäèòå ëþáîå ÷èñëî '))
b = int(input('Ââåäèòå âòîðîå ëþáîå ÷èñëî '))
while b>0 :
	a, b = b, a%b
print('Íàèáîëüøèé îáùèé äåëèòåëü ðàâåí ' + str(a))
