A = int(input('Primeiro lado: '))
B = int(input('Segundo lado: '))
C = int(input('Terceiro lado: '))

if A > 0 and B > 0 and C > 0:
    if A + B > C and A + C > B and B + C > A:
       if A != B and A != C and B != C:
           print('Escaleno')
       else:
            if A == B and A == C and B == C:
                print('Equilátero')
            else:
                print('isósceles')
    else:
        print('Ao menos um dos valores indicados não servem para formar um triângulo.')
else:
    print('Ao menos um dos valores indicados não servem para formar um triângulo')