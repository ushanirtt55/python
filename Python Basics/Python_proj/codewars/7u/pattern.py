def pattern(n):
    print ("Pattern C")
    for e in range (n,0,-1):
        print((n-e) * ' ' + e * '*')
    
    print ("Pattern D")
    for g in range (n,0,-1):
        print(g * ' ' + (n-g) * '*')    
            
            
                
                
pattern(4)               