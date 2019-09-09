FROM garawalid/autokeras:latest
RUN mkdir -p /opt/autokeras
WORKDIR /opt/autokeras
COPY requirements.txt /opt/autokeras/
RUN pip install -r requirements.txt
COPY . /opt/autokeras/
RUN chmod +x start.sh
ENTRYPOINT ["./start.sh"]
CMD []
