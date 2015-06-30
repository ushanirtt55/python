def pattern(rows):
    if rows<=0:
        print ""
    else:
        for i in range (rows,0,-1):
            print ' '*(i-1) + (''.join(map(str,range(1,rows+1))))
        return
                  
pattern(5)

