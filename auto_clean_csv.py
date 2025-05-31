import pandas as pd

def clean_ai_tools_csv(input_path='ai_tools.csv', output_path='cleaned_ai_tools.csv'):
    """
    ai_tools.csv 파일을 전처리하여 cleaned_ai_tools.csv로 저장합니다.
    - 중복 제거
    - 필수 컬럼(tool_name, category) 결측값 제거
    - 문자열 정리
    """
    df = pd.read_csv(input_path)

    # 1. 중복 제거
    df.drop_duplicates(inplace=True)

    # 2. 필수 컬럼 누락 행 제거
    df.dropna(subset=['tool_name', 'category'], inplace=True)

    # 3. 문자열 컬럼 정리
    df['tool_name'] = df['tool_name'].astype(str).str.strip()
    df['category'] = df['category'].astype(str).str.strip().str.lower()
    df['target_user'] = df['target_user'].astype(str).str.strip()

    # 4. 저장
    df.to_csv(output_path, index=False)
    print(f"✅ 전처리 완료! → {output_path}로 저장되었습니다.")

if __name__ == "__main__":
    clean_ai_tools_csv()
