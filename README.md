# Drug Inquiry Program

## 프로그램 개요
제약 회사의 약물 정보 조회, 추가, 삭제, 갱신 작업을 돕기 위한 응용 프로그램입니다.  
사용자는 DrugBank ID를 기준으로 약물 데이터를 조회, 수정, 추가, 삭제할 수 있습니다.

### 주요 기능
- **데이터베이스 접속** : 로컬컴퓨터 mySQL 호스트, 포트, DB 명, 비밀번호를 입력하여 연동할 수 있습니다.
- **약물 정보 조회**: 특정 약물의 상세 정보를 확인
- **약물 추가**: 데이터베이스에 새로운 약물 정보를 추가
- **약물 수정**: 기존 약물 정보를 수정하여 데이터베이스에 반영
- **약물 삭제**: 데이터베이스에서 약물 데이터를 삭제

---

## 필수 설치 라이브러리

프로그램 실행 전에 필요한 Python 라이브러리를 설치해야 합니다. 아래의 명령어를 사용하여 개별적으로 설치할 수 있습니다.

### 설치 단계

1. **MySQL Connector Python**
    ```bash
    pip install mysql-connector-python
    ```

2. **Matplotlib**
    ```bash
    pip install matplotlib
    ```

---

## 파일 구성 및 기능
```bash
drugprogram/
├── DB_QUERY           # mySQL에서 각 파일 순서에 따라 실행하여 예제 데이터베이스 생성       
├── dist/            
│   └── main.exe       # 실행 가능한 단일 EXE 파일
├── source_code/       
│   ├── main.py              # 프로그램 진입점
│   ├── connection_frame.py  # 데이터베이스 연결 UI
│   ├── database.py          # 데이터베이스 연결 및 쿼리 실행 모듈
│   ├── main_frame.py        # 메인 UI 및 검색/관리 기능
│   ├── view_details.py      # 약물 상세 정보 조회 UI
│   ├── add_drug.py          # 약물 추가 UI
│   ├── edit_drug.py         # 약물 수정 UI
│   ├── delete_drug.py       # 약물 삭제 처리
├── README.md                # 프로그램 설명 파일
```

### 1. `main.py`
프로그램의 시작점으로, 전체 응용 프로그램의 메인 프레임을 실행합니다.
- **기능**:
  - 프로그램 창을 열고 초기 화면 구성
  - 플랫폼에 따라 창 크기를 자동으로 조정
  - `ConnectionFrame`(데이터베이스 연결 화면) 호출

### 2. `database.py`
MySQL 데이터베이스와의 연결을 처리합니다.
- **기능**:
  - 데이터베이스 연결 설정
  - SQL 쿼리 실행
  - 결과 반환 또는 데이터 삽입, 삭제, 갱신

### 3. `connection_frame.py`
사용자가 MySQL 데이터베이스에 연결할 수 있도록 구성된 초기 화면입니다.
- **기능**:
  - 사용자로부터 데이터베이스 연결 정보를 입력받음
  - 연결이 성공하면 `MainFrame`으로 전환

### 4. `main_frame.py`
프로그램의 메인 화면으로, 데이터 조회, 추가, 수정, 삭제와 같은 주요 기능을 실행합니다.
- **기능**:
  - 약물 검색 및 전체 조회
  - 특정 약물의 상세 정보 보기
  - 약물 추가, 수정, 삭제 작업 호출
  - **결과 초기화 버튼**: TreeView에 표시된 모든 결과를 초기화

### 5. `view_details.py`
선택한 약물의 상세 정보를 표시합니다.
- **기능**:
  - 약물 및 분류 정보, 약물-효소-작용 정보, 약물-타겟 정보, 약물-경로 연관 정보를 탭으로 분리하여 표시
  - 각 데이터는 TreeView로 시각적으로 확인 가능

### 6. `add_drug.py`
새로운 약물 데이터를 추가하기 위한 화면을 제공합니다.
- **기능**:
  - 약물 기본 정보 및 관련 데이터를 입력받아 데이터베이스에 삽입
  - 동적 입력창(`+/- 버튼`)으로 여러 개의 데이터를 추가 가능 (예: 타겟 정보, 효소 정보 등)

### 7. `edit_drug.py`
기존 약물 데이터를 수정하기 위한 화면을 제공합니다.
- **기능**:
  - 선택한 약물의 데이터를 데이터베이스에서 읽어와 입력 필드에 미리 표시
  - 사용자가 수정한 데이터를 데이터베이스에 반영
  - 동적 입력창(`+/- 버튼`)으로 새로운 데이터를 추가 가능

### 8. `delete_drug.py`
기존 약물 데이터를 삭제하기 위한 간단한 확인 창을 제공합니다.
- **기능**:
  - 약물 삭제 여부 확인
  - 데이터베이스에서 약물 데이터 삭제 후 결과 반영

---

## 데이터베이스 구조

이 프로그램은 아래와 같은 데이터베이스 테이블 구조를 사용합니다. 테이블 생성 SQL 파일은 별도로 제공됩니다.

| 테이블명                 | 주요 컬럼                                      |
|--------------------------|-----------------------------------------------|
| `DRUG`                   | `DRUGBANK_ID`, `NAME`, `DESCRIPTION`, `CAS_NUMBER` |
| `CLASSIFICATION`         | `KINGDOM`, `SUPERCLASS`, `CLASS`, `SUBCLASS`      |
| `TARGET`                 | `TARGET_ID`, `NAME`, `ORGANISM`                  |
| `ENZYME`                 | `ENZYME_ID`, `NAME`, `ORGANISM`                  |
| `PATHWAY`                | `SMPDB_ID`, `NAME`, `CATEGORY`                  |
| `DRUG_ENZYME_ACTION`     | `DRUGBANK_ID`, `ENZYME_ID`, `ENZYME_ACTION`      |
| `DRUG_PATH_ASSOCIATION`  | `DRUGBANK_ID`, `SMPDB_ID`, `UNIPROT_ID`         |
| `DRUG_TARGET`            | `DRUGBANK_ID`, `TARGET_ID`                       |

---

## 실행 방법

1. **예제 데이터베이스 생성**
    - DB_QUERY 디렉토리에 포함된 쿼리 파일 1, 2번을 순서대로 mySQL에서 실행하여 DB를 생성합니다.

2. **프로그램 실행**
    - 다음 두 방법 중 하나를 이용하여 프로그램을 실행할 수 있습니다.
    ```bash
    (1) drugprogram/source_code 디렉토리 내 파일을 IDE 환경에서 열고, main.py 실행
    (2) drugprogram/dist 디렉토리 내 .exe 파일 실행
    ```

3. **데이터베이스 연결**
    - 호스트, 포트, 데이터베이스 이름, 사용자 이름, 비밀번호를 입력하여 데이터베이스에 연결합니다.
    - 각 사용자 로컬 환경 설정에 따라, mySQL 환경에 맞춰 위 정보를 입력하세요.

4. **약물 관리**
    - **검색**: 특정 약물 정보를 검색합니다.
    - **전체 조회**: 데이터베이스의 모든 약물 정보를 조회합니다.
    - **상세 정보 보기**: 선택한 약물의 상세 정보를 확인합니다.
    - **약물 추가**: 새로운 약물 정보를 입력하고 데이터베이스에 추가합니다.
    - **약물 수정**: 선택한 약물의 정보를 수정하여 데이터베이스에 반영합니다.
    - **약물 삭제**: 선택한 약물을 데이터베이스에서 삭제합니다.

5. **결과 초기화**
    - **결과 초기화 버튼**을 클릭하여 TreeView에 표시된 모든 데이터를 초기화하고 검색어 입력 필드를 비웁니다.

---
