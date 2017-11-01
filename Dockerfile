FROM ubuntu
LABEL maintainer="flkangel@gmail.com"
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install requests
RUN pip3 install requests requests_oauthlib
RUN apt-get install -y net-tools
CMD bash
