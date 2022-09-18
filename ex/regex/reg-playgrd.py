import re



x = 'Ayyub is 6 and MEkropok ME 2 fave numbers are 7 and 11 and ismaeel is 9 years old'

x1 = re.findall(r'[0-9]+', x)
x2 = re.findall(r'[AEIOUM]+\s+', x)
x3 = re.findall(r'ME\S+', x) 

print('x1', x1)
print('x2', x2)

# parenthesis() to indicate start and end of extraction
email = 'zaburraya.me@gmail.com'

email1 = re.findall(r'(\S+)@', email)
print(email1)


# escape character \ for special characters like $
# .search() finds first match but does not extract
# use .search(regex, var).group() to extract first match
# /d+ for digits, same as [0-9]+
money = 'I have $2.50 left, paid $4.60 for \ burgers'

money1 = re.findall(r'\$([0-9.]+)', money)
money2 = re.search(r'\$\d+\.\d+', money).group()


# Regarding r, these 2 lines are the same, raw string literals, the \n is not handled as a new line in both cases:
# moneyex2 = r'I have $2.50 left, paid $4.60 \n for burgers'
# moneyex2 = 'I have $2.50 left, paid $4.60 \\n for burgers'

# why r is important, in money str, you need to do money4 as the eqvlnt of money3, to find \ (actually \\) as handled by py
# Therefore, always add an r for regex so that the regex pattern will be treated as a string literal
# first 4 paras: https://docs.python.org/3/library/re.html

money3 = re.findall(r'\\', money)
money4 = re.findall('\\\\', money)


print(money)
print(money1)
print(money2)

phrase = 'Please enter the nine-digit id as it appears on your colour - coded pass-key'

phrase1 = re.findall(r'\b-\b', phrase)
phrase2 = re.findall(r'\B-\B', phrase)
phrase3 = re.findall(r'\w+\W+-\W+\w+', phrase)

print('phrase1', phrase1)
print('phrase2', phrase2)
print('phrase3', phrase3)
