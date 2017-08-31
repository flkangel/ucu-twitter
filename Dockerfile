FROM ubuntu
RUN apt-get update
RUN apt-get install -y net-tools
RUN apt-get install -y iputils-ping
CMD bash

