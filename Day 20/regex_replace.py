import re

text = "Thank you very very much"

#pat = r'\b[a-z]{3}\b'
pat = r'very'

npat = 'so'

print(text)
print(re.sub(pat,npat,text))
