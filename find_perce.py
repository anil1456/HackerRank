d={}
line=[]
for _ in range(int(input())):
    line = raw_input().split(' ')
    a1, a2 = line[0], line[1:]
    d[a1] = sum(map(float, a2))/3
print()
print( "%.2f", d[input()])
