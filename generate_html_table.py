import pandas as pd

# CSV 파일 읽기
df = pd.read_csv('ai_tools.csv')

# 상위 10개 데이터만 HTML 테이블로 변환
html_table = df.head(10).to_html(index=False)

# HTML 템플릿 작성
html_content = f"""
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>AI 도구 데이터 표</title>
    <style>
        body {{
            font-family: 'Apple SD Gothic Neo', 'AppleGothic', sans-serif;
            padding: 20px;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }}
        th {{
            background-color: #f2f2f2;
        }}
    </style>
</head>
<body>
    <h1>AI 도구 상위 10개 목록</h1>
    {html_table}
</body>
</html>
"""

# HTML 파일로 저장
with open('table.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ table.html 파일이 생성되었습니다.")
