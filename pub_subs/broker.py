import socket
import threading
subscribers = {} #topic --> lista de los sockets de los subcriptores
lock = threading.Lock()
def handle_client(conn, addr):
    try:
        msg_type = conn.recv(1024).decode().strip() #Strip quita los espacios del principio y del final
        if msg_type.startswith("PUB:"):
            parts = msg_type[4:].split(":", 1) #Comienza a partir del PUB:
            if len(parts) != 2: #Esto se llama programación defensiva para considerar lo negativo. Considerar lo que no queremos
                conn.close()
                return
            topic, message = parts #Las partes se le asignan al tema y al mensaje
            print(f"[>] Publicacion en '{topic}':{message}")
            with lock: #Se cierra para que estas variables no se toquen
                for sub in subscribers.get(topic, []): #Iterador en funcion de la lista 
                    try:
                        sub.sendall(f"[{topic}] {message}".encode()) #Para mandar a los canales sobre esos temas
                    except:
                        continue
        else:
            conn.sendall(b"Comando no reconocido.")
    except Exception as e:
        print(f"[!] Error con {addr}: {e}")
    finally:
        conn.close()
def start_broker(hots = 'localhost', port = 14000):
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Se levanta el servidor
    server.bind((hots, port))
    server.listen(5)
    print(f"[BROKER]  Escuchando en {hots}: {port} ...")
    try:
        while True:
            conn, addr = server.accept()
            threading.Thread(target=handle_client, args=(conn, addr), #Se genera un hilo y recibe las instrucciones de nuestro client
            deamon = True).start()
    except KeyboardInterrupt:
        print("Broker detenido")
    finally:
        server.close()

if __name__ == "__main__":
    start_broker()
