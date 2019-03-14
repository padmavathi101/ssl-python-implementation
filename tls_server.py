import socket
import ssl
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain('server.crt', 'server.key')

days_file = open('padmavathi.txt','rb')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
     sock.bind(('127.0.0.1', 6664))
     sock.listen(5)
     with context.wrap_socket(sock, server_side=True) as ssock:
        conn, addr = ssock.accept()
        with conn:
            print('Recieved connection request from client',addr)
            print("Sending the file which gets verified and encrypted using TLS public key encryption")
            conn.write(b'The file name is padmavathi.txt\nThe File contains this data:')
            conn.sendfile(days_file)


