"""def capitals(word):
    c=word
    last=-1
    dup=[]
    s=[]
    for i in c:     
        if i.isupper():
            print i
            dup.append(i) 
            if i in dup:          
                while i in c[last + 1:]:
                    d = c[last+1:].index(i)
                    s.append(last + d + 1)
                    last += d+1  
            else:
                s.append(word.index(i))  
                                               
    return list(set(s))"""

"""def indices(l, val):

    retval = []
    last = -1
    while val in l[last + 1:]:
        i = l[last+1:].index(val)
        print l[last+1:],i
        retval.append(last + i + 1)
        last += i+1
     
    return retval

a=indices('AbCdAvA', 'A')
print a"""

"""  i=0
    for i in word:
        if i.islower()==False:
            c.append(word.index(i))
            print word.index('A')
    print c"""
    
def capitals(s):
    return [i for i, c in enumerate(s) if c.isupper()]

a= capitals('AAAAcAdBfCbCcAcB')
print a