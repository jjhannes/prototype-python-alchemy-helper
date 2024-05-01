
FROM python:3
WORKDIR /prototype-python-alchemy-helper
COPY . .
RUN pip install -r requirements.txt
CMD [ "python", "index.py" ]
EXPOSE 6668
