from calculadora import soma

try:
    print(soma(10, '30'))
except AssertionError as e:
    print('Conta inválida')