#Author:Padmavathi
import socket
import ssl
hostname = "padma"
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations('server.crt')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
        ssock.connect(('127.0.0.1', 6664))

        buf = b''  # Buffer to hold received client data
        try:
            while True:
                data = ssock.read(1024)
                if data:
                    # Server sent us data. Append to buffer
                    buf += data
                else:
                    # No more data from client. Show buffer and close connection.
                    print("Received:", buf.decode('ascii'))
                    break
        finally:
            ssock.sendall(b'close connection')
            print("closing connection")
    sock.close()
