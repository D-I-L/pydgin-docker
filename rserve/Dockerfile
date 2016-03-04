FROM r-base:latest

RUN R -e "install.packages('Rserve', repos='http://cran.r-project.org')"
RUN R -e "source('https://bioconductor.org/biocLite.R'); biocLite('snpStats')"
RUN R -e "install.packages('data.table')"
RUN R -e "install.packages('rjson')"
ENV ROOT /usr/share/rserve/config/
RUN apt-get update && apt-get install -y procps vim libcurl4-gnutls-dev libxml2-dev
RUN apt-get install -y libmime-base64-urlsafe-perl libdigest-hmac-perl libdigest-sha-perl libssl-dev

USER www-data
EXPOSE 6311
