# pydgin-docker

Notes for docker on MacOSX using docker-machine-nfs:
```
docker-machine create -d virtualbox --virtualbox-memory 8096 dev-nfs
docker-machine-nfs dev-nfs
sudo vi /etc/exports 
sudo nfsd restart
eval "$(docker-machine env dev-nfs)"
```

After connecting to the docker machine:
```
docker-compose build
docker-compose up postgres    # creates webuser role
docker stop $(docker ps -q)
docker-compose up
```

This assumes the elasticsearch indices are in ./elasticsearch/esdata/ on the host machine. Run 
the following command to find the IP address of the running nginx server:
```
docker-machine ip dev-nfs
```
