FROM python:3.7.12-alpine3.15

RUN apk add py3-pip build-base
RUN pip install beautifulsoup4 requests

ADD src /app
ADD /startup.sh /

WORKDIR /app

CMD [ "/startup.sh"  ]


