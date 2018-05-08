n=input("enter number of testcases: ")
for i in range(n):
    l=input("enter size of array: ")
    a = [int(x) for x in raw_input().split(' ')]
    print l
    if l%2 == 0:
        m= a[l/2-1]+a[l/2]
    else:
        m= a[l/2]
    print m
    elem = [i for i, x in enumerate(a) if x == 0]
    print elem
    if len(elem) > 0:
        p=0
        for j in elem:
            p+=1
            a.insert(j+,m)

    print a
