FROM python:3.5-onbuild
RUN apt-get update && apt-get install -y git --no-install-recommends
RUN git clone https://github.com/D-I-L/pydgin.git gittmp
RUN mv gittmp/* .
RUN sed -i '/^mod-wsgi==/ d' requirements-dev.txt
RUN pip install --no-cache-dir -r requirements.txt
RUN cp pydgin/settings_secret.py.template pydgin/settings_secret.py
RUN mkdir /usr/src/app/log/
