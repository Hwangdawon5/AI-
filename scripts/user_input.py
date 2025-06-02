# user_input.py

def get_user_input():
    """
    사용자에게 추천 조건을 입력받아 딕셔너리 형태로 반환합니다.
    """
    print("🔍 AI 도구 추천을 위한 정보를 입력해주세요!")

    purpose = input("1. 사용 목적을 입력하세요 (예: 텍스트 생성, 이미지 제작 등): ").strip()
    category = input("2. 관심 있는 AI 카테고리를 입력하세요 (예: 텍스트, 이미지, 음악 등): ").strip()
    difficulty = input("3. 원하는 사용 난이도 (0=쉬움, 1=보통, 2=어려움, 3=전문가): ").strip()
    customization = input("4. 커스터마이징 가능성 수준 (0~3 숫자 입력): ").strip()
    target_user = input("5. 사용자 유형 (예: 학생, 연구자, 디자이너 등): ").strip()

    return {
        "purpose": purpose,
        "category": category,
        "difficulty": difficulty,
        "customization": customization,
        "target_user": target_user
    }

def preprocess_input(user_input):
    """
    사용자 입력값을 정제하여 모델 입력에 적합한 형태로 가공합니다.
    """
    return {
        "purpose": user_input["purpose"].lower().strip(),
        "category": user_input["category"].lower().strip(),
        "difficulty": int(user_input["difficulty"]),
        "customization": int(user_input["customization"]),
        "target_user": user_input["target_user"].lower().strip()
    }

if __name__ == "__main__":
    raw = get_user_input()
    clean = preprocess_input(raw)
    print("\n🧼 정리된 입력값:")
    print(clean)
