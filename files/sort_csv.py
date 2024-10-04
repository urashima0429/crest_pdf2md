import pandas as pd
import os

input_dir = 'classified_csv'
output_dir = 'sorted_csv'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

csv_files = [f for f in os.listdir(input_dir) if f.endswith('.csv')]

for file in csv_files:
    data = pd.read_csv(os.path.join(input_dir, file), dtype=str)

    file_base = os.path.splitext(file)[0]

    if "papers" in file_base:
        date_column = '発行年月日'
    elif "presentations" in file_base:
        date_column = '発表年月日'
    elif "workshops" in file_base:
        date_column = '開催年月日'
    elif "media_coverage" in file_base:
        date_column = '報道年月日'
    elif "books" in file_base:
        date_column = '発行年月日'
    elif "awards" in file_base:
        date_column = '受賞年月日'
    else:
        raise ValueError(f"Unknown file type: {file_base}")

    data['temp_sort_date'] = pd.to_datetime(data[date_column], format='%Y/%m/%d', errors='coerce')
    sorted_data = data.sort_values(by='temp_sort_date', ascending=False)
    sorted_data.drop(columns=['temp_sort_date'], inplace=True)
    sorted_data.to_csv(os.path.join(output_dir, f"{file_base}.csv"), index=False, encoding='utf-8-sig')

