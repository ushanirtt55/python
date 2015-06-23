def foo_with_yield():
    yield 1
    print "ONE"
    yield 2
    print "TWo"
    yield 3
    print "THREE"

for yield_value in foo_with_yield():
        print yield_value