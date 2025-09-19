class A:
    def show(self):
        print('ini adalah show A')

class B(A):
    pass

class C(A):
    def show(self):
        print('ini adalah show C')

class D(B,C):
    pass

d = D()
d.show()