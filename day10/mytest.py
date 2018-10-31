# def yang():
#     try:
#         a = 1
#         # a = 1 % 0
#     except Exception as e:
#         print(e)
#     else:
#         return yang
#     print(a)


# class user():
#
#     def __getitem__(self, key):
#         return getattr(self, key, None)
#
#     def updata(self):
#         self.index = 1
#         self.max = 10
#
#         self.suffix = '%(index)d:%(max)d'
#
#         self.suffix = self.suffix % self
#         print(self.suffix)
#
#
# a = user()
# a.updata()

class user():
    def __init__(self):
        self._password = 1

    @property
    def password(self):
        return self._password

        # user.password = password

    @password.setter
    def password(self, value):
        self._password = value + self._password


a = user()
a.password = 2
print(a.password)
