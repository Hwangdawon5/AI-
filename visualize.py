import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import platform

if platform.system() == 'Darwin':
    font_path = '/System/Library/Fonts/Supplemental/AppleGothic.ttf'  # Mac 한글 폰트 경로
    font_name = font_manager.FontProperties(fname=font_path).get_name()
    rc('font', family=font_name)

plt.rcParams['axes.unicode_minus'] = False

# 나머지 코드...
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 불러오기
df = pd.read_csv('ai_tools.csv')

# 시각화 1: 카테고리 분포
plt.figure(figsize=(8, 4))
sns.countplot(data=df, x='category')
plt.title('AI 도구 카테고리 분포')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('category_distribution.png')
plt.show()

# 시각화 2: 난이도 분포
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='difficulty')
plt.title('난이도 분포')
plt.tight_layout()
plt.savefig('difficulty_distribution.png')
plt.show()
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

class AIToolVisualizer:
    def __init__(self, csv_file):
        self.data = pd.read_csv(csv_file)
    
    def create_category_distribution(self):
        """카테고리별 도구 분포 차트 생성"""
        pass
    
    def create_difficulty_chart(self):
        """난이도별 분포 차트 생성"""
        pass
    
    def create_user_type_analysis(self):
        """사용자 타입별 분석 차트 생성"""
        pass
    
    def save_visualizations(self):
        """모든 시각화 결과를 이미지로 저장"""
        pass