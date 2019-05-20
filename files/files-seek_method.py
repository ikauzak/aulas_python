#Abrindo um arquivo, o caminho pode ser absoluto ou relativo
hosts = open('hosts')
print('Current position: {}'.format(hosts.tell()))
print(hosts.read())

print('Current position: {}'.format(hosts.tell()))

hosts.seek(0)
print('Current position: {}'.format(hosts.tell()))
print(hosts.read())
