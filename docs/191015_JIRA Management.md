# JIRA 관리

> 참고  https://community.atlassian.com/t5/Jira-Core-questions/epic-vs-story-vs-task/qaq-p/204224



## Issue types

### Epic

features 단위 모음(stories 모음)



### User Story

features = 사용자 기능 



### Sub-Task

story를 완성하기 위한 개발 업무들 

주로 하루 안에 완성할 수 있는 업무 위주로 작성한다 



### (Engineering) Task

Dev Stories = User Story에 직접적으로 연결되진 않는 기능들 



## Example

- **Epic** : 사용자 인증.

- **User Stories**

  - 사용자 로그인 화면
  - 비밀번호를 잊어 버렸을 때
  - 시도가 너무 많이 실패한 후 계정을 잠그기 설정
  - 구글 로그인 지원
  - 페이스 북 로그인 지원

- **Sub-Tasks**

   :

  -  사용자 로그인 화면 :
    - 디자인 로그인 페이지
    - SVG 아이콘과 이미지를 잘라내기
    - 로그인 페이지 HTML / CSS / JS를 구현하기
    - SQL 스크립트를 작성하여 테이블을 작성
    - 저장 프로 시저에 대한 SQL 스크립트를 만들기
    - 사용자 자원에 대한 웹 서비스 REST API를 작성
    - 로그인 페이지를 웹 서비스 REST API에 연결
  - 비밀번호를 잊어 버린 워크 플로 :
    - ...

- (Engineering) **Tasks** :

  - GitHub 프로젝트 저장소를 설정
  - GCP (또는 AWS) 계정, 컨테이너 및 서비스를 설정
    - (이들에 대한 하위 작업이있을 수도 있습니다)
    - ...
  - Jenkins CI 파이프 라인을 설정
  - 전반적인 (고수준) 시스템 아키텍처를 설계
  - 단위 테스트 및 조롱 프레임 워크를 연구하고 결정