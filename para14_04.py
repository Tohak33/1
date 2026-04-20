import socket
import threading

clients = []
clients_lock = threading.Lock()

def handle_client(client_socket, client_address):
    print(f'Клиент {client_address} подключён')
    client_socket.send('Добро пожаловать в чат!'.encode('utf-8'))
    
    with clients_lock:
        for c in clients:
            if c != client_socket: c.send(f'Участник {client_address} присоединился'.encode('utf-8'))

    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode('utf-8')
            print(f'От {client_address} пришло:', message)
            
            with clients_lock:
                for c in clients:
                    if c != client_socket: c.send(f'{client_address}: {message}'.encode('utf-8'))
        except:
            break

    with clients_lock:
        if client_socket in clients:
            clients.remove(client_socket)
        for c in clients:
            try: c.send(f'Участник {client_address} покинул чат'.encode('utf-8'))
            except: pass

    client_socket.close()
    print(f'Клиент {client_address} отключился')

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind(('127.0.0.1', 5002))
server_socket.listen()

print('Сервер ждёт подключения клиентов')

while True:
    client_socket, client_address = server_socket.accept()

    with clients_lock:
        clients.append(client_socket)

    threading.Thread(target=handle_client, args=(client_socket, client_address), daemon=True).start()
