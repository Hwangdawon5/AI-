import pandas as pd

# CSV 읽기
df = pd.read_csv('ai_tools.csv')

# HTML 테이블 문자열 생성
html_table = df.head(10).to_html(index=False)

# HTML 파일에 쓸 내용 만들기 (그래프 이미지 추가 포함!)
html_content = f'''
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>AI 도구 리포트</title>
    <style>
        /* 기존 스타일 유지 */
    </style>
</head>
<body>
    <div class="container">
        <h1>🤖 AI 도구 데이터</h1>
        <p><strong>총 데이터 수:</strong> 310개</p>
        <p><strong>컬럼 수:</strong> 6개</p>
        <h2>상위 10개 데이터 미리보기</h2>
        {html_table}
        <h2>Difficulty Distribution</h2>
        <img src="difficulty_distribution.png" alt="Difficulty Distribution Graph" width="600">
        <h2>Category Distribution</h2>
        <img src="category_distribution.png" alt="Category Distribution Graph" width="600">
    </div>
</body>
</html>
'''


# UTF-8로 파일 쓰기
with open('result.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ result.html 파일 생성 완료!")
