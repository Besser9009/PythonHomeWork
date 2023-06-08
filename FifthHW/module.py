def degree(A, B):
    if B == 1:
        return A
    elif B != 1:
        return (A * degree(A, B - 1))

def sumnumber_A(a, b):
    if a == 0:
        return b
    else:
        return sumnumber_A(a - 1, b + 1)
    
def sumnumber_B(a, b):
    if b == 0:
        return a
    else:
        return sumnumber_B(a + 1, b - 1)
    
def sumnumber_minA(a, b):
    if a == 0:
        return b
    else:
        return sumnumber_minA(a + 1, b - 1)
    
def sumnumber_minB(a, b):
    if b == 0:
        return a
    else:
        return sumnumber_minB(a - 1, b + 1)