class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def sign_in(self):
        print(f'User {self.username} signed in!')


class PermanentEmployee(User):
    def __init__(self, username, password):
        super().__init__(username, password)


class ContractedEmployee(User):
    pass


class HybridEmployee(PermanentEmployee, ContractedEmployee):
    def __init__(self, username, password):
        super().__init__(username, password)

    # def __init__(self, username, password):
    #    PermanentEmployee.__init__(self, username, password)
    #    ContractedEmployee.__init__(self, username, password)


user1 = PermanentEmployee('abcd@gmail.com', '123456')
user1.sign_in()
print(user1.username)
