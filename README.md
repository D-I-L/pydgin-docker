# pydgin-docker

Notes for docker on MacOSX using docker-machine-nfs:

docker-machine create -d virtualbox  --virtualbox-memory 8096 dev-nfs
docker-machine-nfs dev-nfs
sudo vi /etc/exports 
sudo nfsd restart
eval "$(docker-machine env dev-nfs)"
docker-compose build
docker-compose up

