def digital_root(n):
    num = map(int, list(str(n)))
    s=0
    for i in range(len(num)):
        s=s+num[i]
    return s
    
a=digital_root(15)
print a
    