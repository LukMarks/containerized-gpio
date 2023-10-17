FROM raspbian/desktop
LABEL image="blink"
LABEL tag="latest"

WORKDIR /home

COPY requeriments.txt /home/
COPY blink.py /home/

RUN sudo mkdir /home/logs && sudo chmod 777 /home/logs
#RUN pip install -r /requeriments.txt

CMD ["python3", "blink.py"]
