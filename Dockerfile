FROM python:3

ENV PYTHONIOENCODING UTF-8
ENV TZ=Asia/Almata

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

RUN mkdir static && mkdir media

COPY . .

EXPOSE 8000
