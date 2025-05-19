import pandas as pd
import os
from openai import OpenAI
import json

def analyze_excel_content(df):
    """AI를 사용하여 엑셀 내용을 분석하고 구조화된 데이터로 변환"""
    
    # 데이터프레임을 문자열로 변환
    content = df.to_string()
    
    # AI 프롬프트 구성
    prompt = f"""
    아래는 비주얼 노벨 게임의 시나리오 데이터입니다. 
    각 행을 분석하여 다음 형식의 JSON으로 변환해주세요:
    
    대사의 경우:
    {{
        "type": "dialogue",
        "speaker": "화자 이름",
        "expression": "표정 (있는 경우)",
        "position": "위치 (left/right/center)",
        "text": "대사 내용",
        "background": "배경 이미지 (변경되는 경우)",
        "effect": "효과 (있는 경우)"
    }}
    
    선택지/분기의 경우:
    {{
        "type": "choice",
        "choices": [
            {{
                "text": "선택지 텍스트",
                "result": "선택 결과",
                "jump_to": "이동할 레이블 (있는 경우)"
            }}
        ]
    }}
    
    분석할 내용:
    {content}
    """
    
    try:
        client = OpenAI()
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that analyzes visual novel scenario data and converts it to structured JSON format."},
                {"role": "user", "content": prompt}
            ],
            response_format={ "type": "json_object" }
        )
        
        # JSON 응답 파싱
        structured_data = json.loads(response.choices[0].message.content)
        return structured_data
        
    except Exception as e:
        print(f"AI 분석 중 오류 발생: {str(e)}")
        return None

def convert_to_structured_excel(structured_data):
    """구조화된 데이터를 새로운 엑셀 형식으로 변환"""
    
    # 대사용 데이터프레임
    dialogue_data = []
    # 선택지용 데이터프레임
    choice_data = []
    
    for item in structured_data['scenes']:
        if item['type'] == 'dialogue':
            dialogue_data.append({
                'Type': 'dialogue',
                'Speaker': item.get('speaker', ''),
                'Expression': item.get('expression', ''),
                'Position': item.get('position', ''),
                'Text': item.get('text', ''),
                'Background': item.get('background', ''),
                'Effect': item.get('effect', '')
            })
        elif item['type'] == 'choice':
            for choice in item.get('choices', []):
                choice_data.append({
                    'Type': 'choice',
                    'Choice_Text': choice.get('text', ''),
                    'Result': choice.get('result', ''),
                    'Jump_To': choice.get('jump_to', '')
                })
    
    # 데이터프레임 생성
    df_dialogue = pd.DataFrame(dialogue_data)
    df_choices = pd.DataFrame(choice_data)
    
    # 새로운 엑셀 파일 생성
    with pd.ExcelWriter('game/scripts/structured_scenario.xlsx') as writer:
        df_dialogue.to_excel(writer, sheet_name='Dialogues', index=False)
        df_choices.to_excel(writer, sheet_name='Choices', index=False)
    
    return True

def main():
    try:
        # 원본 엑셀 파일 읽기
        file_path = os.path.join('game', 'scripts', '찐 완성본.xlsx')
        df = pd.read_excel(file_path, sheet_name='챕터1', header=None)
        
        # AI 분석 수행
        print("AI로 시나리오 분석 중...")
        structured_data = analyze_excel_content(df)
        
        if structured_data:
            # 구조화된 엑셀 파일 생성
            print("구조화된 엑셀 파일 생성 중...")
            success = convert_to_structured_excel(structured_data)
            
            if success:
                print("변환 완료! structured_scenario.xlsx 파일이 생성되었습니다.")
                return True
    
    except Exception as e:
        print(f"오류 발생: {str(e)}")
        return False

if __name__ == '__main__':
    main() 