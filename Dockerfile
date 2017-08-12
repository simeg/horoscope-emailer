FROM heroku/heroku:16

RUN apt-get update
RUN apt-get install -y \
    python-pip \
    python-dev \
    build-essential
RUN pip install --upgrade \
    pip \
    virtualenv

COPY src ./src
COPY requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt

CMD ["python", "/src/app.py"]
