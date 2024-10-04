#!/bin/bash
python pdf2csv.py
python replace_text.py
python classify_csv.py
python sort_csv.py
python csv2md.py
echo "done"
