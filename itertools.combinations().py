from itertools import combinations
[a,b] = input().split()
for i in range(1,int(b)+1):
    for items in combinations(sorted(a),int(i)):
        print(''.join(items))   
