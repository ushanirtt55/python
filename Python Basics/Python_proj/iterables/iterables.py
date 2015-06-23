import re


def chain(*iterables):
    # chain('ABC', 'DEF') --> A B C D E F
    for it in iterables:
        for element in it:
            yield element
            print "First"
            
a = chain('ABC', 'DEF')
for i in a:
    print i