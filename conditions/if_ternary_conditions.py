condition = True
if condition:
    print('It is true')
else:
    print('It is false')

number = 1440
divisor = 5
if number % divisor == 0 and 1440 % 2 == 0:
    print(f'Number {number} is divisible by {divisor} and even number')
else:
    print(f'Number {number} is not divisible by {divisor}')

print('')
print(bool('somestring'))
print(bool(''))
print(bool(5))
print(bool(0))
print(bool(-1))
print(bool(-10))
print(bool(True))
print(bool(None))

# ternary operators
# condition_if_true if condition else  condition_if_false
is_allowed = True
is_friend = True

# if is_allowed and is_friend:
#     can_message = 'messaging is allowed'
# else:
#     can_message = 'messaging is disabled'
# can be written as here below:
can_message = 'messaging is allowed' if (is_allowed and is_friend) else 'messaging is disabled'
# can_message = 'messaging is allowed' if (is_allowed or is_friend) else 'messaging is disabled'
print(can_message)
