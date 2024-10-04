import csv
import os
from pathlib import Path
import pandas as pd

input_dir = 'sorted_csv'
output_dir = 'markdown'
month_abbr = {
    1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr",
    5: "May", 6: "Jun", 7: "Jul", 8: "Aug",
    9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
}


if not os.path.exists(output_dir):
    os.makedirs(output_dir)

csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]
for file in csv_files:
    data = pd.read_csv(os.path.join(input_dir, file), dtype=str)
    file_base = os.path.splitext(file)[0]

    output_file_path = Path(output_dir) / (file_base + '.md')

    if "papers" in file_base:
        # 成果発生年度,論文種別,国内/国際,タイトル,著者,掲載誌,DOI,発行年月日,掲載巻,掲載号,掲載開始ページ,掲載終了ページ,査読,論文ステータス区分,国際共著,備考
        # 必ずある項目: 著者,タイトル,掲載誌,発行年月日,査読,論文ステータス区分,国際共著
        # データなしがある項目: DOI,掲載巻,掲載号,掲載開始ページ,掲載終了ページ,備考
        with output_file_path.open('w', encoding='utf-8') as md_file:
            for index, row in data.iterrows():
                try:
                    authors = row['著者']
                    title = row['タイトル']
                    journal = row['掲載誌']
                    date = row['発行年月日']
                    year, month, _ = date.split('/')
                    peer_reviewed = row['査読'] # '有' or '無'
                    # status = row['論文ステータス区分'] # published, in press, or accepted
                    # international_coauthorship = row['国際共著'] # '有' or '無'
                    
                    citation = f"-"
                    citation += f" {authors}."
                    citation += f" {title}."
                    citation += f" {journal}" 
                    if pd.notna(row['掲載巻']):
                        citation += f", {row['掲載巻']}"
                        if pd.notna(row['掲載号']):
                            citation += f", ({row['掲載号']})"
                            if pd.notna(row['掲載開始ページ']) and pd.notna(row['掲載終了ページ']):
                                citation += f", {row['掲載開始ページ']}-{row['掲載終了ページ']}."
                            else:
                                citation += f"."
                        else:
                            citation += f"."
                    else:
                        citation += f"."
                    if pd.notna(row['DOI']):
                        citation += f" DOI: {row['DOI']}."
                    if row['国内/国際'] == '国際':
                        citation += f" {month_abbr[int(month)]} {year}."
                    else:
                        citation += f" {year}年{int(month)}月."
                    if peer_reviewed == '有':
                        citation += f" (Peer-reviewed)."
                except KeyError as e:
                    error_message = f"Missing key in row {index + 1} in file {file}: {str(e)}"
                    raise ValueError(error_message)
                md_file.write(citation + "\n")

    if "presentations" in file_base:
        # 成果発生年度,発表区分,国内/国際,国際共著,タイトル,著者,会議名,DOI,発表年月日,掲載巻,掲載号,掲載開始ページ,掲載終了ページ,論文ステータス区分
        # 必ずある項目: 国際共著,タイトル,著者,会議名,発表年月日
        # データなしがある項目: DOI,掲載巻,掲載号,掲載開始ページ,掲載終了ページ,論文ステータス区分
        with output_file_path.open('w', encoding='utf-8') as md_file:
            for index, row in data.iterrows():
                try:
                    authors = row['著者']
                    title = row['タイトル']
                    conference = row['会議名']
                    date = row['発表年月日']
                    year, month, _ = date.split('/')
                    # international_coauthorship = row['国際共著'] # '有' or '無'

                    citation = f"-"
                    citation += f" {authors}."
                    citation += f" {title}."
                    citation += f" {conference}."
                    if row['国内/国際'] == '国際':
                        citation += f" {month_abbr[int(month)]} {year}."
                    else:
                        citation += f" {year}年{int(month)}月."
                except KeyError as e:
                    error_message = f"Missing key in row {index + 1} in file {file}: {str(e)}"
                    raise ValueError(error_message)
                md_file.write(citation + "\n")

    if "workshops" in file_base:
        # 成果発生年度,開催年月日,名称,場所,参加人数,概要,備考
        # 必ずある項目: 開催年月日,名称,場所,参加人数,概要
        # データなしがある項目: 備考
        with output_file_path.open('w', encoding='utf-8') as md_file:
            for index, row in data.iterrows():
                try:
                    date = row['開催年月日']
                    year, month, day = date.split('/')
                    citation = f"- {row['名称']}. {row['場所']}. {year}年{int(month)}月{int(day)}日."
                except KeyError as e:
                    error_message = f"Missing key in row {index + 1} in file {file}: {str(e)}"
                    raise ValueError(error_message)
                md_file.write(citation + "\n")

    if "media_coverage" in file_base:
    # 成果発生年度,掲載メディア,タイトル,報道年月日,備考
    # 必ずある項目: 掲載メディア,タイトル,報道年月日
    # データなしがある項目: 備考
        with output_file_path.open('w', encoding='utf-8') as md_file:
            for index, row in data.iterrows():
                try:
                    date = row['報道年月日']
                    year, month, _ = date.split('/')
                    citation = f"- {row['掲載メディア']}. {row['タイトル']}. {year}年{int(month)}月."
                except KeyError as e:
                    error_message = f"Missing key in row {index + 1} in file {file}: {str(e)}"
                    raise ValueError(error_message)
                md_file.write(citation + "\n")

    if "books" in file_base:
        # 成果発生年度,著作物種別,タイトル,著者,掲載誌,DOI,発行年月日,備考
        # 必ずある項目: タイトル,著者,発行年月日
        # データなしがある項目: DOI,掲載誌,備考
        with output_file_path.open('w', encoding='utf-8') as md_file:
            for index, row in data.iterrows():
                try:
                    date = row['発行年月日']
                    year, month, _ = date.split('/')
                    if row['著作物種別'] == '総説':
                        citation = f"- {row['著者']}. {row['掲載誌']}. {row['タイトル']}. {year}年{int(month)}月."
                    else:
                        citation = f"- {row['著者']}. {row['タイトル']}. {year}年{int(month)}月."
                except KeyError as e:
                    error_message = f"Missing key in row {index + 1} in file {file}: {str(e)}"
                    raise ValueError(error_message)
                md_file.write(citation + "\n")

    if "award" in file_base:
        # 成果発生年度,受賞者名,受賞名,表彰団体名,国内/国際,受賞年月日,備考
        # 必ずある項目: 受賞者名,受賞名,表彰団体名,受賞年月日
        # データなしがある項目: 備考 
        with output_file_path.open('w', encoding='utf-8') as md_file:
            for index, row in data.iterrows():
                try:
                    date = row['受賞年月日']
                    year, month, _ = date.split('/')
                    citation = f"- {row['受賞者名']}. {row['受賞名']}. {row['表彰団体名']}."
                    if row['国内/国際'] == '国際':
                        citation += f" {month_abbr[int(month)]} {year}."
                    else:
                        citation += f" {year}年{int(month)}月."
                except KeyError as e:
                    error_message = f"Missing key in row {index + 1} in file {file}: {str(e)}"
                    raise ValueError(error_message)
                md_file.write(citation + "\n")