FROM ubuntu
MAINTAINER rclarkson
RUN apt-get update

RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y postgresql postgresql-contrib 
RUN apt-get install -y vim
RUN apt-get install -y python3-sqlalchemy python3-sqlalchemy-utils python3-psycopg2
RUN apt-get install -y python3-pandas
RUN apt-get install -y tree
RUN apt-get install -y curl
RUN apt-get install -y sqlite
RUN apt-get install -y wget
RUN apt-get install -y sudo
RUN apt-get install -y python3-matplotlib
RUN apt-get install -y python3-numpy
RUN pip3 install nose
RUN pip3 install seaborn

USER postgres
RUN /etc/init.d/postgresql start && psql --command "CREATE USER mimic_user WITH SUPERUSER PASSWORD 'mimic';" && createdb -O mimic_user mimicry_db

USER root
ADD pgpass /root/.pgpass
ADD psqlrc /root/.psqlrc
RUN chmod 0600 /root/.pgpass
WORKDIR /analysis
