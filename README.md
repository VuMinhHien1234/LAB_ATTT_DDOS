Code được cấu hình lại nhằm phục vụ mục đích học tập từ nguồn:
https://github.com/skavngr/netbot

Tuyên bố từ chối trách nhiệm
Việc sử dụng phần mềm và các script tải về từ kho lưu trữ này là hoàn toàn tùy thuộc vào quyết định và rủi ro của bạn, với sự đồng ý rằng bạn sẽ hoàn toàn chịu trách nhiệm cho bất kỳ thiệt hại nào đối với hệ thống máy tính của bạn hoặc sự gián đoạn hệ thống khác do các hoạt động này gây ra.


Bạn hoàn toàn chịu trách nhiệm về việc sử dụng phần mềm này.
Tác giả sẽ không chịu trách nhiệm với bất kỳ thiệt hại nào bạn gặp phải hoặc sự gián đoạn dịch vụ xảy ra đối với các hệ thống khác khi sử dụng, chỉnh sửa hoặc phân phối phần mềm này.

Không có bất kỳ lời khuyên hay thông tin nào (bằng miệng hoặc văn bản) từ tác giả hoặc website này được xem như một cam kết bảo hành cho phần mềm.

NetBot là gì?
Mã Proof-of-Concept (PoC): Mô phỏng một môi trường botnet Client-Server.
Thiết lập botnet: Dễ dàng thiết lập một chuỗi botnet báo cáo về trung tâm CCC.
Mô phỏng tấn công DDoS: Hỗ trợ các thử nghiệm tấn công DDoS (Chỉ dành cho mục đích nghiên cứu/ thử nghiệm).
Yêu cầu
Python 3
Hệ điều hành hỗ trợ
Đã thử nghiệm trên:
Debian
Ubuntu
CentOS
MacOS High Sierra

Cảnh báo về nguyên mẫu (Prototype Warning)
Đây chỉ là mã nguyên mẫu và có thể không hoạt động đúng như mong đợi.
Bạn có thể fork dự án và chỉnh sửa để phù hợp với nhu cầu.
Hiện tại, nhóm phát triển đang tiếp tục cải thiện về:
Độ ổn định và giao diện người dùng.
Thêm nhiều vector tấn công: Hiện tại chỉ hỗ trợ TCP Flood, ICMP Flood, UDP Flood, SYN Flood.

Mã nguồn
netbot_server.py: Mã nguồn của máy chủ (CCC).
netbot_config.py: CCC tải thông tin về mục tiêu cần tấn công từ file này.
netbot_client.py: Mã nguồn của client (bots).
Cách thiết lập/thử nghiệm NetBot
Thử nghiệm trên cùng một máy: Bạn có thể thử nghiệm trên một máy duy nhất.
Mục đích chính:
Triển khai các client (bots) trên các máy khác nhau.
Chạy mã máy chủ (CCC) trên máy của bạn.
Lưu ý quan trọng:
Bạn cần chỉnh sửa địa chỉ CCC server trong file netbot_client.py. Nếu không, các bot sẽ không kết nối được với CCC.
