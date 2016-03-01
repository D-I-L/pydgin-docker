FROM python:3.5-onbuild
RUN git clone https://github.com/D-I-L/pydgin.git
RUN sed -i '/^mod-wsgi==/ d' pydgin/requirements-dev.txt
RUN sed -i "s|'mod_wsgi.server',||" pydgin/pydgin/settings.py
RUN pip install --no-cache-dir -r pydgin/requirements.txt
RUN mkdir /usr/src/app/pydgin/log/
WORKDIR /usr/src/app/pydgin
