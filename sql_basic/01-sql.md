# SQL[2021.09.14]



## 1. DB

- 데이터의 집합
- RDB - 대부분(관계형 데이터 베이스)
- NoSQL - 배울일 없음



## 2. RDB

- Relational Database

- key와 value들의 관계를 table형태로 정리한 DB

- 용어정리

  - 스키마 : 데이터베이스의 명세(구조, 표현방법, col, datatype)
  - 테이블 : 테이블의 명세에 데이터가 들어가 있는 것(schema -> table 순)
  - 기본키 : 각 행(레코드)의 고유 값(유일무이한 값)

  

## 3. RDBMS

- Relational Database Management System

- 관계형 모델을 기반으로 하는 데이터베이스 관리시스템을 의미

- 프로그램 종류(브라우저처럼 각각 비슷하면서도 차이점이 존재함)

  - MySQL
  - SQLite(가장 가벼움)
  - ORACLE
  - MS SQL
  - PostgreSQL

  

## 4. SQL

- Structured Query Language

- 특정 소프트웨어 프로그램(데이터 관리)을 위한 특수목적 프로그래밍 언어

- 데이터베이스 스키마 생성 및 수정

- 자료의 검색 및 관리

- 데이터베이스 객체 접근 조정 관리

- csv = comma sperated values = 콤마로 구분되어있는 파일

  - cvs파일을 DB에 넣는 방법
    1. .mode csv
    2. .import ./hellodb.csv examples

- DML(data manipulation language)

  - INSERT
  - SELECT
  - UPDATE
  - DELETE

- DDL

  - CREATE
  - DROP
  - ALTER

  

## 5. DDL(Data Definition Language)

- CREATE

  - 데이터베이스에서 테이블 생성

  - ```sqlite
    -- 01_create_table.sql
    
    -- 내가 이름직접 이름 짓는 것은 소문자, 나머지는 대문자
    CREATE TABLE classmates (
      id INTEGER PRIMARY KEY,
      name TEXT
    );
    
    CREATE TABLE classmates(
      name TEXT,
      age INTEGER,
      address TEXT
    );
    
    CREATE TABLE classmates(
      id INTEGER PRIMARY KEY, -- AUTOINCREMENT, => 마지막 레코드가 삭제되었을 경우에는 마지막 레코드에 추가
      name TEXT NOT NULL,
      age INTEGER NOT NULL,
      address TEXT NOT NULL
    );
    
    CREATE TABLE users (
      -- id INTEGER PRIMARY KEY AUTOINCREMENT,
      first_name TEXT NOT NULL,
      last_name TEXT NOT NULL,
      age INTEGER NOT NULL,
      country TEXT NOT NULL,
      phone TEXT NOT NULL,
      balance INTEGER NOT NULL
    );
    ```

- DROP

  - 데이터베이스에서 테이블 제거

  - ```sqlite
    -- 05_delete.sql
    
    -- SELECT col1, col2 FROM table WHERE condition
    -- DELETE            FROM table WHERE condition
    
    DELETE FROM classmates WHERE id=5;
    ```

    

## 6. DML(Data Manipulation Language)

- INSERT(create)

  - 테이블에 단일 행 삽입

  - 따로 PRIMARY KEY로 지정하지 않으면 SQLite가 알아서 rowid로 관리하고 있음

  - ```sqlite
    -- 03_insert.sql
    
    INSERT INTO classmates (name, age, address)
    VALUES ('홍길동', 30, '서울');
    
    INSERT INTO classmates
    VALUES ('김싸피', 50, '서울');
    
    -- id없으면 알아서 할당
    INSERT INTO classmates (name, age, address)
    VALUES ('박삼성', 20, '구미'), ('최전자', 23, '부산');
    ```

- SELECT(read)**

  - 테이블에서 데이터를 조회

  - 함께 사용하는 clause

    - LIMIT
      - 쿼리에 반환되는 행 수를 제한
      - 특정 행부터 시작해서 조회하기 위해 OFFSET키워드와 함께 사용
    - WHERE
      - 쿼리에서 반환된 행에 대한 특정 검색 조건을 지정
    - SELECT DISTINCT
      - 조회결과에서 중복 행을 제거 SELECT DISTINCT

  - ```sqlite
    -- 04_read.sql
    
    -- 모든 컬럼에 대하여
    SELECT * FROM classmates;
    
    -- id, name 만 조회
    SELECT id, name FROM classmates;
    
    -- 앞에 2개만 조회(pagination)
    SELECT id, name FROM classmates LIMIT 2;
    
    -- 앞에 2개 이후 2개만 조회(pagination)
    SELECT id, name FROM classmates LIMIT 2 OFFSET 2;
    
    -- 주소 대전만 검색
    SELECT id, name, address FROM classmates WHERE address='대전';
    
    -- 나이를 중복없이 조회
    SELECT DISTINCT age FROM classmates;
    ```

- DELETE(delete)

  - 테이블에서 행을 제거

  - ```sqlite
    -- 05_delete.sql
    
    -- SELECT col1, col2 FROM table WHERE condition
    -- DELETE            FROM table WHERE condition
    
    DELETE FROM classmates WHERE id=5;
    -- TABLE 생성과정에서 AUTOINCREMENT 설정을 통해 이전에 삭제된 행의 값을 재사용하는 것을 방지
    ```

- UPDATE(update)

  - 기존 행의 데이터를 수정

  - SET clause에서 테이블의 각 열에 대해 새로운 값을 설정

  - ```sqlite
    -- 06_update.sql
    
    -- id값이 3인 레코드의 이름을 홍길동으로 주소를 제주도로 수정
    UPDATE classmates SET name='홍길동', address='제주도' WHERE id=3;
    ```

  - 중복 불가능한(UNIQUE) 값인 id를 기준으로 수정!

- ![crud](https://user-images.githubusercontent.com/73927750/133226770-56917bc0-64d2-4691-81b2-17523fa45c23.JPG)

- WHERE

  - ```sqlite
    -- 07_where.sql
    
    -- 나이가 30 이상 이름만
    SELECT first_name FROM users WHERE age >= 30;
    
    -- 나이가 30 이상이고 성이 '김'인 사람의 나이와 성만 조회
    SELECT age, last_name FROM users WHERE age >= 30 AND last_name='김';
    ```

    

## 7. Aggregate Functions

- 숫자 관련

  - COUNT, MAX, MIN, AVG, SUM

    - ```sqlite
      -- 08_function.sql
      -- 숫자 관련
      
      -- 레코드의 개수
      SELECT COUNT(*) FROM users;
      
      -- age 30이상의 평균 나이
      SELECT AVG(age) FROM users WHERE age >= 30;
      
      -- balance가 가장 높은 사람과 그 액수를 조회
      SELECT first_name, MAX(balance) FROM users;
      
      -- 나이가 30 이상인 사람의 평균 계좌 잔액 조회
      SELECT AVG(balance) FROM users Where age >= 30;
      ```

- 문자 관련

  - LIKE

    - 패턴 일치를 기반으로 데이터를 조회하는 방법

    - wildcard('_', '%')

      - '_' : 반드시 이자리에 한 개의 문자가 존재한다
      - '%' : 이 자리에 문자열이 있을 수도, 없을 수도 있다

    - ```sqlite
      -- 09_like.sql
      -- 문자 관련
      
      -- 20대 조회
      SELECT age FROM users WHERE age >= 20 AND age < 30;
      -- 나이중에 숫자가 2_로 시작하는 나이를 조회(_에는 한 글자만 존재)
      SELECT age FROM users WHERE age LIKE '2_';
      
      -- 지역번호가 02 인 사람만 조회
      -- 02-로 시작하고 뒤에는 관심없음(02로 시작만 아면 OK)
      SELECT phone FROM users WHERE phone LIKE '02-%';
      
      -- 이름이 *준으로 끝나는 사람 조회
      SELECT * FROM users WHERE first_name LIKE '%준';
      
      -- 중간번호가 5114인 사람만 조회
      SELECT phone FROM users WHERE phone LIKE '%-5114-%';
      ```

- 정렬

  - ORDER BY

    - 조회 결과 집합을 정렬

    - SELECT 문에 추가하여 사용(default = ASC)

    - ```sqlite
      -- 10_orderby.sql
      
      -- 나이를 오름차순으로 정렬하고 상위 10개만 조회
      SELECT * FROM users ORDER BY age -- ASC
      LIMIT 10;
      
      -- 나이순, 성 순으로 정렬하여 상위 10개만 조회
      SELECT age, last_name FROM users ORDER BY age, last_name ASC LIMIT 10;
      
      -- 계좌잔액 상위 10명의 이름 10개만 조회
      SELECT last_name, first_name, balance FROM users ORDER BY balance DESC LIMIT 10;
      
      -- 10대 중에 부자 10명만 조회
      SELECT last_name, first_name, balance FROM users WHERE age LIKE '1_' ORDER BY balance DESC LIMIT 10;
      ```

  - GROUP BY

    - 행 집합에서 요약 행 집합을 만든다

    - SELECT문의 optional임

    - 지정된 기준에 따라 행 세트를 그룹으로 결합 = 데이터를 요약하는 상황에 주로 사용

    - WHERE 절이 포함된 경우 반드시 WHERE 절 뒤에 작성!

    - ```sqlite
      -- 11_groupby.sql
      
      SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
      -- 같은 성을 가진 사람들의 수
      SELECT last_name, COUNT(*) AS name_count FROM users GROUP BY last_name;
      
      -- 나이 + 성이 같은 사람들을 grouping 하여 count 
      SELECT age, last_name, COUNT(*) FROM users GROUP BY age, last_name 
      
      -- 집안 재력 확인 => 성씨
      SELECT last_name, AVG(balance) AS asset 
      FROM users 
      GROUP BY last_name 
      ORDER BY asset DESC
      LIMIT 10; 
      ```

- ALTER TABLE

  - 테이블 이름은 복수형(Entity들의 집합)

  - table 이름 변경

  - table에 새로운 column추가

  - ```sqlite
    -- 12_alter_table.sql
    
    -- 테이블 생성
    CREATE TABLE articles (
      title TEXT NOT NULL,
      content TEXT NOT NULL
    );
    
    -- 데이터 추가
    INSERT INTO articles
    VALUES ('1번 제목', '1번 내용');
    
    -- 테이블 이름 변경
    ALTER TABLE articles 
    RENAME TO news;
    
    -- 테이블에 컬럼 추가
    ALTER TABLE news ADD COLUMN writer TEXT NOT NULL DEFAULT 'admin';
    ```



## 8. SQL & ORM

- db.sqlite3 내용 확인 방법 

  -> python manage.py dbshell

- python manage.py shell_plus --print-sql

  -> ORM을 통해 날아가는 SQL문을 확인하게 해주는 명령어

- ORM에서 대/소 관계 비교 조건

  - `__gte` , `__lte`, `__gt`, `__lt`

- aggregate()

  - 특정 필드 전체의 합, 평균, 개수 등을 계산할 때 사용

  - ```python
    # ORM
    
    from django.db.models import MaX, Avg, Sum
    
    # 전체 유저의 평균나이
    User.objects.aggregate(Avg('age'))
    
    # 성이 김씨인 유저들의 평균 나이
    User.objects.filter(last_name='김').aggregate(Avg('avg'))
    
    # 지역이 강원도인 유저들의 평균 계좌 잔고
    User.objects.filter(country='강원도').aggregate(Avg('balance'))
    
    # 계좌의 잔고 중 가장 높은 값
    User.objects.aggregate(Max('balance'))
    
    # 계좌 잔고의 총 합
    User.objects.aggregate(Sum('balance'))
    ```

- annotate()

  - GROUP BY와 같음
  - 마치 컬럼 하나를 추가하는 것과 같음
  - 특정 조건으로 계산된 값을 가진 컬럼을 하나 만들고 추가하는 개념
  - ![사진](https://user-images.githubusercontent.com/73927750/133286676-7f66df8d-d45e-4511-9717-1cb8c91c0519.JPG)

- aggregate()와 annotate()를 사용하는 이유

  -> 성능이 압도적으로 빠르다...ㄷㄷ

