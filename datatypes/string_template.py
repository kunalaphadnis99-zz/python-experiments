from string import Template

template = Template('$who is $what here?')
value_dict = {
    'who': 'Kunal',
    'what': 'TL'
}

substituted_value = template.substitute(value_dict)
print(substituted_value)
