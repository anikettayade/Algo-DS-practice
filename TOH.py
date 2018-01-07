def toh(n):
	a = []
	b = []
	c = []
	x = []
	for i in range(n,0,-1):
		a.append(i)
	print a
	cnt = 0
	while len(b)<n:
		move(a,c)
		move(a,b)
		move(b,c)
	print b

def move(x,y):
	#print x
	#print y
	if len(x)== 0:
		ele = y.pop()
		x.append(ele)
		return
	if len(y)==0:
		ele=x.pop()
		y.append(ele)
		return
	if x[-1] > y[-1]:
		ele=y.pop()
		x.append(ele)
		return
	else:
		ele=x.pop()
		y.append(ele)
		return
n=4
toh(n)
	
