class PasswordManager:
    def __init__(self, word):
        self.__word = word
    
    # TODO: Implement the verify_password method
    def verify_password(self, my):
        if self.__word == my:
            return True
        return False



# Don't modify the code below this line
my_password = PasswordManager("secret123")
print(my_password.verify_password("secret123"))  # Should print: True
print(my_password.verify_password("wrong"))      # Should print: False
