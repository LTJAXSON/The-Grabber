import paramiko
import socket
import threading
import socketserver
print("#!------------Starting The Honeypot-----------#!")
print("#!------------Note: Even if you see's an erorr dont worry it will still work-----------#!")
class SSHServer(paramiko.ServerInterface):
    def __init__(self):
        self.event = threading.Event()
        self.host_key = paramiko.RSAKey.from_private_key_file('key')

    def check_channel_request(self, kind, chanid):
        if kind == 'session':
            return paramiko.OPEN_SUCCEEDED
        return paramiko.OPEN_FAILED_ADMINISTRATIVELY_PROHIBITED

    def check_auth_password(self, username, password):
        username_password = open('Data-Collection/credentials.txt', 'a')
        username_password.write(f'Protocol : SSH , Host : {client_ip} , UserName : {username} , Password : {password}\n')
        if username == 'Honey' and password == 'LOUOFD#$%^XSW0()$#@!':
            return paramiko.AUTH_FAILED
        else:
            return paramiko.AUTH_FAILED
        return paramiko.AUTH_FAILED

    def check_auth_publickey(self, username, key):
        return paramiko.AUTH_FAILED

    def get_allowed_auths(self, username):
        return 'password'

    def get_client(self):
        transport = paramiko.Transport(self.event)
        transport.start_client()
        client = transport.remote_version
        transport.close()
        return client

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        global client_ip
        client_ip = self.client_address[0]
        transport = paramiko.Transport(self.request)
        ssh_server = SSHServer()
        
        transport.add_server_key(ssh_server.host_key)
        
        transport.local_version = 'SSH-2.0-OpenSSH_9.2p1 Debian-2'
        
        transport.start_server(server=ssh_server)
        
        channel = transport.accept(20)
        
        if channel is None:
            transport.close()
            while True:
                continue
        
        data = channel.recv(1024).decode()
        
        channel.close()
        
        transport.close()

class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == '__main__':
    server = ThreadedTCPServer(('0.0.0.0', 2222), ThreadedTCPRequestHandler)
    server.serve_forever()
