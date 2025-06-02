import requests

# Flask 서버 주소
url = "http://127.0.0.1:5000/recommend"

# 사용자 입력 예시
data = {
    "category": "텍스트",
    "difficulty": 1,
    "quality": 2,
    "customization": 1
}

# POST 요청 보내기
response = requests.post(url, json=data)

# 결과 출력
print("🔍 추천 결과:")
print(response.json())
