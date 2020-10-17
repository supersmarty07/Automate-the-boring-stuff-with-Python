import re
phoneNumRegex = re.compile(r'\'d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Call me 415-555-101 tomorrow, or at 15-555-9999 on Friday.')
print(mo.group)
