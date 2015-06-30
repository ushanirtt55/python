def pattern(n):
    for i in range(n,0,-1):
        print " "*(n-i) + str(i) + " "*(i) + str(i) + " "*(n-i)

pattern(5)
