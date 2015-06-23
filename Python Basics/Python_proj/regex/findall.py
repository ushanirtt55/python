import re

text = 'abbaaabbbbaaaaa'

pattern = ['ab','ba']

for pat in pattern:
    for match in re.findall(pat, text):
        print 'Found "%s"' % match