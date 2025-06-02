import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, request, jsonify
from scripts.user_input import process_user_input
from model import load_data, find_similar_tools

app = Flask(__name__)
data = load_data()

@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.json
    if not user_input:
        return jsonify({"error": "입력값 없음"}), 400

    try:
        processed = process_user_input(user_input)
    except Exception as e:
        return jsonify({"error": f"입력 처리 오류: {str(e)}"}), 500

    results = find_similar_tools(
        data,
        processed['category'],
        processed['difficulty'],
        processed['quality'],
        processed['customization']
    )

    return jsonify(results.to_dict(orient='records')), 200

if __name__ == '__main__':
    app.run(debug=True)
