import re

text = 'This is some text -- with punctuation.'

print text
print

for pattern in [ r'^(?P<first_word>\w+)',#FIirst word
                 r'(?P<last_word>\w+)\S*$',#last word
                 r'(?P<t_word>\bt\w+)\W+(?P<other_word>\w+)', #starts with t and ends with another word
                 r'(?P<ends_with_t>\w+t)\b',#ends with t
                 ]:
    regex = re.compile(pattern)
    match = regex.search(text)
    print 'Matching "%s"' % pattern
    print '  ', match.groups()
    print '  ', match.groupdict()
