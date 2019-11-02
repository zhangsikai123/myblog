FROM zhangsikai/skyblog:skyflask

MAINTAINER sikaizhang

RUN mkdir /app

ENV WORK_PATH /app

WORKDIR $WORK_PATH

ADD . .

EXPOSE 8000

RUN echo Hello Sikai

RUN python -v

RUN gunicorn -v

ENTRYPOINT ["gunicorn", "-b 0.0.0.0:80", "--access-logfile", "web.log", "web:app"]
