class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.user_dict = {
            'key1': 111,
            'key2': 222,
            'key3': 333
        }

    def __str__(self):
        return f'{self.name} {self.age}'

    def __del__(self):
        print('Deleted user successfully')

    def __call__(self, *args, **kwargs):
        print('Called')

    def __getitem__(self, item):
        return self.user_dict[item]


user1 = User('Kunal', 30)
# print(dir(user1))
print(user1.__str__())

print(user1['key1'])

user1()

user1.__del__()
del user1
