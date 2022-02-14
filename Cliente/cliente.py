from tkinter import *
import socket

class Funcs():
    def conectar(self):
        self.ip = str(self.entrada_ip.get())
        self.porta = int(self.entrada_porta.get())
        self.userget = str(self.entrada_user.get())
        ServerIP = self.ip
        PORT = self.porta
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            self.username = self.userget
            self.client.connect((ServerIP,PORT))
            print(f'Conectado com sucesso a {ServerIP}:{PORT}')
        except:
            print(f'ERRO: Por favor, revise sua entrada: {ServerIP}:{PORT}')

    def enviaMessage(self):
        self.mensagemChat = str(self.entrada_chat.get())
        self.client.send(self.mensagemChat.encode('ascii'))
        self.entrada_chat.delete(0, END)
            
class Aplicativo(Funcs):
    def __init__(self):
        root = Tk()
        root.geometry("258x310+540+180")
        root.configure(background="#062F4F")
        root.title("Cliente")
        root.resizable(width=False, height=False) #Proibe modificar o tamanho da janela.
        self.root = root
        self.frames()
        self.widgetsroot()
        root.mainloop()

    def frames(self):
        self.frame_1 = Frame(self.root, borderwidth=2, relief="solid", background="#233237")
        self.frame_1.place(x=3 , y=4, width=125 , height= 83)
        self.frame_2 = Frame(self.root, borderwidth=2, relief="solid", background="#233237")
        self.frame_2.place(x=130 , y=4, width=125 , height= 83)
        self.frame_3 = Frame(self.root, borderwidth=2, relief="solid", background="#233237")
        self.frame_3.place(x=3 , y=90, width=252 , height= 110)

    def widgetsroot(self):
        self.lb_ip = Label(self.frame_1, text="Informe o IP", background="#233237", font=("Rockwell",11, "bold")).place(x=17 ,y=13)
        self.entrada_ip = Entry(self.frame_1)
        self.entrada_ip.place(x=21, y=35, width=80 )
        self.lb_porta = Label(self.frame_2, text="Informe a porta", background="#233237", font=("Rockwell",11, "bold")).place(x=5 ,y=13)
        self.entrada_porta = Entry(self.frame_2)
        self.entrada_porta.place(x=21, y=35, width=80 )
        self.lb_user = Label(self.frame_3, text="Informe o usuário", background="#233237", font=("Rockwell",11, "bold")).place(x=60 ,y=15)
        self.entrada_user = Entry(self.frame_3)
        self.entrada_user.place(x=85, y=37, width=80 )
        self.bt = Button(self.frame_3, text="Conectar ao servidor", font=("Rockwell",9 , "bold"), command=self.conectar)
        self.bt.place(x=62, y=70)


Aplicativo()
