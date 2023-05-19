import re

text = "foo    bar\t baz  \tqux"
regex = re.compile('\s+')
print(regex.split(text), '\n')

print(regex.findall(text), '\n')


text = """Dave dave@google.com￼
        Steve steve@gmail.com￼
        Rob rob@gmail.com￼
        Ryan ryan@yahoo.com￼
"""

pattern = r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}'

# re.IGNORECASE使正则表达式不区分大小写￼
regex = re.compile(pattern, flags=re.IGNORECASE)
print(regex.findall(text), '\n')
print(regex.search(text), '\n')

# sub: 替代
print(regex.sub("REDACTED", text), '\n')

# groups 查找方法之一
pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
regex = re.compile(pattern, flags=re.IGNORECASE)
m = regex.match('wesm@bright.com')
print(m.groups(), '\n')
print(regex.findall(text), '\n')

# sub: 特殊符号
print(regex.sub(r'Username: \1, Domain: \2, Suffix: \3', text), '\n')

