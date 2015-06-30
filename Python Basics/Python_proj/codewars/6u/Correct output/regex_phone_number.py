import re

def validPhoneNumber(phoneNumber):
    match= re.search(r'(^\([(\d{3})]*\) (\d{3})-(\d{4})$)', phoneNumber) 
    if match:
        return True
    else:
        return False
    
a=validPhoneNumber("(123) 456-1234")
print a