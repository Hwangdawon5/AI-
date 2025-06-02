import firebase_admin
from firebase_admin import credentials, db

# 인증서 경로 (파일은 현재 폴더에 있어야 함)
cred = credentials.Certificate("firebase_credentials.json")

# ✅ 너가 알려준 정확한 databaseURL 사용
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://ai-tools-pathfinder-default-rtdb.firebaseio.com/'
})

# 테스트용 데이터 쓰기
ref = db.reference('test')
ref.set({
    'message': 'Hello from Python!'
})

print("✅ Firebase 연결 및 쓰기 성공")
