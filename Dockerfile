FROM python:3.6
RUN mkdir -p /opt/autokeras
COPY requirements.txt /opt/autokeras/
WORKDIR /opt/autokeras
RUN pip install -r requirements.txt
COPY . /opt/autokeras/
RUN chmod +x start.sh
ENTRYPOINT ["./start.sh"]
CMD []
