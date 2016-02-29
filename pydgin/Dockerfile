FROM python:3.5-onbuild
RUN git clone https://github.com/D-I-L/pydgin.git gittmp
RUN mv gittmp/* .
RUN sed -i '/^mod-wsgi==/ d' requirements-dev.txt
RUN sed -i "s|'mod_wsgi.server',||" pydgin/settings.py
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir /usr/src/app/log/
