
import time, socket, sys
from RSA_copy import calcule_d, decrypt,encrypt


# Driver code    


rest=calcule_d()
d=rest[0]
n=rest[1]
e=rest[2]
publicKey1=(e,n)
new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
 
port = 8081
new_socket.bind((host_name, port))
print( "Binding successful!")
print("This is your IP: ", s_ip)
 
name = "Serveur"+','+str(e)+','+str(n)
 
new_socket.listen(1) 
 
 
conn, add = new_socket.accept()
 
print("Received connection from ", add[0])
print('Connection Established. Connected From: ',add[0])
 
client = (conn.recv(1024)).decode()
print(client + ' has connected.')
 
conn.send(name.encode())
while True:
    clientsplit =client.split(',')
    eOther=clientsplit[1]
    nOther=clientsplit[2]
    nameOther=clientsplit[0]
    message = input('Me : ')
    messageEncrypted=encrypt((int(eOther),int(nOther)),message)
    print("messageEncrypred",messageEncrypted)
    listToStr = ','.join(map(str, messageEncrypted))
    messageEncryptedList= listToStr 
    print("messageEncrypredList",messageEncryptedList)


    #sned message encrypted server to client


    conn.send(str(messageEncryptedList).encode())

    #receive  from client


    message = (conn.recv(1024)).decode()
    print("messageEncrypted from client =",message)

    messageDecrypted=decrypt((d,n),message)
    print(nameOther, ':', messageDecrypted)