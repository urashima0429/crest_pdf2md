import pdfplumber
import pandas as pd

target_pdf = "input.pdf"
output_folder = "raw_csv"

tables_info = {
    "summary": (2, 2),  # (開始ページ, 終了ページ)
    "papers": (3, 9),
    "presentations": (10, 13),
    "books": (14, 14),
    "awards": (15, 16),
    "media_coverage": (17, 17),
    "workshops": (18, 18)
}

def clean_cell(cell):
    """セル内のコンマの後に必ず半角スペースを追加し、改行を削除する"""
    if cell:
        cell = cell.replace('\n', '')
        cell = cell.replace(',', ', ')
        cell = ' '.join(cell.split())
    return cell

with pdfplumber.open(target_pdf) as pdf:
    for table_name, (start_page, end_page) in tables_info.items():
        all_tables = []
        header = None
        for page_number in range(start_page - 1, end_page):
            page = pdf.pages[page_number]
            table = page.extract_table()
            if table:
                if header is None:
                    header = [col.replace('\n', '') for col in table[0]]
                cleaned_rows = []
                for row in table[1:]:
                    cleaned_row = [clean_cell(cell) for cell in row]
                    cleaned_rows.append(cleaned_row)
                df = pd.DataFrame(cleaned_rows, columns=header)
                all_tables.append(df)

        if all_tables:
            combined_df = pd.concat(all_tables, ignore_index=True)
            combined_df.to_csv(f"{output_folder}/{table_name}.csv", index=False)
        else:
            print(f"No tables found for {table_name}")
