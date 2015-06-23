import re

str = 'hello for you python openerp'
pattern=['odoo','openerp']
for a in pattern:
    match = re.search(a, str)
# If-statement after search() tests if it succeeded
    if match:                      
        print str ## 'found word:cat'
    else:
        print 'did not find'