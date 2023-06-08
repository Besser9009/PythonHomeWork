def degree(A, B):
    if B == 1:
        return A
    elif B != 1:
        return (A * degree(A, B - 1))