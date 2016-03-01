# pydgin-docker

Notes for docker on MacOSX using docker-machine-nfs:

```
docker-machine create -d virtualbox --virtualbox-memory 8096 dev-nfs
docker-machine-nfs dev-nfs
sudo vi /etc/exports 
sudo nfsd restart


eval "$(docker-machine env dev-nfs)"
docker-compose build
docker-compose up postgres    # creates webuser role
docker stop $(docker ps -q)
docker-compose up


docker-compose run pydgin /usr/local/bin/python manage.py collectstatic
docker-compose run pydgin /usr/local/bin/python manage.py makemigrations
docker-compose run pydgin /usr/local/bin/python manage.py migrate
docker-compose run pydgin /usr/local/bin/python manage.py migrate elastic
docker-compose run pydgin /usr/local/bin/python manage.py makemigrations elastic

```

