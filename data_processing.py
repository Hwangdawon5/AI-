import pandas as pd
from config import firebase_connect

def preprocess_ai_tools(filepath):
    df = pd.read_csv(filepath)

    # 🔧 Firebase에서 사용할 수 없는 문자 제거: 공백 → '_', 마침표 제거
    df['tool_id'] = (
        df['tool_name'].str.replace(" ", "_").str.replace(".", "", regex=False) +
        "_" +
        df['target_user'].str.replace(" ", "_")
    )

    # 중복 제거
    df = df.drop_duplicates(subset='tool_id')

    return df[['tool_id', 'category', 'difficulty', 'quality', 'customization', 'target_user']]

def upload_to_firebase(df):
    db = firebase_connect()
    ref = db.reference('tools')

    for _, row in df.iterrows():
        ref.child(row['tool_id']).set({
            'category': row['category'],
            'difficulty': int(row['difficulty']),
            'quality': int(row['quality']),
            'customization': int(row['customization']),
            'target_user': row['target_user']
        })

    print("✅ Firebase 업로드 완료")

# 실행용
if __name__ == "__main__":
    df = preprocess_ai_tools("ai_tools.csv")
    upload_to_firebase(df)