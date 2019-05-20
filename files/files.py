#Abrindo um arquivo, o caminho pode ser absoluto ou relativo
hosts = open('hosts')
hosts_file_contents = hosts.read()
print(hosts_file_contents)
