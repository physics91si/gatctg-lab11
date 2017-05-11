import string

alphabet = (string.ascii_lowercase)

def first10():
    return ([s for s in alphabet[:10]])
def first10minus6th():
    return ([s for s in alphabet[:10] if s != alphabet[6]])
def repeated():
    return [j*i for i in first10minus6th() for j in range(1,4)]
def grid():
    return [repeated() for i in repeated()]
