# Bài tập giữa kỹ môn học SOA
**Ở bài tập này chúng ta hiện thực ứng dụng mô phỏng chức năng đóng học phí của ứng dụng iBanking.**

***Ứng dụng được thiết kế và xây dựng bằng Python IDE PyCharm trên hệ điều hành Microsoft Windows***

## 🚀 Chức năng
Ứng dụng bao gồm các luồng chức năng như:
- Đăng nhập: người dùng đăng nhập vào hệ thống bằng cách cung cấp thông tin đăng nhập (username, password).
- Sau khi đăng nhập thành công, ứng dụng sẽ hiển thị trên màn hình chức năng thanh toán dưới dạng biểu mẫu, người dùng cần điền vào các thông tin như mã số sinh viên, họ và tên sinh viên, ứng dụng sẽ hiển thị số tiền học phí sinh viên còn phải đóng.
- Đồng thời hệ thống cũng sẽ hiển thị thông tin người dùng username và số dư khả dụng.
- Sau khi điền xong biểu mẫu thanh toán và bấm submit, một mã OTP sẽ được gửi về email của người dùng và chuyển đến trang xác nhận OTP, người dùng nhập mã OTP và xác nhận lần cuối
- Đăng xuất: thoát phiên đăng nhập và trở về trang chủ

## 💾 Phiên bản của phần mềm sử dụng trong đồ án giữa kỳ.
- [JetBrains PyCharm](https://www.jetbrains.com/pycharm/download/#section=windows)
- [Python 3.11 (64-bit)](https://www.python.org/downloads/) 
- [XAMPP v8.1.10](https://www.apachefriends.org/download.html)
- [MySQL](https://www.mysql.com/)

## 📦 Install:   

*Các câu lệnh cài đặt được thực hiện trên Command prompt sau khi đã cài đặt phiên bản Python phù hợp.* 😉😉😉
(Sử dựng các terminal khác có thể gây ra lỗi hoặc sẽ có cú pháp khác)
Chúng ta bắt đầu với việc tạo venv environment 👇:
- B1. Cài đặt virtualenv
```sh
    python -m pip install --user virtualenv
```
- B2. Mở Terminal -> trỏ đến thử mục project, Tạo folder env (Lưu Ý nếu đã tồn tại thư mục env thì phải xóa đi trước khi tạo mới): 
```sh
    python -m venv env
```
- B3. Kích hoạn virtual env:
```sh
    .\env\Scripts\activate
```
- B4. Tải các thư viện liệt kê trong requirements.txt: 
```sh
python -m pip install -r requirements.txt
```
- B6. Import DATABASE: file user.sql vào MySQL.
Mở Xampp => Start 2 module Apace và MySQL. Bấm vào nút Admin trên dòng MySQl để vào PHPMyAdmin
 Tuỳ chỉnh port của MySQL là 3306
Sau khi bấm nút admin vào trang PHPMyAdmin
Bấm mục Nhập (Import) và chọn tệp Chọn tệp user.sql rồi bấm nhập (import) để import dữ liệu vào database
Kết quả có database tên user và có 5 Column là được. Trong đó chỉ có 2 cột users và schoolfee là có dữ liệu sẵn.
- B7. Chạy ứng dụng:
```sh
set FLASK_APP=flasky.py
flask run
```
- B8. Truy cập địa chỉ http://127.0.0.1:5000 trên trình duyệt để bắt đầu sử dụng ứng dụng(Địa chỉ có thể khác tuy nhiên sẽ được hiện thị trên cửa số dòng lệnh khi chạy flask app).

## Hướng dẫn chạy từng bước step by step:
- Bước 1
- Chạy flask app => truy cập địa chỉ http://127.0.0.1:5000 hoặc có thể thay đổi khác tuỳ máy.
Trên trang chủ bấm biểu tượng logout dưới mục Home để vào trang Login
- Nhập username và password (xem dữ liệu trong PHPMySQL bảng user.) hoặc nhập user3/admin => sẽ được chuyển đến trang giao dịch.
- Điền thông tin muốn đóng học phí vào form (xem dữ liệu trong PHPMySQL bảng SchoolFee ) hoặc điền mssv: 52000101/ho ten: Ngoc Linh/So hoc phi: 11000000(Số tiền học phí sẽ được tự động hiện khu nhập xong mssv ). Lưu ý số dư phải lớn hơn số tiền học phí thì mới submit được, nếu số dư bé hơn thì bạn phải logout và chọn user khác.
- Bấm submit => hệ thống sẽ gửi email về email của userName:(Đăng nhập gmail: Abc@gmail.com/passwprd để xem OTP được gửi về). Nếu muốn thay đổi email nhận mã OTP hãy thay đổi ở trong PHPMyADmin bảng users thay đổi thong tin email thành email mong muốn nhận mã OTP
- Ở trang xác nhận mã OTP => Nhập mã OTP được gửi về email => Bấm submit
- Nếu đúng mã OTP thì sẽ quay về trang giao dịch. Học phí được đóng sẽ bị xoá. Bấm trang chủ để xem trang học phí được cập nhật. 

!!! Nếu có thông tin gì bị nhập sai ở trang giao dịch hoặc trang OTP khiến bấm nút submit không có gì
=> Hãy vào PHPMyAdmin vào bảng TranscationProcessing xoá hết dữ liệu
## Author
- Lê Tuấn Anh - 51900698.
- Tống Đức Thành Nam - 52000896.
- Phạm Nguyễn - 52000092.
