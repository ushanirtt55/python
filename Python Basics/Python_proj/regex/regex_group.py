import re

patterns = [ 'this', 'that','text' ]
text = 'Does this text match the pattern?'

for pattern in patterns:
    
    match=re.search(pattern,  text)

    if match:
        print 'found a match!',match.group(), text
    else:
        print 'no match'
