# Hylink _ 서울 1반 
## Final 프로젝트

- 프로젝트 기간 : 2019년 10월 14일 ~ 2019년 11월 08일
- 팀장 : 서진환
- 팀원 : 심창훈, 이동현, 이하동, 임종완

## 프로젝트 구조

> - 

## Git 관리 요령

> <b>"Git 작업은 프로젝트 기능(Feature) 단위로 진행한다."</b>

### Feature Branch Name Rule

- 작업파트_기능
  - 작업 파트 : AI, Model, Components[이름] 등 
  - 기능 : 작업하려는 기능의 요약 (명사 형태 권장)
  - 소문자와 언더바(_)로만 구성
  - ex) feature/link_main_sample

### Commit Message Rule

> <b>"커밋 메세지는 '제목행'과 '본문행'으로 구분된다"</b>

- 접두어는 [ADD] | [MOD] | [FIX] | [DEL] | [DOC] | [DAY]중에서 선택한다
  - [MOD] : 기능 구조의 변경 또는 개선
  - [FIX] : 오타 수정, 불필요한 주석 삭제 등 간단하고 사소한 코드 변경 + 버그 수정
- 접두어 다음에 오는 첫 글자와 고유명사만 대문자로 쓴다
- 제목은 명령문으로 작성한다 (첫 단어는 동사 기본형)
- 제목 행 끝에 마침표를 넣지 않는다
- 제목은 간결하게, 자세한 내용은 본문에 쓴다
- 한글 가능

#### 커밋 메세지 예시

##### 

```
[ADD] Enable autofocus on login/signup email input field

- when LoginDialog is opened or when switching between login/signup mode

Jira: S1P1213006-12
```

```
[MOD] Replace WriteDialog with ArticleWriter (nested router component)

Jira: S1P1213006-16
```

```
[DEL] Remove disqus comment component in detail page
```

```
[FIX] Fix ImgBanner error
```