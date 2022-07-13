from random import randrange

def gerador():
    a = randrange(10)
    b = randrange(10)
    c = randrange(10)
    d = randrange(10)
    e = randrange(10)
    f = randrange(10)
    g = randrange(10)
    h = randrange(10)
    i = randrange(10)
    j = randrange(10)
    k = randrange(10)

    x = [a,b,c,d,e,f,g,h,i,j,k]
    s = 0

    for i in range(0, len(x)):
        s = s + int(x[i])

    x = str(x).replace(',', '').replace(' ','').replace('[', '').replace(']', '')

    if len(x) == 11 and s == 44:
        return True, print(f'Gerado o CPF de número {x[:3]}.{x[3:6]}.{x[6:9]}-{x[9:11]}')
    else:
        return False


gerador()

while gerador != True:
    gerador
    if gerador():
        break