FROM python:3

WORKDIR /usr/src/works

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ADD . .
ADD data.tar.gz .

CMD [ "python", "./random_forest.py" ]
