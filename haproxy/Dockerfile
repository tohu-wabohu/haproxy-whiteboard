FROM haproxy:2.5.2-bullseye

USER root
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
  vim \
  iputils-ping \
  iproute2 \
  curl \
  procps

USER haproxy

ADD haproxy.cfg /usr/local/etc/haproxy/haproxy.cfg 

CMD exec haproxy -S 0.0.0.0:1234 -W -db -f /usr/local/etc/haproxy/haproxy.cfg
