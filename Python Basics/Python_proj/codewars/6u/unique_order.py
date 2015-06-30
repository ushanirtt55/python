def unique_in_order(iterable):
    num = map(str, list(str(iterable)))
    for i in range(len(num)):
        for j in 
            num.pop(i+1)
    print num     
    
unique_in_order('AAAABBBCCDAABBB')   
