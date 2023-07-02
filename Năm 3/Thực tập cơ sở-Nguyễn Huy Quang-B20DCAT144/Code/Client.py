import socket

HOST = '127.0.0.1'
PORT = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# tạo socket
s.connect((HOST, PORT))# rằng buộc socket đến địa chỉ và cổng
while True:
    mes = input() #nhập text
    s.sendall(bytes(mes, "utf8")) # gửi thông điệp qua server
    data = s.recv(1024)  # nhận phản hồi từ server
    print('Server Respone: ', data.decode("utf8")) #in ra phản hồi server
    if not data:
        break