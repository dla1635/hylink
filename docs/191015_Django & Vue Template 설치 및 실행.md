# Django & Vue 설치 및 실행 

> - 프로젝트 초기 설정 
> - 장고 관리자 및 api 관리 



### Setup 

> Window 기준으로 가상 환결 설정하기 

```bash
$ yarn install 
$ python -m venv .venv
$ source .venv/Scripts/activate
```



### Django pakage 설치 

```bash
$ pip install -r requirements.txt
$ python manage.py migrate
```



### Server 테스트 확인하기

> backend 

```bash
$ python manage.py runserver 
```

> frontend

```bash
$ yarn serve
```



### Django 관리자 계정 만들기

```bash
$ python manage.py createsuperuser
```

```bash
사용자 이름 : 아무개
이메일 주소: 아무개@ssafy.com
Password: 아무거나
Password(again): 아무거나
```



### Server 실행하기

```bash
$ yarn build
$ python manage.py runserver
```

- Vue 메인화면 : http://127.0.0.1:8000/#/ 
- Django REST framework: http://127.0.0.1:8000/api/
- Django 관리자 페이지: http://127.0.0.1:8000/api/



### 파일 구조 

```
.venv
backend
	- api
		-migrations
		admin.py
		apps.py
		models.py
		tests.py
		views.py
    - settings
    	__init__.py
    	dev.py
    	prod.py
    __init__.py
    urls.py
    wsgi.py
dist
	- static
	index.html
docs
node_modules
public
	- static
	index.html
src
	- assets
	- components
	- services
	- store
	main.js
	router.js
	App.vu
.gitignore
vue.config.js
app.json
package.json
yarn.lock
README.nd
manage.py
db.sqlite3
requirements.txt
```

