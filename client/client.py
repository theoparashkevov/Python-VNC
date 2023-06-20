import socket


HOST = "127.0.0.1"  
PORT = 65432        

class VNCClient():

    def __init__(self):
        pass

    def __initialize_socket(self):
        pass


    def connect():
        pass
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)




# -------------------------------
# Main
# -------------------------------
if __name__ == "__main__":
    pass
