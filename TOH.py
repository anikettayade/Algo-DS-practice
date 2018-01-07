def toh(n):
	a = []
	b = []
	c = []
	x = []
	for i in range(n,0,-1):
		a.append(i)
	#print a
	cnt = 0
	while 1:
		if n%2 == 0:
			if len(c)<n and len(b)<n:
				move(a,c)
				print ("a=",a ,"c=",c)
			if len(c)<n and len(b)<n:
				move(a,b)
				print ("a=",a ,"b=",b)
		else:
			if len(c)<n and len(b)<n:
				move(a,b)
				print ("a=",a ,"b=",b)
			if len(c)<n and len(b)<n:
				move(a,c)
				print ("a=",a ,"c=",c)
		if len(c)<n and len(b)<n:
			move(b,c)
			print ("b=",b ,"c=",c)
		if len(b)==n:
			break
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
	
