# curso de python basico professor Poyatos 

import socket

ports = [21,22,80,443,445,3306,25] # Coloquei as principais portas 

for port in ports:
	client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	client.settimeout(0.2) # as vezes eu mudo o tempo de resposta, porque pode variar de alvo pra alvo
	code = client.connect_ex(("", port)) # Aqui "" coloque o alvo 
	if code == 0:
		print(port, "Aberta") # somente as portas abertas irão aparecer	