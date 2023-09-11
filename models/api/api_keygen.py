# API key generator and saver
##TODO Make the API key generator to save the data to a DB, so that it can be used later.
##TODO Make the API key generator to check if the key is already in the DB, so that it can be used later.
##TODO Make the API key generator to check if the key is valid.
##TODO Make the API key generator to check if the key is expired.
##TODO Make the API key generator to check if the key is used.
##TODO Make the API key generator to check if the key is used by the same user.
##TODO Make the API key generator throw an error if the user tries to make a new key before the old one is expired.

import secrets
import string


class ApiKey:
    def __init__(self):
        self.key = self.key_gen()

    def key_gen(self):
        alphabet = string.ascii_letters + string.digits
        key = ''.join(secrets.choice(alphabet) for i in range(32))
        return key

    def save_key(self):
        with open("api_key.txt", "w") as file:
            file.write(self.key)

    def get_key(self):
        with open("api_key.txt", "r") as file:
            key = file.read()
        return key


