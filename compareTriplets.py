str1 = input()
a = list(map(int, str1.split()))
str2 = input()
b = list(map(int, str2.split()))
f = [0,0]
for i in range(3):
	if a[i] > b[i]:
		f[0] = f[0]+1
		continue
	elif a[i] < b[i]:
		f[1] = f[1]+1
		continue
	else:
		f[0] = f[0]
		f[1] = f [1]
		continue	
print(f)
