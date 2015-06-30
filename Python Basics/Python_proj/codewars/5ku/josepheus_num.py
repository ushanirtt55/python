def josephus_survivor(ls, skip):
    lis=[]
    for i in ls:
        lis.append(i)
    skip -= 1 
    idx = skip
    b=0
    while len(lis) > 1:
        idx=(b+skip-1) % len(lis)
        lis.pop(idx)
        idx = (idx + skip) % len(lis)
    return 'survivor: ', lis[0]

a=josephus_survivor((1,2,3,4,5,6,7), 3)
print a
        