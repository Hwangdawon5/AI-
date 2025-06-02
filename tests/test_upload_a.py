from config import firebase_connect

db = firebase_connect()

# 팀원 A의 테스트 데이터
ref = db.reference('users/teamA/test')
ref.set({
    'name': 'A',
    'goal': '텍스트 생성',
    'level': '중급',
    'frequency': '10회 이상'
})

print("✅ 팀원 A 테스트 업로드 성공")
    