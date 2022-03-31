from calculadora import soma

try:
    print(soma(10, '30'))
except AssertionError:
    print('Conta inválida')
