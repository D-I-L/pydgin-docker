# pydgin-docker

This docker-compose repository defines and runs containers for pydgin 
(Django project), elasticsearch (document storage), postgres (user 
authentication) and NGINX (web-site server).

```
git clone https://github.com/D-I-L/pydgin-docker.git
cd pydgin-docker
mkdir elasticsearch/config/scripts
mkdir ./elasticsearch/esdata/
chmod a+rwx ./elasticsearch/esdata/
```

The directory elasticsearch/esdata/ is where the index files are stored
and this is mounted in the elasticsearch container. 

