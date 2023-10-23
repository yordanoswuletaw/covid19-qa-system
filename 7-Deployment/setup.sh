# Download the clean dataset
wget https://storage.googleapis.com/haystack-qa/SAMPLE_COVID_QA_PROCESSED.csv

# The first docker command pulls the elasticsearch image from the docker hub
docker pull docker.elastic.co/elasticsearch/elasticsearch:7.13.4
# We are running elasticsearch docker and mapping the 9200 port of local server with the host server
docker run -p 9200:9200 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.13.4