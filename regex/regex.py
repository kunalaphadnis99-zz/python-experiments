import re

value = 'My name is Kunal. Still whatever you think, my name is Kunal A. P.'

# print('K' in value)

pattern = re.compile('K')
value_re = pattern.findall(value)
# print(value_re.start())
# print(value_re.end())
# print(value_re.span())
# print(value_re.group())
print(value_re)
