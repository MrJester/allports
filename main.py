import threading
import socketserver


class ClientHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(2048)
        print("Received data from: {}:{}".format(self.client_address[0], self.client_address[1]))

        if self.data:
            self.request.sendall(self.data)


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


sockets = []
socket_threads = []
server = '127.0.0.1'

for port_number in range(1025, 1027):
    try:
        sockets.append(ThreadedTCPServer((server, port_number), ClientHandler))
        print("Socket opened on port {}".format(port_number))
    except OSError:
        print("Error opening socket on {}, port is already in use.".format(port_number))
        pass

for TDC_server in sockets:
    socket_threads.append(threading.Thread(target=TDC_server.serve_forever))

for TDC_server_thread in socket_threads:
    TDC_server_thread.setDaemon(True)
    TDC_server_thread.start()

while True:
    continue
