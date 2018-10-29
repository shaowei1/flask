# def yang():
#     try:
#         a = 1
#         # a = 1 % 0
#     except Exception as e:
#         print(e)
#     else:
#         return yang
#     print(a)
class user():
    def __init__(self):
        self.__password = None

    def double(self, value):
        return value * 2

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.password_hash = self.double(value)


u = user()
u.password = 2
print(u.password)
