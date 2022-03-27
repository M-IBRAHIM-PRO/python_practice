#THIS IS A PROBLEM DUE TO MULTIPLE INHERITENCE.
class A:
    pass
class B(A):
    passf
class C(A):
    pass
class D(B,C):
    pass