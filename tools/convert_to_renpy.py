import pandas as pd
import os

def convert_dialogue_to_renpy(row):
    """대사 행을 Ren'Py 코드로 변환"""
    code = []
    
    # 배경 변경
    if row['Background']:
        code.append(f"scene {row['Background']} with fade")
    
    # 캐릭터 표시
    if row['Speaker']:
        position = row['Position'] if row['Position'] else 'center'
        expression = f"_{row['Expression']}" if row['Expression'] else ''
        code.append(f"show {row['Speaker']}{expression} at {position}")
    
    # 대사
    if row['Text']:
        code.append(f"{row['Speaker']} \"{row['Text']}\"")
    
    # 캐릭터 숨기기
    if row['Speaker']:
        code.append(f"hide {row['Speaker']}{expression}")
    
    return '\n'.join(code)

def convert_choice_to_renpy(choices_group):
    """선택지 그룹을 Ren'Py 코드로 변환"""
    code = ["menu:"]
    
    for _, row in choices_group.iterrows():
        code.append(f"    \"{row['Choice_Text']}\":")
        if row['Result']:
            code.append(f"        \"{row['Result']}\"")
        if row['Jump_To']:
            code.append(f"        jump {row['Jump_To']}")
        else:
            code.append("        pass")
    
    return '\n'.join(code)

def generate_renpy_script():
    try:
        # 구조화된 엑셀 파일 읽기
        excel_path = 'game/scripts/structured_scenario.xlsx'
        df_dialogue = pd.read_excel(excel_path, sheet_name='Dialogues')
        df_choices = pd.read_excel(excel_path, sheet_name='Choices')
        
        # Ren'Py 스크립트 생성
        script = []
        
        # 레이블 시작
        script.append("label chapter1:")
        
        # 대사와 선택지 처리
        current_index = 0
        while current_index < len(df_dialogue):
            row = df_dialogue.iloc[current_index]
            
            if row['Type'] == 'dialogue':
                script.append(convert_dialogue_to_renpy(row))
            
            # 현재 위치에 해당하는 선택지가 있는지 확인
            choices_group = df_choices[df_choices['Scene_Index'] == current_index]
            if not choices_group.empty:
                script.append(convert_choice_to_renpy(choices_group))
            
            current_index += 1
        
        # 스크립트 파일 생성
        output_path = 'game/scripts/generated_script.rpy'
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n\n'.join(script))
        
        print(f"Ren'Py 스크립트가 생성되었습니다: {output_path}")
        return True
        
    except Exception as e:
        print(f"오류 발생: {str(e)}")
        return False

if __name__ == '__main__':
    generate_renpy_script() 