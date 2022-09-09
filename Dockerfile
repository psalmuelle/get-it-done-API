FROM python:3.8-alpine

ENV PATH="/scripts:${PATH}"

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers && apk add libffi-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp

RUN mkdir /slickAPI
COPY ./slickAPI /slickAPI
WORKDIR /slickAPI
COPY ./scripts /scripts

RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/static

RUN adduser -D user 
RUN chown -R user:user /vol
RUN chmod -R 777 /vol/web
USER user

CMD ["entrypoint.sh"]
