import re

text = 'This is some text -- \nwith punctuation.'
pattern = r'(?m)\bT\w+'
regex = re.compile(pattern)

print 'Text      :', text
print 'Pattern   :', pattern
print 'Matches   :', regex.findall(text)

"""
IGNORECASE    i
MULTILINE    m
DOTALL    s
UNICODE    u
VERBOSE    x
"""