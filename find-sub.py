a1=input().strip()
a2=input().strip()
count=0
for i in range(0,len(a1)+1,len(a2)):
    if a1[i:i+len(a2)] == a2:
        count += 1
print(count)
