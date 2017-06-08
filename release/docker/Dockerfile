#Farmers Market Register on Ubuntu Linux 16.04

FROM ubuntu:16.04
MAINTAINER Rohith K Polishetty "rohith.polishetty@gmail.com"

#Base package setup
RUN apt-get update
RUN apt-get install -y git python python-dev vim
RUN ln -sf python2.7 python
RUN ln -sf python2.7-config python-config

# Create a non-root user for the FarmersMarket program
RUN /usr/sbin/useradd --create-home --home-dir /home/farmersmarket --shell /bin/bash farmersmarket

# Switch to farmersmarket user
USER farmersmarket

# Set home environment variable
ENV HOME /home/farmersmarket

# Clone Farmer's Market Repository from GitHub
WORKDIR /home/farmersmarket
RUN git clone https://github.com/rpolishetty/FarmersMarketRegister.git

#change the working directory to FarmersMarketRegister folder
WORKDIR /home/farmersmarket/FarmersMarketRegister

