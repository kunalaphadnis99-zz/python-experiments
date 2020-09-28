# 1 What would be the output of the below 4 print statements?
# Try to answer these before you click RUN!
# string is immutable in nature, that is it cannot be modified once created

username = 'superuser'
password = 'supersecret'

long_string = '''
this
is
a
long
string
here
'''

# print(type(username))
# print(type(password))
# print(type(long_string))

# print(username + ' ' + password)

print(type(int(str(100))))

print("Hello {}, your balance is {}.".format("Cindy", 50))

print("Hello {0}, your balance is {1}.".format("Cindy", 50))

print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50))

print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))

# 2 How would you write this using f-string? (Scroll down for answer)

name = 'Cindy'
amount = 90
age = 30

print(f'Hello {name}, your balance is {amount}.')
print(f'Hello {name}, your balance is {amount} and your age is {age}.')

some_string = 'abcdefghijklmnopqrstuvwxyz'
print(some_string[0])
print(some_string[8])
print(some_string[0:9])
print(some_string[0:10])
print(some_string[0:10:1])
print(some_string[0:10:2])
print(some_string[0:10:3])
print(some_string[0:10:10])
print(some_string[0:])  # defaulted to end of string
print(some_string[:6])  # defaulted to start of string
print(some_string[::1])  # defaulted to start and end of string
print(some_string[::2])  # defaulted to start and end of string
print(some_string[-1])  # negative index means start from the end of string
print(some_string[::-1])  # negative index means start from the end of string

# strings are immutable

new_str = some_string.swapcase()
print(new_str)

new_str1 = some_string.upper()
print(new_str1)

new_str2 = some_string.capitalize()
print(new_str2)
