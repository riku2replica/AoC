import math
str = "3267: 81 40 27" 
# your code goes here

a = []
a1 = 0
b1 = []
postComb = []
ttlVal = 0
vMul = 0
vAdd = 0

def mul(x, y):
	return int(x) * int(y)
def add(x, y):
	return int(x) + int(y)
def attest(yList):
	print(yList)
	return ''
def genRng(x,y):
	for xx in x:
		print(xx)
	print(y)

def testA(x, y):
	#to test around
	#print(x)
	#print(y)
	for yy in y:
		#print(yy)
		try:
			iY = int(yy)
		except:
			iY = 0
		if iY != 0:
			postComb.append(iY)
	#print(postComb)
	#print(len(postComb))
	
	#types of combination
	#Maybe 2^2 how many slot multiply variation
	#a+b+c
	#a+b*c
	#a*b+c
	#a*b*c
	cmbtion = int(math.pow(2, len(postComb)-1))
	#print(cmbtion)
	#for a in range(cmbtion):
	genRng(postComb, cmbtion)


	#if x < mul(y[2],mul(y[0],y[1])):
		#print('False')
	#else:
		#print('Something')
		

a = str.split(":")
a1 = int(a[0])
b = a[1]
b1 = b.split(' ')
#c1 = int(a[0])
#print(len(b1))
i = 0
#for i in range(len(b1))
#vMul = len(b1) - 1
testA(a1, b1)