version=`date "+%H-%M-%S_%d-%m-%y"`
echo $version
sudo docker build -t qa-api .
sudo docker tag qa-api us.gcr.io/annular-mercury-318319/qa-api:$version

sudo docker container prune -f
sudo docker image prune -f
sudo docker volume prune -f
sudo docker network prune -f

sudo docker push us.gcr.io/annular-mercury-318319/qa-api:$version

# sudo docker run -p 85:8080 qa-api -e ELASTIC_SEARCH_HOST='host.docker.internal' -e ELASTIC_SEARCH_PORT=9200