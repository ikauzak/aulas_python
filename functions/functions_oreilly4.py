def get_name():
    name = input('Qual o seu nome?')
    return name

def say_name(name):
    print('Seu nome é {}.' .format(name))

def get_and_say_name():
    """Get and display name"""
    name = get_name()
    say_name (name)

get_and_say_name()
