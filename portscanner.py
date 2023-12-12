import socket
import os, sys

print("[#] Kirombo - Port Scanner [#]")

portas = [21,22,80,443,445,3306,25]

ip = input("IP Alvo: ")

for porta in portas:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.6)
    code = cliente.connect_ex((ip, porta))
    if code == 0:
        print(porta, ": aberta\n")
    else:
        print(porta, ": fechada\n")
