import re

text = 'siddhi shintre'
pattern = r'siddhi'
match=re.findall(pattern,text)
match = re.search(pattern,text)
print(match)
print(match.start())
print(match.end())


strings = ['The quick brown fox', 'The lazy dog', 'A quick brown fox']
pat = r'^The'
for i in strings:
    if re.match(pat,i):
        print(i)
   

