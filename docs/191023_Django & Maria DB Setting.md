# Django & Maria DB 연결

## Maria DB 설치

- 아래 URL에 접속해서 설치하기
https://downloads.mariadb.org/mariadb/10.4.8/

![mariadb](img/mariadb.PNG)

```text
password : root
```

## DB 생성

1. MySQL Client를 실행
2. 설치때 설정한 passwd를 입력 (passwd : root)
3. DB 생성

```sql
show databases; # 현재 데이터 베이스 확인

create database hylink; # hylink DB 생성

use hylink; # hylink 활성화
```

## Python Maria DB 설치

```python
pip install mysqlclient
```

## django DB setting

- setting.py 수정 (hylink에서는 `settings/dev.py`)

```python
DATABASES = {

    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db-name',  # hylink
        'USER': 'db-user-name', # root
        'PASSWORD': 'db-password', # root
        'HOST': 'db-adress', #공백으로 냅두면 default localhost
        'PORT': 'port-number' #공백으로 냅두면 default 3306
    }
}
```

## DB migrate

- **app별로 migrations&migrate를 해줘야 한다**

```python
python manage.py makemigrations <appname>
python manage.py migrate <appname>
```

- `appname`을 붙여서 app별로 migrate를 해준 뒤, 전체적으로 migrate를 한번 더 해준다.

```python
python manage.py migrate
```

_app 별로 migrate를 해주고 전체적으로 해야 error가 발생하지 않습니다._
