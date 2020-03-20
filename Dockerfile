FROM python:3.7

WORKDIR /usr/src/app
COPY requirements.txt ./
COPY server.py ./
COPY playwithme ./playwithme

EXPOSE 8080/tcp

ENTRYPOINT python
CMD ./server.py