import pandas as pd
import os

def analyze_row_type(row):
    """행의 타입을 분석"""
    # null이 아닌 값들만 추출
    values = [str(v).strip() for v in row if pd.notna(v)]
    if not values:
        return "empty"
    
    # 첫 번째 non-null 값으로 타입 판단
    first_value = values[0].lower()
    
    if "대사" in first_value:
        return "dialogue_header"
    elif any(keyword in str(row.values) for keyword in ["플레이", "미니게임", "선택"]):
        return "choice"
    elif values and not any(keyword in str(row.values) for keyword in ["플레이", "미니게임", "선택"]):
        return "dialogue"
    
    return "other"

def extract_dialogue_info(row):
    """대사 정보 추출"""
    values = [str(v).strip() for v in row if pd.notna(v)]
    if len(values) >= 2:
        return {
            'Type': 'dialogue',
            'Speaker': values[0],
            'Text': values[1],
            'Expression': values[2] if len(values) > 2 else '',
            'Position': 'left' if '왼쪽' in str(row.values) else 'right' if '오른쪽' in str(row.values) else 'center',
            'Background': '',
            'Effect': ''
        }
    return None

def extract_choice_info(row):
    """선택지 정보 추출"""
    values = [str(v).strip() for v in row if pd.notna(v)]
    if values:
        return {
            'Type': 'choice',
            'Choice_Text': values[0],
            'Result': values[1] if len(values) > 1 else '',
            'Jump_To': values[2] if len(values) > 2 else ''
        }
    return None

def parse_excel():
    try:
        # 엑셀 파일 읽기
        file_path = os.path.join('game', 'scripts', '찐 완성본.xlsx')
        df = pd.read_excel(file_path, sheet_name='챕터1', header=None)
        
        print("엑셀 파일 분석 중...")
        
        # 결과 저장용 리스트
        dialogues = []
        choices = []
        
        current_section = None
        for idx, row in df.iterrows():
            row_type = analyze_row_type(row)
            
            if row_type == "dialogue_header":
                current_section = "dialogue"
                print(f"대사 섹션 발견 - 행 {idx + 1}")
            
            elif row_type == "dialogue" and current_section == "dialogue":
                dialogue_info = extract_dialogue_info(row)
                if dialogue_info:
                    dialogues.append(dialogue_info)
                    print(f"대사 추출: {dialogue_info['Speaker']} - {dialogue_info['Text'][:20]}...")
            
            elif row_type == "choice":
                choice_info = extract_choice_info(row)
                if choice_info:
                    choices.append(choice_info)
                    print(f"선택지 추출: {choice_info['Choice_Text'][:20]}...")
            
            elif row_type == "empty":
                current_section = None
        
        # 결과를 엑셀로 저장
        with pd.ExcelWriter('game/scripts/structured_scenario.xlsx') as writer:
            pd.DataFrame(dialogues).to_excel(writer, sheet_name='Dialogues', index=False)
            pd.DataFrame(choices).to_excel(writer, sheet_name='Choices', index=False)
        
        print("\n변환 완료! structured_scenario.xlsx 파일이 생성되었습니다.")
        return True
        
    except Exception as e:
        print(f"오류 발생: {str(e)}")
        return False

if __name__ == '__main__':
    parse_excel() 