#Euclid's algorithm
a = int(input('Input any number: '))
b = int(input('Input another number: '))
while b>0 :
	a, b = b, a%b
print('Greatest common divisor is  ' + str(a))