FROM python:3.7

WORKDIR /home/

ENV API_KEY ${API_KEY}
ENV PORT ${PORT}

RUN wget http://www.nano-editor.org/dist/v2.4/nano-2.4.2.tar.gz \
    && tar -xzf nano-2.4.2.tar.gz \
    && cd nano-2.4.2 \
    && ./configure \
    && make \
    && make install

WORKDIR /app

COPY . ./

RUN pip install -r req.txt

EXPOSE 2020

CMD ["python", "/app/server.py"]