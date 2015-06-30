def pattern(n=5):
    for i in range(n,0,-1):
        print (n-i)* ' ' + (i)* str(i)
    for i in range(n,0,-1):
        print (i)* str(i) + (n-i)* ' ' 
    for i in range(0,n,1):
        print (i)* str(i) + (n-i)* ' ' 
    for i in range(0,n,1):
        print (n-i)* ' ' + (i)* str(i)

pattern(5)