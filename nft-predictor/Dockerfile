FROM python:3.7

ENV PORT ${PORT}

WORKDIR /home/

RUN wget http://www.nano-editor.org/dist/v2.4/nano-2.4.2.tar.gz \
    && tar -xzf nano-2.4.2.tar.gz \
    && cd nano-2.4.2 \
    && ./configure \
    && make \
    && make install

WORKDIR /app
COPY . ./
RUN pip install -r req.txt

#EXPOSE 2020
VOLUME [ "/app/data" ]
RUN ["chmod", "+x", "/app/entrypoint.sh"]

CMD ["/app/entrypoint.sh"]