import time, socket, sys
 
from RSA_copy import calcule_d,decrypt, encrypt
def chat_client(user_name):
    rest=calcule_d()
    d=rest[0]
    n=rest[1]
    e=rest[2]
    publicKey1=(e,n)

    socket_server = socket.socket()
    server_host = socket.gethostname()
    ip = socket.gethostbyname(server_host)
    sport = 8081
    
    print('This is your IP address: ',ip)
    server_host = input('Enter friend\'s IP address:')
    name = user_name+','+str(e)+','+str(n)
    
    
    socket_server.connect((server_host, sport))
    
    socket_server.send(name.encode())
    server_name = socket_server.recv(1024)
    server_name = server_name.decode()
    
    print(server_name,' has joined...')
    while True:
        message = (socket_server.recv(1024)).decode()
        
        clientsplit =server_name.split(',')
        eOther=clientsplit[1]
        nOther=clientsplit[2]
        nameOther=clientsplit[0]
        
        messageDecrypted=decrypt((d,n),message)
        print(nameOther, ":", messageDecrypted)
        
    
        message = input('Me : ')
        messageEncrypted=encrypt((int(eOther),int(nOther)),message)
        listToStr = ','.join(map(str, messageEncrypted))
        messageEncryptedList= listToStr 
        print("messageEncrypredList",messageEncryptedList)
        socket_server.send(str(messageEncryptedList).encode())  
        #socket_server.send(message.encode())  
