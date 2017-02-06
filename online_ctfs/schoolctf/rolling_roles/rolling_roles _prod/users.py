from hashlib import sha256

# Some awkward autoinc realization
_current_id = 0


class User:
    def __init__(self, login, password):
        global _current_id
        self.id = _current_id
        _current_id += 1
        self.login = login
        # If everyone
        self.password = sha256(password).hexdigest()
        # If FBI will ask for user passwords I'd be prepared
        self.__secret = password

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __hash__(self):
        if hasattr(self, "hashval") is False:
            def calc(string):
                val = 0
                ind = 0
                for i in string:
                    val ^= ord(i) << (ind * 8)
                    ind = (ind + 1) % 4
                return val
            self.hashval = calc(self.login + self.__secret)
        return self.hashval

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __repr__(self):
        return '<User name={0} hash={1}>'.format(self.login, self.hashval)


class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.get_id()] = user

    def add_users(self, users):
        for user in users:
            self.add_user(user)

    def get_by_id(self, id):
        try:
            return self.users[id]
        except KeyError:
            return None

    def get_by_name(self, name):
        for user in self.users.itervalues():
            if user.login == name:
                return user
        return None

