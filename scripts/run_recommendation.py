# run_recommendation.py

from user_input import get_user_input, preprocess_input

# 임시 추천 함수 (model.py에 연결되기 전 테스트용)
def find_similar_tools(user_data):
    # 여기선 그냥 임시 결과만 출력
    return [
        {
            "tool_name": "ChatGPT 3.5",
            "category": user_data["category"],
            "difficulty": 1,
            "target_user": user_data["target_user"]
        },
        {
            "tool_name": "Gemini 1.5",
            "category": user_data["category"],
            "difficulty": 2,
            "target_user": user_data["target_user"]
        },
        {
            "tool_name": "Notion AI",
            "category": user_data["category"],
            "difficulty": 0,
            "target_user": user_data["target_user"]
        }
    ]

def main():
    print("🔍 AI 도구 추천을 시작합니다!")
    raw_input = get_user_input()
    user_data = preprocess_input(raw_input)

    print("\n✅ 추천 결과:")
    recommendations = find_similar_tools(user_data)

    for i, tool in enumerate(recommendations, 1):
        print(f"{i}. {tool['tool_name']} - 카테고리: {tool['category']}, 사용자: {tool['target_user']}, 난이도: {tool['difficulty']}")

if __name__ == "__main__":
    main()
