FROM ubuntu:14.04
MAINTAINER Felipe Triana, ftrianakast@gmail.com

# Update
RUN apt-get update

# Install wget
RUN apt-get install -y wget

# Install latest R

RUN sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9
RUN sh -c 'echo "deb http://cran.rstudio.com/bin/linux/ubuntu trusty/" >> /etc/apt/sources.list'
RUN apt-get update
RUN sudo apt-get -y install r-base

# Important additional libraries
RUN apt-get install -y libcurl4-gnutls-dev
RUN apt-get install -y libxml2-dev
RUN apt-get install -y libmime-base64-urlsafe-perl libdigest-hmac-perl libdigest-sha-perl
RUN apt-get install -y libssl-dev


RUN R -e "install.packages('Rserve', repos='http://cran.r-project.org')"
RUN R -e "source('https://bioconductor.org/biocLite.R'); biocLite('snpStats')"
RUN R -e "install.packages('data.table', repos='http://cran.rstudio.com/')"
RUN R -e "install.packages('rjson', repos='http://cran.rstudio.com/')"
ENV ROOT /usr/share/rserve/config/
RUN apt-get update && apt-get install -y procps vim libcurl4-gnutls-dev libxml2-dev
RUN apt-get install -y libmime-base64-urlsafe-perl libdigest-hmac-perl libdigest-sha-perl libssl-dev

USER www-data
EXPOSE 6311
