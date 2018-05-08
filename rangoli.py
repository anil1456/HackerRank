n=input()
b=n+96
for j in range(1,n):
    print((2*j-1)*'-{}'.format(chr(b)) )
for k in range(n,0,-1):
    z=(2*k-1)
    print("{0:{z}r}".format(chr(b)) )

    #print('-'*(2*n-1))
