import socket

HOST = '127.0.0.1'
PORT = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # khởi tạo socket
s.bind((HOST, PORT)) # rằng buộc công và địa chỉ ip
s.listen(1) # lắng nghe kết nối
conn, addr = s.accept() # chấp nhận kết nối conn là đối tượng socket, addr là địa chỉ ip cần kết nối
with conn:
    try:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024) # server nhận dữ liệu
            str_data = data.decode("utf8") # chuyển đổi giữ liệu thành chuỗi
            print(f"Client: {str_data}") # in
            mess = input() # nhập gửi client
            conn.sendall(bytes(mess, "utf8")) # gửi
            if not data or str_data == 'quit': # nếu không nhận được hay nhận được quit từ clien thì thoát
                break
    finally:
        s.close()