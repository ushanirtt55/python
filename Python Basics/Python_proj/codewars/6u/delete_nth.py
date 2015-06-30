import collections
def delete_nth(order,max_e):
    new_li=[]
    for i in range(len(order)):
        new_li=[item for item, count in collections.Counter(order).items() if count>=max_e]
    print new_li
 
delete_nth([1,2,3,1,2,1,3], 7)   
