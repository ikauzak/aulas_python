#Abrindo um arquivo, o caminho pode ser absoluto ou relativo
hosts = open('hosts')
#O read(n) lê a quantidade de bytes (carácteres) do arquivo
print(hosts.read(7))
print(hosts.tell())
