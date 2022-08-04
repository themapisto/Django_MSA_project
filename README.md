# Django_MSA_project


## 1. git clone
```
mkdir projects ( /home/ubuntu/projects )
cd projects
git clone https://github.com/themapisto/Django_MSA_project.git
cd Django_MSA_project

```
## 2. docker-compose up
```
vim docker-compose.yml 
# version 3.3 으로 변경 (3.8 에러)
docker-compose up
```
## 3. WEB 서버 확인
```
localhost:8000/api/products
# DB 마이그레이션이 안되어있으면 에러가 뜰거임
```

![image](https://user-images.githubusercontent.com/52188918/176075642-ab57647e-1434-42d4-a788-488b952d0a0b.png)

## 4. DB migrate
``` 
# docker exec -it 이미지명 /bin/bash
python manage.py migrate
```

## 5. postman
[POST 방식 ]
http://3.145.116.119:8000/api/products

### Header
- Content-type : application/json
### body 
- raw
- "title", "image" key값 : value값 
- 예시
{
    "title": "title",
    "image": "image"
}

