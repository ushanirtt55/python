def yrange(n):
    i = 0
    while i < n:
        print "Before yield", i
        yield i
        print "After yield", i
        i += 1
        

for i in yrange(8):
    print i
