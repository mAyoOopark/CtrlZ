import pandas as pd
import os

def analyze_row_type(row):
    """각 행의 타입을 분석"""
    # 모든 null이 아닌 값을 리스트로 변환
    values = [str(v).strip() for v in row if pd.notna(v)]
    
    if not values:  # 빈 행
        return "empty"
        
    # 대사 확인 (첫 번째 non-null 값이 "대사"인 경우)
    if "대사" in values[0]:
        return "dialogue_header"
        
    # 선택지/분기 확인
    if any(keyword in str(row.values) for keyword in ["플레이", "미니게임", "선택"]):
        return "choice"
        
    # 실제 대사인 경우 (dialogue_header 다음에 나오는 실제 대사)
    if values and not any(keyword in str(row.values) for keyword in ["플레이", "미니게임", "선택"]):
        return "dialogue"
        
    return "other"

def process_dialogue(row):
    """대사 행 처리"""
    values = [str(v).strip() for v in row if pd.notna(v)]
    if values:
        print(f"대사 발견: {values}")
    return values

def process_choice(row):
    """선택지/분기 행 처리"""
    values = [str(v).strip() for v in row if pd.notna(v)]
    if values:
        print(f"선택지 발견: {values}")
    return values

def read_scenario_file():
    try:
        # 엑셀 파일 경로
        file_path = os.path.join('game', 'scripts', '찐 완성본.xlsx')
        
        # 챕터1 시트 읽기 (헤더 없이)
        df = pd.read_excel(file_path, sheet_name='챕터1', header=None)
        
        print("=== 챕터1 시트 분석 ===")
        
        current_section = None
        for idx, row in df.iterrows():
            row_type = analyze_row_type(row)
            
            if row_type == "dialogue_header":
                current_section = "dialogue"
                print(f"\n[새로운 대사 섹션 시작] - 행 {idx + 1}")
            elif row_type == "choice":
                values = process_choice(row)
                print(f"[선택지/분기] - 행 {idx + 1}")
            elif row_type == "dialogue" and current_section == "dialogue":
                values = process_dialogue(row)
            elif row_type == "empty":
                current_section = None
                
        return True
        
    except Exception as e:
        print(f"오류 발생: {str(e)}")
        return False

if __name__ == '__main__':
    read_scenario_file() 