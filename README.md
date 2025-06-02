# 🧠 AI 도구 학습 경로 추천 시스템

이 프로젝트는 사용자의 목표와 AI 활용 수준에 따라 맞춤형 AI 도구 학습 경로를 추천해주는 플랫폼입니다.

## 🌟 주요 기능
- 설문 기반 사용자 입력
- 조건 기반 & K-means 클러스터링 추천
- 시각화된 도구 학습 경로
- GitHub 기반 협업 및 HTML 결과 출력

## 🛠️ 사용 기술
- Python, Flask
- scikit-learn, Matplotlib
- HTML, CSS (CANVA 템플릿 연동)
- Firebase (현재는 미사용)

---

## 📦 Feature: Data Processing

이 브랜치는 AI 도구 추천 플랫폼에서 **데이터 정제**, **전처리**, **사용자 입력 처리**를 담당합니다.

### 📁 주요 폴더 구조

```
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



### ✅ 주요 작업
- 중복 제거, 결측값 처리, 컬럼 표준화
- 사용자 입력 정규화 및 구조화
- 정제된 CSV 생성 및 저장

### 🛠 스크립트 설명

| 파일명               | 설명                                       |
|----------------------|--------------------------------------------|
| `auto_clean_csv.py`  | 원본 데이터를 정제하고 저장하는 스크립트 |
| `user_input.py`      | 사용자 입력을 받아 모델 입력 형태로 변환 |
| `config.py`          | 설정값을 저장하는 파일                   |

### ⚠️ 주의사항
- `firebase_credentials.json`, `__pycache__`, `.env` 등의 파일은 Git 추적 대상에서 제외되어야 합니다.
- `.gitignore`를 반드시 최신 상태로 유지하세요.

---

## 🔗 관련 브랜치
- `feature/data-processing` – 데이터 전처리 및 사용자 입력 처리
- `feature/modeling` – 추천 모델 및 알고리즘 구현
- `feature/visualization` – 시각화 및 결과 출력
- `feature/frontend` – 프론트엔드 HTML 구조 설계
