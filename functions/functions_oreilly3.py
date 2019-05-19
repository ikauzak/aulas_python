def say_hi(first, last='Masuda'):
    """Imprime o nome no console"""
    print('Hi {} {}!' .format(first, last))

help(say_hi)
say_hi('Bruno')
say_hi('Bruno', 'Kazuaki')
