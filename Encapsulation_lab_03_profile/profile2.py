class Profile:
    def __init__(self, username, password):

        def username_is_valid(username):
            return 5 <= len(username) <= 15

        if not username_is_valid(username):
            raise ValueError(f"The username must be between 5 and 15 characters.")
        self.__username = username

        def password_is_valid(password):
            special_chars = {
                'upper': 0,
                'digit': 0
            }
            for c in password:
                if c.isupper():
                    special_chars['upper'] += 1
                elif c.isdigit():
                    special_chars['digit'] += 1
            return len(password) >= 8 and special_chars['upper'] > 0 and special_chars['digit'] > 0

        if not password_is_valid(password):
            raise ValueError(f"The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    def __str__(self):
        return f"You have a profile with username:'{self.username}' and password: {'*' * len(self.password)}."




