# 🧠 Feature: Data Processing

이 브랜치는 AI 도구 추천 플랫폼에서 **데이터 정제**, **전처리**, **사용자 입력 처리**를 담당합니다.

## 📁 주요 폴더 구조
```
.
├── data/
│ ├── ai_tools.csv # 원본 데이터
│ └── cleaned_ai_tools.csv # 정제된 데이터
├── scripts/
│ ├── auto_clean_csv.py # 데이터 정제 스크립트
│ ├── config.py # 설정 파일
│ └── user_input.py # 사용자 입력 처리
├── docs/
│ └── user_input_spec.md # 사용자 입력 명세 문서
├── tests/
│ ├── check_file.py
│ ├── firebase_test.py
│ └── test_upload_a.py
└── .gitignore # Git 추적 제외 규칙 파일
```


## ✅ 주요 작업

- 중복 제거, 결측값 처리, 컬럼 표준화
- 사용자 입력 정규화 및 데이터 구조화
- 정제된 CSV 생성 및 저장

## 🛠 스크립트 설명

| 파일명               | 설명                                       |
|----------------------|--------------------------------------------|
| `auto_clean_csv.py`  | 원본 데이터를 정제하고 저장하는 스크립트       |
| `user_input.py`      | 사용자 입력을 받아 모델 입력 형태로 변환함     |
| `config.py`          | 설정값을 저장하는 파일                      |

## ⚠️ 주의사항

- `firebase_credentials.json`, `__pycache__`, `.env` 등의 파일은 Git 추적 대상에서 제외되어야 합니다.
- `.gitignore`를 반드시 최신 상태로 유지하세요.

## 🔗 관련 브랜치

- `feature/modeling` – 추천 모델 및 알고리즘 구현
- `feature/frontend` – 사용자 인터페이스 및 시각화 구현
