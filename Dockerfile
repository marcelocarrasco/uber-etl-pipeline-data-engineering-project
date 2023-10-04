FROM python:3.10

RUN apt-get install curl
RUN apt-get install apt-transport-https
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list | tee /etc/apt/sources.list.d/msprod.list

RUN apt-get update
ENV ACCEPT_EULA=y DEBIAN_FRONTEND=noninteractive
# RUN apt-get install mssql-tools unixodbc-dev -y

RUN apt-get update && apt-get install -y libaio1 wget unzip unixodbc

WORKDIR /opt/devtools

RUN export INSTALL_ON_LINUX=1; \
 python -m pip install xlwings psutil

RUN python -m pip install --upgrade pip

RUN python -m pip install \
		pandas==2.1.0 \
		pyodbc \
		sqlalchemy==2.0.20 \
		cx_Oracle \
    pyarrow==13.0.0

CMD ["python"]