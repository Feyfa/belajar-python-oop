class A :
    def method_A(self) :
        print('ini adalah method_A')

class B :
    def method_B(self) :
        print('ini adalah method_B')

class C(A, B) :
    pass

c = C()

c.method_A()
c.method_B()