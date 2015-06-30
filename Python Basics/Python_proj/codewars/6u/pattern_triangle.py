def pattern(rows):
    if rows<=0:
        print "Empty"
    for i in range (rows):
        print ' '*(rows-i-1) + str(i)*(2*i+1)        

pattern(5)