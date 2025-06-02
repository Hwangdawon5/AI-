# config.py

import firebase_admin
from firebase_admin import credentials, db

def firebase_connect():
    # 인증 키 파일 경로 (루트 디렉토리에 있어야 함)
    cred = credentials.Certificate("firebase_credentials.json")

    # ⚠️ 정확한 databaseURL 넣기 (너는 아래 값 사용!)
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://ai-tools-pathfinder-default-rtdb.firebaseio.com'
    })

    return db
