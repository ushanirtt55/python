#In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

"""def filter_list(l):
    a=[]
    for i in l:
        if type(i)== int:
            a.append(i)
    return a

"""
"""def filter_list(l):
    'return a new list with the strings filtered out'
    return [i for i in l if not isinstance(i, str)]
  """
  
def filter_list(l):
    return filter(lambda x: not type(x) is str, l)

    
b= filter_list([1,'a','b',0,15])
print b           
    