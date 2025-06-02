import pandas as pd
import matplotlib.pyplot as plt

# 데이터 읽기
try:
    df = pd.read_csv('ai_tools.csv')
    print(f"✅ ai_tools.csv 로드 완료! 총 {len(df)}개의 데이터")
except FileNotFoundError:
    print("❌ ai_tools.csv 파일이 없습니다. 같은 폴더에 있는지 확인하세요.")
    exit()

# ✅ [1] 카테고리 분포 (막대그래프)
try:
    category_counts = df['Category'].value_counts()
    plt.figure(figsize=(10, 6))
    category_counts.plot(kind='bar', color='skyblue')
    plt.title('Category Distribution')
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('category_distribution.png')
    plt.close()
    print("📊 category_distribution.png 생성 완료!")
except Exception as e:
    print(f"❌ Category 그래프 생성 실패: {e}")

# ✅ [2] 난이도 분포 (파이차트)
try:
    difficulty_counts = df['Difficulty'].value_counts()
    plt.figure(figsize=(6, 6))
    difficulty_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff','#99ff99'])
    plt.title('Difficulty Distribution')
    plt.ylabel('')  # y축 라벨 제거
    plt.tight_layout()
    plt.savefig('difficulty_distribution.png')
    plt.close()
    print("📈 difficulty_distribution.png 생성 완료!")
except Exception as e:
    print(f"❌ Difficulty 그래프 생성 실패: {e}")
