import socket
import hashlib
HOST = '127.0.0.1'
PORT = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # tạo socket
s.bind((HOST, PORT)) # rằng buộc cổng
s.listen(1) # lắng nghe kết nối
conn, addr = s.accept() # chấp nhận kết nối conn là đối tượng addr là địa chỉ ip
with conn:
    try:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024) # chấp nhận dữ liệu
            hashdata = conn.recv(1024) # chấp nhận mã băm
            str_data = data.decode("utf8") # chuyển dữ liệu được băm thành chỗi
            str_hashdata = hashdata.decode("utf8") # chuyển đổi mã băm thành chuỗi
           
            key = "B20DCAT144"
            checkhash = hashlib.md5((str_data + key).encode()).hexdigest() # tạo mã băm từ thông điệp nhận được và key
            if str_hashdata == checkhash: 
                print("message from client is OK")
                print(f"Client: {str_data}")
            else:
                print("the received message from client has lost its integrity")
            print("Server: ", end='')
            mess = input()
            hashmess = hashlib.md5((mess + key).encode()).hexdigest() # tạo mã băm từ thông điệp vừa nhập và key
            conn.sendall(bytes(mess, "utf8")) # gửi thông điệp
            conn.sendall(bytes(hashmess, "utf8")) # gửi mã băm
            if not data or str_data == 'quit':
                break
    finally:
        s.close()