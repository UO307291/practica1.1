import socket
import sys
import random

# puerto por defecto: 9999
puerto = 9999

if len(sys.argv)>1:
    puerto = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # udp
s.bind(("", puerto))

print("Puerto: ", puerto)

while True:
    mensaje, direccion = s.recvfrom(1024)

    numero = random.randint(0, 1)
    if numero == 0:
        print("Simulando paquete perdido")
    else:
        print("Direccion: ", direccion)
        print("Mensaje:", mensaje.decode("utf-8"))