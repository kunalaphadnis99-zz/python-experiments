class Person:
    is_membership_allowed = False

    def __init__(self, name, age):
        self.name = name
        self.age = age
        if 18 < self.age < 38:
            self.is_membership_allowed = True

    def run(self):
        print(f'{self.name} is running...')

    @classmethod
    def add_numbers(cls, num1, num2):
        # print(f'{cls.name} -- this is inside class method without self') - Not allowed
        return num1 + num2

    @classmethod
    def dummy_method(cls):
        return cls('Jui K P', 30)

    @staticmethod  # no access to cls
    def static_add_numbers(num1, num2):
        return num1 + num2

    def self(self):
        return self


person1 = Person('Kunal', 30)
# person2 = Person() - not allowed
print(f'Name: {person1.name}, Age: {person1.age}')
person1.run()
print(person1.is_membership_allowed)
print(person1.add_numbers(3, 3))
print(Person.add_numbers(3, 3))
print(Person.dummy_method().age)
print(Person.static_add_numbers(3, 3))

print(person1.self())
print(person1.self().self().self().self().self().self().self())


# standard class implementation
class NameOfTheClass:
    # attributes
    attribute1 = True
    attribute2 = 30

    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

    def method1(self, param1):
        self.attribute1 = False  # can access attributes using self keyword
        pass

    def method2(self):
        pass

    @classmethod
    def class_method1(cls, param1):
        # can use cls as __init__ method to instantiate this class object
        pass

    @classmethod
    def class_method2(cls):
        # can use cls as __init__ method to instantiate this class object
        pass

    @staticmethod
    def static_class_method():
        # no access to cls
        pass
