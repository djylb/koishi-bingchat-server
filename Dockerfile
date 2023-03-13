FROM phusion/baseimage:jammy-1.0.1
MAINTAINER D-Jy <duan@d-jy.net>

EXPOSE 8007

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

RUN echo 'APT::Get::Clean=always;' >> /etc/apt/apt.conf.d/99AutomaticClean

RUN apt-get update -qqy \
    && DEBIAN_FRONTEND=noninteractive apt-get -qyy install \
	--no-install-recommends \
	python3-venv \
	python3-dev \
	python3-lxml \
	python3-pip \
	libssl-dev \
	pkg-config \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY ./bing.py /srv/openchat/
COPY ./requirements.txt /srv/openchat/

RUN chown -R www-data:www-data /srv/openchat

# Setup openchat
WORKDIR /srv/openchat
RUN python3 -m venv venv && \
	. venv/bin/activate && \
 	pip3 install -U pip && \
	pip3 install wheel && \
	pip3 install --upgrade  -r requirements.txt && \
	pip3 cache purge && \
	chown -R www-data:www-data /srv/openchat

# Register services to runit
RUN mkdir /etc/service/bing
COPY conf/runit/bing.sh /etc/service/bing/run
RUN chmod a+x /etc/service/bing/run

# Define mountable directories.
#VOLUME []

WORKDIR /srv/openchat
