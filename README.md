"Bài tập giữa kỹ môn học SOA" 
Đầu tiên chúng ta tạo venv environment:

B1. Cài đặt virtualenv
py -m pip install --user virtualenv

B2. Mở Terminal -> trỏ đến thử mục project
Tạo folerenv: 
py -m venv env

kích hoạn virtual env: 
.\env\Scripts\activate

Tải các thư viện liệt kê trong requirements.txt: 
python -m pip install -r requirements.txt

Chạy app: 
env FLASK_APP=flasky.py python -m flask run

Để chạy trên trình duyệt: 
http://127.0.0.1:5000
