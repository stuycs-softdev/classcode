import re

s="""
111-111-1111 and (222) 222-2222 and 1 (333) 333-3333
"""
pattern = "1? ?\(([0-9]{3})\) ([0-9]{3})-([0-9]{4})"
result = re.sub(pattern," \\1-\\2-\\3",s)
print s
print result
