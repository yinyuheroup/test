class A:
    def __init__(self):
        self.n = 2

    def add(self, m):
        print('self is {0} @A.add'.format(self))
        print(self)
        print(m)
        print(self.n)
        self.n += m
        print(self.n)


class B(A):
    def __init__(self):
        self.n = 1

    def add(self, m):
        print('self is {0} @B.add'.format(self))
        super().add(m)
        self.n += 3

b = B()
b.add(2)
print(b.n)