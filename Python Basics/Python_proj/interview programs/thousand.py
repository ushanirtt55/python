def thousands_with_comma(i):
    s, l = str(i), []    
    skip = len(s) % 3
    if skip:
        l.append(s[:skip])
        
    for start in xrange(skip, len(s), 3):
        l.append(s[start:start + 3])
    return ','.join(l)

a= thousands_with_comma(12345)
print a
