from pandas.core.common import is_number
def sum(*args):
    a=list(args)
    total=0
    for i in a:
        if is_number(i):
            total=total+i
        else:
            continue
    return total
        
"""from __builtin__ import sum as builtin_sum

def sum(*args):
    return builtin_sum(arg for arg in args if isinstance(arg, int))"""
    
"""s = sum
def sum(*args):
    return s(x for x in args if isinstance(x, int))"""
    
a=sum(1,2,3,4,5,'a')
print a