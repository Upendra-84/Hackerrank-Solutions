X,Y = map(int,input().split())
for i in range(1, X, 2): 
    print((str('.|.')*i ).center(Y, '-'))
print(str('WELCOME').center(Y, '-'))
for i in range(X-2, -1, -2): 
    print(( str('.|.')*i ).center(Y, '-'))
