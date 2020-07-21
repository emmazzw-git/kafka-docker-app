# Kafka Docker App 

## Getting Started
* Spin up the Zookeeper, brokers and Kafka Monitoring UI using docker

```
docker-compose up
```

* List the docker container names

```bash
docker ps --format "{{ .Names }}"
```

> kafka-docker-app_kafka-web-ui_1
> kafka-docker-app_kafka-1_1
> kafka-docker-app_kafka-2_1
> kafka-docker-app_zookeeper_1

* Connect to the container of the Kafka broker

```bash
docker inspect --format='{{range $k, $v := .NetworkSettings.Ports}}{{range $v}}{{$k}} -> {{.HostIp}} {{.HostPort}}{{end}}{{end}}' kafka-docker-app_kafka-1_1
```

> 9092/tcp -> 0.0.0.0 9091

* Check the connection from the host to the single Kafka broker

```bash
nc -vz 0.0.0.0 9091
```

> found 0 associations
> found 1 connections:
    > 1:	flags=82<CONNECTED,PREFERRED>
	> outif lo0
	> src 127.0.0.1 port 58967
	> dst 127.0.0.1 port 9091
	> rank info not available
	> TCP aux info available

> Connection to 0.0.0.0 port 9091 [tcp/xmltec-xmlmail] succeeded!

* List the topics

```bash
docker exec -it kafka-docker-app_kafka-1_1 \
  kafka-topics.sh \
  --bootstrap-server :9092 \
  --list 
```

* Create topics

```bash
docker exec -it kafka-docker-app_kafka-1_1 \
  kafka-topics.sh \
    --bootstrap-server :9092 \
    --create \
    --topic payments-stream \
    --partitions 3 \
    --replication-factor 1
```

* Describe topics

```bash
docker exec -it kafka-docker-app_kafka-1_1 \
  kafka-topics.sh \
    --bootstrap-server :9092 \
    --describe \
    --topic payments-stream
```

* Delete topics

```bash
docker exec -it kafka-docker-app_kafka-1_1 \
  kafka-topics.sh \
    --bootstrap-server :9092 \
    --delete \
    --topic payments-stream
```

* Run and run app in docker

```bash
docker build -t kafka-app .
```

```bash
docker run -it --rm \
    --network kafka-docker-app_default \
    --name kafka-app kafka-app
```

* When scaling brokers, clear the existing volumes

```bash
docker volume prune
```




