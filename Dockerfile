FROM python:3.7

WORKDIR /usr/src/app
COPY requirements.txt ./
COPY server.py ./
COPY playwithme ./playwithme


RUN pip install -r requirements.txt
RUN pip install psycopg2-binary

EXPOSE 8080/tcp
ENTRYPOINT python
CMD ./server.py