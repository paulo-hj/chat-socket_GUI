import socket

HOST = "127.0.0.1"
PORT = 61565

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

def conexaoInicial():
    try:
        cliente, address = server.accept()
        print(f"Nova conexão: {str(address)}")
        clientes.append(cliente)
        cliente.send('getUser'.encode('ascii'))
        usuario = cliente.recv(2048).decode('ascii')
        usuarios.append(usuario)
        globalMensagens(f'{usuario} acabei de entrar no chat!'.encode('ascii'))
    except:
        pass

conexaoInicial()