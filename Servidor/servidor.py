import socket
import threading

print("Informe o host e porta")
HOST = input("Host: ")
PORT = int(input("Port: "))

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((HOST,PORT))
server.listen()
print(f'O servidor está ativo {HOST}:{PORT}')
print("Aguardando clientes...")

clientes = []
usuarios = []

def globalMensagens(message):
    for client in clientes:
        client.send(message)

def mensagensget(cliente):
    while True:
        try:
            mensagemCliente = cliente.recv(2048).decode('ascii')
            globalMensagens(f'{usuarios[clientes.index(cliente)]} :{mensagemCliente}'.encode('ascii'))
        except:
            saiuCliente = clientes.index(cliente)
            cliente.close()
            clientes.remove(clientes[saiuCliente])
            chaveCliente = usuarios[saiuCliente]
            print(f'{chaveCliente} deixou o chat...')
            globalMensagens(f'{chaveCliente} nos deixou...'.encode('ascii'))
            usuarios.remove(chaveCliente)

def conexaoInicial():
    try:
        cliente, address = server.accept()
        print(f"Nova conexão: {str(address)}")
        clientes.append(cliente)
        cliente.send('getUser'.encode('ascii'))
        usuario = cliente.recv(2048).decode('ascii')
        usuarios.append(usuario)
        globalMensagens(f'{usuario} acabei de entrar no chat!'.encode('ascii'))
        user_thread = threading.Thread(target=mensagensget,args=(cliente,))
        user_thread.start()
    except:
        pass

conexaoInicial()