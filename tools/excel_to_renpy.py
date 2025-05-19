import pandas as pd
import os

def convert_dialogue(df_dialogue):
    script = []
    current_scene = None
    
    for _, row in df_dialogue.iterrows():
        # Scene change
        if row['Background'] and row['Background'] != '-':
            script.append(f"scene {row['Background']} with fade\n")
            
        # Character display
        if row['Speaker'] and row['Expression'] != '-':
            position = row['Position'] if row['Position'] != '-' else ''
            script.append(f"show {row['Speaker']}_{row['Expression']} at {position}")
            
        # Dialogue
        if row['Dialogue']:
            script.append(f"{row['Speaker']} \"{row['Dialogue']}\"")
            
        # Hide character
        if row['Speaker']:
            script.append(f"hide {row['Speaker']}_{row['Expression']}\n")
            
        # Jump
        if row['Jump To'] and row['Jump To'] != '-':
            script.append(f"jump {row['Jump To']}")
            
    return '\n'.join(script)

def convert_choices(df_choices):
    script = []
    current_scene = None
    
    for scene_id in df_choices['Scene ID'].unique():
        scene_choices = df_choices[df_choices['Scene ID'] == scene_id]
        script.append(f"menu:")
        
        for _, choice in scene_choices.iterrows():
            script.append(f"    \"{choice['Choice Text']}\":")
            
            # Life change
            if choice['Life Change'] != 0:
                script.append(f"        $ wrong_count += {abs(choice['Life Change'])}")
                
            # Result text
            if choice['Result']:
                script.append(f"        \"{choice['Result']}\"")
                
            # Jump
            if choice['Jump To']:
                script.append(f"        jump {choice['Jump To']}")
                
    return '\n'.join(script)

def main():
    # Read Excel sheets
    df_dialogue = pd.read_excel('scenario.xlsx', sheet_name='Dialogue')
    df_choices = pd.read_excel('scenario.xlsx', sheet_name='Choices')
    df_variables = pd.read_excel('scenario.xlsx', sheet_name='Variables')
    df_assets = pd.read_excel('scenario.xlsx', sheet_name='Assets')
    
    # Generate script
    script = []
    
    # Add variables
    for _, var in df_variables.iterrows():
        script.append(f"default {var['Variable Name']} = {var['Initial Value']}")
    
    # Add assets
    for _, asset in df_assets.iterrows():
        if asset['Asset Type'] == 'background':
            script.append(f"image {asset['File Name']} = \"{asset['File Name']}.png\"")
    
    # Add dialogue and choices
    script.extend(convert_dialogue(df_dialogue))
    script.extend(convert_choices(df_choices))
    
    # Write to file
    with open('game/scripts/generated_script.rpy', 'w', encoding='utf-8') as f:
        f.write('\n'.join(script))

if __name__ == '__main__':
    main() 