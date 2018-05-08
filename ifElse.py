a = int(raw_input())
if a%2!=0:
    print "weird"
else:
    if a>1 and a<=5:
        print "not weird"
    elif a>5 and a<=20:
        print "weird"
    else:
        print "not weird"
