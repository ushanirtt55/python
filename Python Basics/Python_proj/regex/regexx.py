import re


str = 'an example word:cataa@@a!!'
match = re.search(r'word:\w?', str)
# If-statement after search() tests if it succeeded
if match:                      
    print 'found', match.group() ## 'found word:cat'
else:
    print 'Not found'
    
match = re.search(r'b\w+', 'foobar') 
print match.group() == "bar"

str1="ushanirtt55@gmail.com,yfvfybh@sam.com"
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str1) ## ['alice@google.com', 'bob@abc.com']
for email in emails:
    # do something with each found email string
    print email

str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
print tuples  ## [('alice', 'google.com'), ('bob', 'abc.com')]
for tuple in tuples:
  print tuple[0]  ## username
  print tuple[1]  ## host