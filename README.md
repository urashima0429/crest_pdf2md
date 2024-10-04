# Extracting achievements from a PDF file 
ベストエフォート．元がPDFファイルなので，スペースが結構消える．
`${PWD}/files`に元のpdfを置いてください．

## Setup

```
docker build -t pdf2csv-image .
docker run -it --rm --name pdf2csv-container -v ${PWD}/files:/usr/src/app/files pdf2csv-image bash
```

## Usage

```
cd /usr/src/app/files
python pdf2csv.py
python sort_csv.py
python csv2md.py
```

## Output
markdown file: `./files/markdown/*.md`

