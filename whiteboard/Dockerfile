FROM ubuntu:20.04

SHELL ["/bin/bash", "-c"]
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
  vim \
  python3 \
  python3-pip \
  iproute2 \
  curl \
  socat

RUN useradd -s /bin/bash -m app
RUN mkdir /app
WORKDIR /app

CMD exec sleep infinity

