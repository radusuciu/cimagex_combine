FROM ubuntu:latest

MAINTAINER Radu Suciu <radusuciu@gmail.com>

# Create user with non-root privileges
RUN adduser --disabled-password --gecos '' cimage
RUN chown -R cimage /home/cimage

# install some deps
RUN apt-get update && apt-get -y install python3-pip python3-venv

WORKDIR /home/cimage/cimagex_combine
USER cimage
CMD [ "/bin/bash", "/home/cimage/cimagex_combine/start.sh" ]