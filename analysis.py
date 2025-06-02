import pandas as pd

print("📂 CSV 파일을 불러오는 중...")

try:
    data = pd.read_csv('ai_tools.csv')
    print("✅ 컬럼명:", data.columns.tolist())
    print("✅ 데이터 형태:", data.shape)
    print("✅ 카테고리 종류:", data['category'].unique())
    print("✅ 난이도 분포:\n", data['difficulty'].value_counts())
    print("✅ 사용자 타입:", data['target_user'].unique())
except Exception as e:
    print("❌ 오류 발생:", e)
    import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from collections import Counter
import matplotlib.font_manager as fm

# 한글 폰트 설정
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

class AIToolVisualizer:
    def __init__(self, csv_file='ai_tools.csv'):
        """AI 도구 데이터 시각화 클래스"""
        self.data = pd.read_csv(csv_file)
        self.colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD']
        
    def create_category_distribution(self, save_path='charts/category_distribution.png'):
        """카테고리별 AI 도구 분포 - 도넛 차트"""
        plt.figure(figsize=(10, 8))
        
        category_counts = self.data['category'].value_counts()
        
        # 도넛 차트 생성
        wedges, texts, autotexts = plt.pie(category_counts.values, 
                                          labels=category_counts.index,
                                          autopct='%1.1f%%',
                                          colors=self.colors[:len(category_counts)],
                                          startangle=90,
                                          pctdistance=0.85)
        
        # 중앙에 구멍 만들기 (도넛 차트)
        centre_circle = plt.Circle((0,0), 0.70, fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        
        plt.title('AI 도구 카테고리별 분포', fontsize=16, fontweight='bold', pad=20)
        
        # 범례 추가
        plt.legend(wedges, [f'{cat}: {count}개' for cat, count in category_counts.items()],
                  title="카테고리",
                  loc="center left",
                  bbox_to_anchor=(1, 0, 0.5, 1))
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
    def create_difficulty_analysis(self, save_path='charts/difficulty_analysis.png'):
        """난이도별 분석 - 누적 바 차트"""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # 1. 카테고리별 난이도 분포
        difficulty_by_category = pd.crosstab(self.data['category'], self.data['difficulty'])
        difficulty_by_category.plot(kind='bar', stacked=True, ax=ax1, 
                                   color=['#E8F5E8', '#FFE4B5', '#FFB6C1'])
        ax1.set_title('카테고리별 난이도 분포', fontsize=14, fontweight='bold')
        ax1.set_xlabel('카테고리')
        ax1.set_ylabel('도구 개수')
        ax1.legend(['쉬움(0)', '보통(1)', '어려움(2)'], title='난이도')
        ax1.tick_params(axis='x', rotation=45)
        
        # 2. 전체 난이도 분포
        difficulty_counts = self.data['difficulty'].value_counts().sort_index()
        bars = ax2.bar(range(len(difficulty_counts)), difficulty_counts.values, 
                      color=['#90EE90', '#FFD700', '#FF6347'])
        ax2.set_title('전체 난이도 분포', fontsize=14, fontweight='bold')
        ax2.set_xlabel('난이도')
        ax2.set_ylabel('도구 개수')
        ax2.set_xticks(range(len(difficulty_counts)))
        ax2.set_xticklabels(['쉬움(0)', '보통(1)', '어려움(2)'])
        
        # 막대 위에 숫자 표시
        for bar, count in zip(bars, difficulty_counts.values):
            ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                    str(count), ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
    def create_user_type_analysis(self, save_path='charts/user_analysis.png'):
        """사용자 타입별 분석"""
        plt.figure(figsize=(12, 8))
        
        # 사용자 타입별 개수
        user_counts = self.data['target_user'].value_counts()
        
        # 수평 바 차트
        bars = plt.barh(range(len(user_counts)), user_counts.values, 
                       color=self.colors[:len(user_counts)])
        
        plt.yticks(range(len(user_counts)), user_counts.index)
        plt.xlabel('도구 개수')
        plt.title('사용자 타입별 AI 도구 분포', fontsize=16, fontweight='bold', pad=20)
        
        # 막대 끝에 숫자 표시
        for i, (bar, count) in enumerate(zip(bars, user_counts.values)):
            plt.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
                    str(count), ha='left', va='center', fontweight='bold')
        
        plt.grid(axis='x', alpha=0.3)
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
    def create_quality_difficulty_heatmap(self, save_path='charts/quality_difficulty_heatmap.png'):
        """품질-난이도 히트맵"""
        plt.figure(figsize=(10, 6))
        
        # 품질과 난이도의 교차표 생성
        heatmap_data = pd.crosstab(self.data['quality'], self.data['difficulty'])
        
        # 히트맵 생성
        sns.heatmap(heatmap_data, annot=True, fmt='d', cmap='YlOrRd',
                   cbar_kws={'label': '도구 개수'})
        
        plt.title('품질-난이도 분포 히트맵', fontsize=16, fontweight='bold', pad=20)
        plt.xlabel('난이도 (0:쉬움, 1:보통, 2:어려움)')
        plt.ylabel('품질 (1:기본, 2:고급)')
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
    def create_recommendation_template(self, recommended_tools=None, save_path='charts/recommendation_result.png'):
        """추천 결과 시각화 템플릿"""
        if recommended_tools is None:
            # 샘플 추천 결과 (실제로는 model.py에서 받아올 데이터)
            recommended_tools = [
                {'name': 'ChatGPT 4.0', 'category': '텍스트', 'score': 0.95},
                {'name': 'Claude Opus', 'category': '텍스트', 'score': 0.88},
                {'name': 'Gemini 1.5', 'category': '텍스트', 'score': 0.82}
            ]
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # 1. 추천 점수 바 차트
        names = [tool['name'] for tool in recommended_tools]
        scores = [tool['score'] for tool in recommended_tools]
        
        bars = ax1.barh(names, scores, color=['#FF6B6B', '#4ECDC4', '#45B7D1'])
        ax1.set_xlabel('추천 점수')
        ax1.set_title('상위 추천 AI 도구', fontsize=14, fontweight='bold')
        ax1.set_xlim(0, 1)
        
        # 점수 표시
        for bar, score in zip(bars, scores):
            ax1.text(bar.get_width() - 0.05, bar.get_y() + bar.get_height()/2,
                    f'{score:.2f}', ha='right', va='center', 
                    fontweight='bold', color='white')
        
        # 2. 추천 도구 카테고리 분포
        categories = [tool['category'] for tool in recommended_tools]
        category_counts = Counter(categories)
        
        ax2.pie(category_counts.values(), labels=category_counts.keys(),
               autopct='%1.0f개', colors=self.colors[:len(category_counts)])
        ax2.set_title('추천 도구 카테고리 분포', fontsize=14, fontweight='bold')
        
        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        plt.show()
        
    def generate_all_visualizations(self):
        """모든 시각화 생성"""
        import os
        
        # charts 디렉토리 생성
        os.makedirs('charts', exist_ok=True)
        
        print("🎨 AI 도구 시각화 생성 중...")
        
        print("1. 카테고리 분포 차트 생성...")
        self.create_category_distribution()
        
        print("2. 난이도 분석 차트 생성...")
        self.create_difficulty_analysis()
        
        print("3. 사용자 타입 분석 차트 생성...")
        self.create_user_type_analysis()
        
        print("4. 품질-난이도 히트맵 생성...")
        self.create_quality_difficulty_heatmap()
        
        print("5. 추천 결과 템플릿 생성...")
        self.create_recommendation_template()
        
        print("✅ 모든 시각화 완료! charts/ 폴더를 확인하세요.")
        
    def get_data_summary(self):
        """데이터 요약 정보 반환"""
        summary = {
            'total_tools': len(self.data),
            'categories': self.data['category'].unique().tolist(),
            'difficulty_distribution': self.data['difficulty'].value_counts().to_dict(),
            'user_types': self.data['target_user'].unique().tolist(),
            'quality_distribution': self.data['quality'].value_counts().to_dict()
        }
        return summary

# 사용 예시
if __name__ == "__main__":
    # 시각화 객체 생성
    visualizer = AIToolVisualizer('ai_tools.csv')
    
    # 데이터 요약 정보 출력
    summary = visualizer.get_data_summary()
    print("📊 데이터 요약:")
    print(f"- 총 도구 개수: {summary['total_tools']}")
    print(f"- 카테고리: {summary['categories']}")
    print(f"- 사용자 타입: {summary['user_types']}")
    
    # 모든 시각화 생성
    visualizer.generate_all_visualizations()
import matplotlib.pyplot as plt

# ✅ 이건 VS Code에서 .py 파일 안에 작성
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

plt.plot([1, 2, 3], [10, 20, 30])
plt.title("한글 제목")
plt.show()
