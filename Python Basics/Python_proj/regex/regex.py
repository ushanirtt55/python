import re
email_id= raw_input("Enter Your email id: ")
print email_id
str = 'an example word:cataa@@a!!'
match = re.search(r'^([\w.-^%&]+)@([\w+.-]+)', email_id)
# If-statement after search() tests if it succeeded
if match:                      
    print 'Valid email id', match.group(2) ## 'found word:cat'
else:
    print 'invalid'
str1="ushanirtt55@gmail.com"
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str1) ## ['alice@google.com', 'bob@abc.com']
for email in emails:
   # do something with each found email string
   print email