from concurrent.futures import thread
import socket
import threading
import time

PORT = 5050
FORMATO = 'utf-8'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

Porta = 0
ip = ""
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
deseja_entrar = False
nome_client = ""

print(f"[CLIENT] Colinha para acessar o servidor (ip, porta): ", ADDR)

def handle_mensagens():
    while(True):
        msg = client.recv(1024).decode()
        mensagem_splitada = msg.split("=")
        global nome_client
        if(nome_client != mensagem_splitada[1]):
            print(mensagem_splitada[1] + ": " + mensagem_splitada[2])

def enviar(mensagem):   
    client.send(mensagem.encode(FORMATO))

def enviar_mensagem():
    global nome_client
    while(1):
        mensagem = input()
        if(mensagem == "/NICK"):
            nome = input('Digite seu novo nome:')
            print("O usuário " + nome_client + " mudou seu nome para " + nome)
            nome_client = nome
            enviar("nome=" + nome)
        else:
            enviar("msg=" + mensagem)

def enviar_nome():
    global nome_client
    nome = input('Digite seu nome: ')
    nome_client = nome
    enviar("nome=" + nome)
                

def iniciar_envio():
    global deseja_entrar
    global ip
    global Porta
    while(not deseja_entrar):
         change = input("digite /ENTRAR parar entrar no chat: ")
         if(change == "/ENTRAR"):
             ip_input = input("informe o ip: ")
             ip = str(ip_input)
             Porta_input = input("informe a porta: ")
             Porta = int(Porta_input)
             addr = (ip, Porta)
             client.connect(addr)
             thread1 = threading.Thread(target=handle_mensagens)
             thread1.start()
             deseja_entrar = True

    enviar_nome()
    enviar_mensagem()

def iniciar():
    thread2 = threading.Thread(target=iniciar_envio)
    thread2.start()
    
iniciar()