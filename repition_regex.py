import re

#()? optional indicates the expression inside () can appear 0 or 1 time.
batRegex = re.compile(r'Bat(wo)?man')
mo=batRegex.search('The adventures of Batman, Batwoman & Batwowowowoman')
mo.group()
print(mo.group())


#()* optional indicates the expression inside () can appear 0 or multiple times.
starRegex = re.compile(r'Bat(wo)*man')
star=starRegex.search('The adventures of Batwowowowoman')
star.group()
print(star.group())

#Here, simply looking for phone number pattern.
phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
pn = phoneRegex.search('My phone number is 415-555-1234. Call me')
pn.group()
print(pn.group())

#Here, simply looking for phone number pattern with or without things inside ()
phRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
area = phRegex.search('My phone number is 555-1234. Call me')
area.group()
print(area.group())

#()+ must indicates the expression inside () must appear at least 1 time or more
btRegex = re.compile(r'Bat(wo)+man')
bt = btRegex.search('The adventures of Batwoman') #('Batman') won't work b'coz there need to be at least 1 wo.
bt.group()
print(bt.group())

#escape +, *, ?  and find only these characters
regex = re.compile(r'\+\*\?')
reg = regex.search('I learnt about +*? regex syntax')
reg.group()
print(reg.group())

#escape +, *, ?  and find multiple these characters
regx = re.compile(r'(\+\*\?) +')
rex = regx.search('I learnt about +*?+*?+*?+*?+*?+*? regex syntax')
rex.group()
print(rex.group())


#exactly n number of times
haRegex = re.compile(r'(Ha){3}')
ha = haRegex.search('He said "HaHaHa" ')
ha.group()
print(ha.group())

#[finding if 3 phone numbers has area code
#codeRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
#bb = codeRegex.search('hey man, 044-432-1111, 111-1234, 123-123-1234')
#bb.group()
#print(bb.group())]

#finding ()expression in a range of 3, 5
#heRegex = re.compile(r'(he){3, 5}')
#he = heRegex.search('He said "hehehe"')
#he.group()
#print(he.group())

#finding ()expression in a range of 3 to anything
#hyRegex = re.compile(r'(he){3, }')
#hy = hyRegex.search('He said "hyhyhy "')
#hy.group()
#print(hy.group())

#finding in longest range
digitRegex = re.compile(r'(\d){3,5}')
dr = digitRegex.search('1234567890')
dr.group()
print(dr.group())

#finding in shortest range
shortRegex = re.compile(r'(\d){3,5}?')
sr = shortRegex.search('1234567890')
sr.group()
print(sr.group())
