import pandas as pd
import os

input_dir = 'raw_csv'
output_dir = 'csv'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]
for file in csv_files:
    data = pd.read_csv(os.path.join(input_dir, file))
    file_base = os.path.splitext(file)[0]

    if "papers" in file_base:
        types = [
            '研究論文（学術雑誌）',
            '研究論文（会議録、プロシーディングス）',
            '研究論文（研究会、シンポジウム資料等）'
        ]
        regions = ['国内', '国際']

        for type in types:
            for region in regions:
                filtered_data = data[(data['論文種別'] == type) & (data['国内/国際'] == region)]
                filename = f"{file_base}_{type}_{region}.csv"
                filtered_data.to_csv(os.path.join(output_dir, filename), index=False, encoding='utf-8-sig')

    elif "presentations" in file_base:
        types = [
            '招待講演',
            '口頭発表',
            'ポスター・デモ'
        ]
        regions = ['国内', '国際']

        for type in types:
            for region in regions:
                filtered_data = data[(data['発表区分'] == type) & (data['国内/国際'] == region)]
                filename = f"{file_base}_{type}_{region}.csv"
                filtered_data.to_csv(os.path.join(output_dir, filename), index=False, encoding='utf-8-sig')
    
    elif "books" in file_base:
        types = [
            '書籍',
            '総説',
            'その他'
        ]
        for type in types:
            filtered_data = data[data['著作物種別'] == type]
            filename = f"{file_base}_{type}.csv"
            filtered_data.to_csv(os.path.join(output_dir, filename), index=False, encoding='utf-8-sig')
    
    elif "awards" in file_base or "media_coverage" in file_base or "workshops" in file_base:
        filename = f"{file_base}.csv"
        data.to_csv(os.path.join(output_dir, filename), index=False, encoding='utf-8-sig')
