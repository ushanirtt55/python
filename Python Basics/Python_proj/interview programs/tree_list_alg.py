def flatten(iterable):
    for elem in iterable:
        print elem
        if hasattr(elem, '__iter__'):
            for sub in flatten(elem): 
                print sub 
                print "SUB"            
                yield sub
            
        else:
            print elem 
            print "ELem"
            yield elem
            
print list(flatten([[1,2,3],[[2,3],4],[4,5,6],[8,9,[1,2,[2,3,4]]]]))