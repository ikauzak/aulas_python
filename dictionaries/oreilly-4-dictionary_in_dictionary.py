contacts = {
    'Jason': {
        'phone': '555-0123',
        'email': 'jason@example.com'
    },
    'Carl': {
        'phone': '555-0987',
        'email': 'carl@example.com'
    }

}
#Geralmente os dicionários são substantivos no plural, enquanto os dados listados dentro de um dicionário são singular.
for contact in contacts:
    print ("{}'s contact info:".format(contact))
    print(contacts[contact]['phone'])
    print(contacts[contact]['email'])
