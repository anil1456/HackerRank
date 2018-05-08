
class Adder(object):
    """docstring forAdder."""
#    def __init__(self, num,lis,div):
#        self.u=num
#        self.n=div
#        self.d = lis
    def convert(self,u,n,d):
        while u>0:
            d.append(u%n)
            u=u/n
        if n == 16:
            for a,b in enumerate(d):
                if b>9 and b<16:
                    d[a]=str(unichr(b+55))
        return ''.join(map(str, d[::-1]))

ele=input("entr input value")

for i in range(1,ele):
    a=Adder()

    print("%4s %4s %4s %4s" %(a.convert(i,2,d=[]), a.convert(i,8,d=[]), a.convert(i,10,d=[]), a.convert(i,16,d=[])) )
