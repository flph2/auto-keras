FROM garawalid/autokeras:latest
RUN mkdir -p /opt/autokeras
COPY requirements.txt /opt/autokeras/
WORKDIR /opt/autokeras
COPY . /opt/autokeras/
RUN pip install -r requirements.txt && chmod +x start.sh
ENTRYPOINT ["./start.sh"]
CMD []
