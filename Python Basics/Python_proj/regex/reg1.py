import re

stri="(123)"
pattern=r'^\(d{3}\)'
match= re.search(r'(^\([(\d{3})]*\) (\d{3})-(\d{4})$)', '(123) 234-2345')
if match:
    print True
else:
    print False