import socket

HOST = '127.0.0.1'
PORT = 65432

class VNCServer():

    def __init__(self):
        self.socket = None
        
        pass

    def __initialize_socket(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(HOST, PORT)

    def listen(self):
        self.socket.listen()

    def accept_connection(self):
        __connection, __address =  self.socket.accept()

        with __connection as connection:
            print(f'Accepted connection from {__address}')
            accepting_data = True
            while accepting_data:
                data = connection.recv(1024)
                print(f'Received [{len(data)}] of data')
                if not data:
                    accepting_data = False



# -------------------------------
# Main
# -------------------------------

if __name__ == "__main__":
    server = VNCServer()
    
                    
