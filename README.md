# 백엔드 API 구성 프로젝트

## 1. 💿 실행하기

### 1) 필요 패키지 다운로드

```bash
$ pip install -r requirements.txt
```

### 2) .env 파일 구성

DB 서버 주소 유출 방지를 위해 .env 파일을 사용하였습니다. <br />
따라서 git clone 이후 .env 파일 구성이 필요합니다. <br />
.env 파일 내용은 다음과 같습니다.

```text
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://[username][password]@[HOST_IP]:[Port]/[Database]'
```

.env 파일은 main 폴더와 동일한 경로에 위치합니다.

### 3) API 서버 실행

본 프로젝트는 Flask를 활용해 API를 구성하였습니다.
main 의 app 파일로 API 서버를 실행합니다.

```bash
$ python main/app.py
```

이후 API 서버는 127.0.0.1:5000 으로 접속할 수 있습니다.

## 2. 📌 프로젝트 진행 우선순위 설정

1. 데이터 설명 문서 기반 DB ORM 설계
2. PostgreSQL 접속 환경 구성 (SQLAlchemy 활용)
3. 각 Table Model 구성
4. Table Model 기반 API 구성

## 3. ✅ 프로젝트 구현 내용

1. 환자, 방문 관련 빈도 수 제공 API 구성 완료
2. 각 테이블에서 활용하는 concept 정보 명시 완료
3. 페이지네이션 기능 추가 완료
4. 키워드 검색 기능 추가 완료
5. 각 테이블의 row 조회 API 일부 구성 완료

🔎 상세 API 사용방법은 main 폴더의 README 를 참고하세요.

## 4. ⚠️ 미구현점

### 1) 미구현점

1. 환자, 방문 관련 속성을 활용한 drug_exposure, condition_occurrence row 조회
2. datetime 속성 기반 조회 API
3. 복합 컬럼 검색

## 5. 🛠️ 개선계획

1. 환자, 방문 관련 속성을 활용한 drug_exposure, condition_occurrence row 조회 <br />
   a) person, visit_occurrence 테이블과 drug_exposure, condition_occurrence 테이블을 조인 합니다. <br />
   b) 이후 person, visit_occurrence 에서 활용하는 키워드에 따라 filter 조건을 추가합니다. <br />
   c) 구성한 SQLAlchemy 쿼리문에 페이지네이션을 적용합니다. <br />
   d) 각각의 검색 API에 맞게 쿼리 스트링을 구성합니다. <br />

2. datetime 속성 기반 조회 API <br />
   a) datetime을 사용하는 속성을 기반으로 SQLAlchemy 쿼리문을 작성합니다. <br />
   b) filter 조건에 `Extract` 내장 함수를 활용하여 연도, 월, 일을 파싱합니다. <br />
   c) 구성한 SQLAlchemy 쿼리문에 페이지네이션을 적용합니다. <br />
   d) 검색할 조건의 쿼리 스트링으로 year, month, day 속성명을 사용합니다. <br />

3. 복합 컬럼 검색 <br />
   a) 기반이 되는 API 에 복합 조건으로 활용할 쿼리 스트링을 추가합니다. <br />
   b) model에 구성된 조회 쿼리문에 사용자로부터 입력받을 쿼리 스트링 검색 조건을 filter 조건에 추가합니다. <br />
   c) 기본적으로 명시하지 않은 속성에는 None을 기본값으로 제공하고, 예외 처리 로직을 구성합니다. <br />
