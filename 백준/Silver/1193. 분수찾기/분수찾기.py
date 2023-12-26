k = int(input())
a = 1
x,y = 0,0
for i in range(10000000):
	if (a + i) > k :
		if i % 2 != 0:
			x += i - (k-a)
			y = 1 + (k-a)
		else:
			x += 1 + (k-a)
			y = i - (k-a)
		break
	a += i
print(str(x) + "/" + str(y))
