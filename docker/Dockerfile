FROM debian:10-slim

LABEL image="blink"
LABEL tag="latest"

WORKDIR /home

RUN mkdir /home/logs && chmod 777 /home/logs

RUN apt update && apt install -y build-essential python3-pip
RUN pip3 install RPi.GPIO

COPY blink.py /home/


CMD ["python3", "blink.py"]
