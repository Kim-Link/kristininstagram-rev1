# kristininstagram-rev1

[파이썬/장고 웹서비스 개발 완벽 가이드 with 리액트 스터디](https://www.inflearn.com/course/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%A5%EA%B3%A0-%EC%9B%B9%EC%84%9C%EB%B9%84%EC%8A%A4/)

<br>

### 0. 패키지 설치

파이썬 버전은 3.10 입니다.

```pip install -r requirements.txt```

<br>

### 1. 초기 마이그레이션 진행

```python manage.py makemigrations```

```python manage.py migrate```

<br>

### 2. superuser 생성

```python manage.py createsuperuser```

<br>

### 3. .env 생성

```
# .env 내용
    
SECRET_KEY = 'Django SECRET_KEY 입력'


SOCIAL_AUTH_GOOGLE_CLIENT_ID = "GOOGLE_CLIENT_ID 입력"
SOCIAL_AUTH_GOOGLE_SECRET = "GOOGLE_SECRET 입력"
STATE = "STATE"

SOCIAL_AUTH_KAKAO_CLIENT_ID = "Kakao rest api key 입력"
SOCIAL_AUTH_KAKAO_SECRET = "Kakao app ID 입력" 
```
