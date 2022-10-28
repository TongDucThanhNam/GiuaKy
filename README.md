"Bài tập giữa kỹ môn học SOA" 
Đầu tiên chúng ta tạo venv environment:

py -m pip install --user virtualenv

py -m venv env

.\env\Scripts\activate

python -m pip install -r requirements.txt

env FLASK_APP=flasky.py python -m flask run

http://127.0.0.1:5000
