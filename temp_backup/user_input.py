# scripts/user_input.py

def process_user_input(user_input):
    category = user_input.get('category', '기타')
    difficulty = int(user_input.get('difficulty', 1))
    quality = int(user_input.get('quality', 1))
    customization = int(user_input.get('customization', 1))

    return {
        'category': category,
        'difficulty': difficulty,
        'quality': quality,
        'customization': customization
    }
