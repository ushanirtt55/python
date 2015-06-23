def foo_with_yield():
    yield 1
    yield 2
    yield 3

x=foo_with_yield()
print x
print next(x)
print x
print next(x)
print x
print next(x)