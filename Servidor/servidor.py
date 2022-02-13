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
