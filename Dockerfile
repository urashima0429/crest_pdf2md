FROM python:3.10-slim

WORKDIR /usr/src/app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

# docker build -t pdf2csv-image .
# docker run -it --rm --name pdf2csv-container -v ${PWD}/files:/usr/src/app/files pdf2csv-image bash
