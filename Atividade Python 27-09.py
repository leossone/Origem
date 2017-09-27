
#ATIVIDADE 27/09
f=open("C:/Users/1700631/Desktop/Python/Lista_IPs.txt","r")#CAMINHO DO ARQUIVO A SER CONSULTADO
IP = f.readlines()
f.close()
ip_valido = ""
ip_invalido = ""
for i in range (len(IP)):#AREA AONDE OCORRE A VALIDAÇÃO DOS IPS
    IP2 = IP[i].rsplit(".")
    if (int(IP2[0])<=255 and int(IP2[1])<=255 and int(IP2[2])<=255 and int(IP2[3])<=255):
        ip_valido += IP[i] + "\n"
    else:
        ip_invalido += IP[i] + "\n"

f=open("C:/Users/1700631/Desktop/Python/ip_valido.txt","w")#DOCUMENTOS GERADOS COMO VÁLIDOS 
f.write(ip_valido)
f.close()

f=open("C:/Users/1700631/Desktop/Python/ip_invalido.txt","w")#DOCUMENTOS GERADOS COMO INVÁLIDOS
f.write(ip_invalido)
f.close()

print ("ARQUIVOS GERADOS COM SUCESSO!")#MENSAGEM AO USUÁRIO APÓS A CONCLUSÃO DO PROGRAMA


