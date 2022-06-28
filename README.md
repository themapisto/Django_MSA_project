# Django_MSA_project

## 1. django ubuntu 가상환경 설치
```
sudo apt-get install python3-venv
python3 -m venv venv
source venv/bin/activate
```

## 2. git clone
```
cd projects ( /home/ubuntu/projects )
git clone https://github.com/themapisto/Django_MSA_project.git
cd Django_MSA_project
```
## 3. docker-compose up
```
vim docker-compose.yml 
# version 3.3 으로 변경 (3.8 에러)
docker-compose up
```
## 4. WEB 서버 확인
localhost:8000 접속 
# 장고페이지 뜨면 

## 5. DB migrate
``` 
# python manage.py backend sh
python manage.py migrate
```
