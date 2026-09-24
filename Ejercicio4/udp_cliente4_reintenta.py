import sys
import socket

ip="localhost"
puerto = 9999

if len(sys.argv)>1:
    ip = sys.argv[1]
if len(sys.argv)>2:
    puerto = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # udp
# En el cliente no hay s.bind

print("Puerto: ", puerto, "; IP: ", ip)

numero = 1

while True:
    mensaje = input("Mensaje: ")

    if mensaje == "FIN":
        break

    num_str = str(numero)
    mensaje_enviar = num_str + mensaje
    s.sendto(mensaje_enviar.encode("utf-8"), (ip, puerto))

    s.settimeout(0.1)
    confirmacion = False
    while confirmacion == False:
        s.sendto(mensaje_enviar.encode("utf-8"), (ip, puerto))
        
        try:
            datagrama, origen = s.recvfrom(1024) # Tamaño máximo a recibir
            datagrama = datagrama.decode("utf8")
            if datagrama=="OK":
                print("Recibida confirmación")
                confirmacion=True
            else:
                print("Recibido datagrama no esperado")
        except socket.timeout:
            print("ERROR. El datagrama de confirmación no llega")

        except:    # Otras posibles excepciones dejamos que las maneje el usuario
            raise

    numero += 1
