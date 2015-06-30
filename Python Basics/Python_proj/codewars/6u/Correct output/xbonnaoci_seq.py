def Xbonacci(signature,n):
    res = signature[:n]
    l=len(signature)
    for i in range(n - l): 
        res.append(sum(res[-l:]))
    return res
    
a=Xbonacci([1,2,2,2,1,5,2], 10)
print a
