docker run -d -p 9092:9092 apache/kafka:4.1.0
docker network create elastic-network
docker run --name elasticsearch --net elastic-network -p 9200:9200  -e "discovery.type=single-node" -e "xpack.security.enabled=false" docker.elastic.co/elasticsearch/elasticsearch:9.1.3  # Replace 8.x.x with desired version
docker run --name kibana --net elastic-network \
      -p 5601:5601 \
      -e "ELASTICSEARCH_HOSTS=http://elasticsearch:9200" \
      docker.elastic.co/kibana/kibana:9.1.3  # Replace 8.x.x with desired version
docker run -d --name my-mongodb -p 27017:27017 mongo