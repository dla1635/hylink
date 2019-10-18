# AWS 초기 셋팅

## IP address & key pair file로 AWS 접속하기(PuTTY)

1. https://www.putty.or 에서 putty 설치
2. PuTTYgen으로 private key 만들기

![puttygen](img/puttygen.PNG)

   - `Load` 버튼을 눌러 key pair file을 선택한 뒤, `Save private key` 버튼을 눌러 private key 생성

3. PuTTY로 AWS 인스턴스 접속하기

![putty1](img/putty1.PNG)

   - `Host Name`에 private IP address를 입력

![putty2](img/putty2.PNG)

   - Connection > SSH > Auth에서 `Private key for authentication`에 2번에서 만든 private key를 가져오기

4. `open`버튼을 눌러 접속

![putty3](img/putty3.PNG)
    - `ubuntu`를 입력하고 로그인

## 주피터 노트북 설치 및 사용

1. 주피터 노트북 설치

   - `apt`란 advanced packaging tool로 Ubuntu를 포함한 Debian 계열의 리눅스에서 쓰이는 패키지 관리 툴

```shell
sudo apt-get update
sudo apt-get install python3-pip
sudi pip3 install notebook
```

2. 주피터 노트북 비밀번호 설정

    - passwd 설정한 뒤 SHA1 값 기록하기

```python
python3
>>> from notebook.auth import passwd
>>> passwd()
```

3. 주피터 환경 설정

```shell
ifconfig # 현재 서버 내부망 IP 주소 확인
jupyter notebook --generate-config # config 파일 위치 확인 
sudo vi /home/ubuntu/.jupyter/jupyter_notebook_config.py
# sudo vi [config.py 위치]
```

- jupyter_notebook_config.py열어서 파일 가장 아래 쪽에 다음 내용을 추가

```python
c = get_config()
c.NotebookApp.password = u'sha1:{해시 값}'
c.NotebookApp.ip = '{내부 IP}'
c.NotebookApp.notebook_dir = '{시작 디렉토리}'
# 내부 IP로는 SSH로 접속했을 때 콘솔 창에 나오는 아이피를 입력
```

![configsetting](img/configsetting.PNG)

4. 주피터 노트북 실행

```shell
sudo jupyter-notebook --allow-root
```

![jupyter](img/jupyter.PNG)

   - 8888 포트번호로 열린 것을 확인
   - `private IP/8888` 로 접속