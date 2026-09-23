import socket
import sys

# puerto por defecto: 9999
puerto = 9999

if len(sys.argv)>1:
    puerto = int(sys.argv[1])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # udp
s.bind(("", puerto))

print("Puerto: ", puerto)

while True:
    mensaje, direccion = s.recvfrom(1024)
    print("Direccion: ", direccion)
    print("Mensaje:", mensaje.decode("utf-8"))