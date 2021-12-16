FROM python:3.9

RUN apt update && apt upgrade -y
RUN apt install python3-pip -y
