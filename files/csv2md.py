import csv
import os
from pathlib import Path
import pandas as pd

input_dir = 'csv'
output_dir = 'markdown'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]
for file in csv_files:
    data = pd.read_csv(os.path.join(input_dir, file))
    file_base = os.path.splitext(file)[0]

    output_file_path = Path(output_dir) / (file_base + '.md')

    if "papers" in file_base:
    # 成果発生年度,論文種別,国内/国際,タイトル,著者,掲載誌,DOI,発行年月日,掲載巻,掲載号,掲載開始ページ,掲載終了ページ,査読,論文ステータス区分,国際共著,備考
        with output_file_path.open('w', encoding='utf-8') as md_file:
            for index, row in data.iterrows():
                try:
                    citation = f"- {row['著者']}. {row['タイトル']}. {row['掲載誌']}. {row['成果発生年度']}."
                except KeyError as e:
                    error_message = f"Missing key in row {index + 1} in file {file}: {str(e)}"
                    raise ValueError(error_message)
                md_file.write(citation + "\n")

    if "presentations" in file_base:
    # 成果発生年度,発表区分,国内/国際,国際共著,タイトル,著者,会議名,DOI,発表年月日,掲載巻,掲載号,掲載開始ページ,掲載終了ページ,論文ステータス区分
        with output_file_path.open('w', encoding='utf-8') as md_file:
            for index, row in data.iterrows():
                try:
                    citation = f"- {row['著者']}. {row['タイトル']}. {row['会議名']}. {row['成果発生年度']}."
                except KeyError as e:
                    error_message = f"Missing key in row {index + 1} in file {file}: {str(e)}"
                    raise ValueError(error_message)
                md_file.write(citation + "\n")

    if "workshops" in file_base:
    # 成果発生年度,開催年月日,名称,場所,参加人数,概要,備考
        with output_file_path.open('w', encoding='utf-8') as md_file:
            for index, row in data.iterrows():
                try:
                    citation = f"- {row['名称']}. {row['場所']}. {row['開催年月日']}."
                except KeyError as e:
                    error_message = f"Missing key in row {index + 1} in file {file}: {str(e)}"
                    raise ValueError(error_message)
                md_file.write(citation + "\n")

    if "media_coverage" in file_base:
    # 成果発生年度,掲載メディア,タイトル,報道年月日,備考
        with output_file_path.open('w', encoding='utf-8') as md_file:
            for index, row in data.iterrows():
                try:
                    citation = f"- {row['掲載メディア']}. {row['タイトル']}. {row['成果発生年度']}."
                except KeyError as e:
                    error_message = f"Missing key in row {index + 1} in file {file}: {str(e)}"
                    raise ValueError(error_message)
                md_file.write(citation + "\n")

    if "books" in file_base:
        # 成果発生年度,著作物種別,タイトル,著者,掲載誌,DOI,発行年月日,備考
        with output_file_path.open('w', encoding='utf-8') as md_file:
            for index, row in data.iterrows():
                try:
                    if row['著作物種別'] == '書籍':
                        citation = f"- {row['著者']}. {row['タイトル']}. {row['成果発生年度']}."
                    elif row['著作物種別'] == '総説':
                        citation = f"- {row['著者']}. {row['タイトル']}. {row['掲載誌']}. {row['成果発生年度']}."
                    elif row['著作物種別'] == 'その他':
                        citation = f"- {row['著者']}. {row['タイトル']}. {row['成果発生年度']}."
                except KeyError as e:
                    error_message = f"Missing key in row {index + 1} in file {file}: {str(e)}"
                    raise ValueError(error_message)
                md_file.write(citation + "\n")

    if "award" in file_base:
        # 成果発生年度,受賞者名,受賞名,表彰団体名,国内/国際,受賞年月日,備考                    
        with output_file_path.open('w', encoding='utf-8') as md_file:
            for index, row in data.iterrows():
                try:
                    citation = f"- {row['受賞者名']}. {row['受賞名']}. {row['表彰団体名']}. {row['成果発生年度']}."
                except KeyError as e:
                    error_message = f"Missing key in row {index + 1} in file {file}: {str(e)}"
                    raise ValueError(error_message)
                md_file.write(citation + "\n")