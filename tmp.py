class L:

    def __init__(self):
        self.t = []

    def add_user(self,user):
        self.t.append(user)

    def get_last_user(self):
        return self.t[-1]

    def c(self):
        self.t[-1].a = 3
class U:

    def __init__(self):
        self.a=1
        self.b=2
        self.c=3

l = L()
u = U()
l.add_user(u)

print(l.get_last_user() is u)