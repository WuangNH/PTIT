import socket
import hashlib

HOST = '127.0.0.1'
PORT = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # tạo socket
s.connect((HOST, PORT)) # rằng buộc socket đến địa chỉ và cổng
while True:
    print("Client: ", end='')
    mes = input() # nhập
    key = "B20DCAT144"
    hashmes = hashlib.md5((mes + key).encode()).hexdigest() # băm thông điệp và key
    s.sendall(bytes(mes, "utf8")) # gửi thông điệp
    s.sendall(bytes(hashmes, "utf8")) # và gửi mà băm
    data = s.recv(1024) # nhận thông điệp
    hashdata = s.recv(1024) # nhập mã băm
    str_data = data.decode("utf8") # chuyển thành chuỗi
    str_hashdata = hashdata.decode("utf8") # chuyển thành chuỗi
  
    checkhash = hashlib.md5((str_data + key).encode()).hexdigest() # tạo lại đoạn mã từ phản hồi từ server
    if str_hashdata == checkhash:
        print('Server Respone: ', data.decode("utf8"))
        print("message from server is OK")
    else:
        print("the received message from server has lost its integrity")
    if not data:
        break