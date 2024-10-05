import re

text = "hello world"
pat = r'world$'
match = re.search(pat,text)
if match:
    print("yes")
else:
    print("no")


p = re.compile('\d+')
print(p.findall("I went to him at 11 A.M. on 4th July 1886"))