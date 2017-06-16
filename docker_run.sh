#!/bin/bash

docker run -d --name="arcus-admin" -h "arcus" ruo91/arcus
docker run -d --name="arcus-memcached-1" -p 11211:11211 -h "memcached-1" ruo91/arcus:memcached
docker run -d --name="arcus-memcached-2" -h "memcached-2" ruo91/arcus:memcached
docker run -d --name="arcus-memcached-3" -h "memcached-3" ruo91/arcus:memcached
docker run -d --name=mysql -p 3306:3306 --env MYSQL_ROOT_PASSWORD=password --env MYSQL_USER=reinose --env MYSQL_PASSWORD=password --env MYSQL_DATABASE=cs494 mysql:5.7
docker run -d --name=nbase-arc -p 6000:6000 hyeongseok05/nbase-arc
