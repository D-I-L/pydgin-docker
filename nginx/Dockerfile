FROM nginx
RUN rm /etc/nginx/conf.d/default.conf
RUN mkdir /etc/nginx/ssl/
ADD sites-enabled/pydgin.conf /etc/nginx/conf.d/

# add SSL certificate
RUN openssl req \
    -new \
    -newkey rsa:4096 \
    -days 365 \
    -nodes \
    -x509 \
    -subj "/C=UK/ST=Cambridge/L=Cambridge/O=Dis/CN=www.example.com" \
    -keyout /etc/nginx/ssl/nginx.key \
    -out /etc/nginx/ssl/nginx.crt

RUN ls -l /etc/nginx/ssl/