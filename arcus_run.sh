#!/bin/bash

docker run -d --name="arcus-admin" -h "arcus" ruo91/arcus
docker run -d --name="arcus-memcached-1" -h "memcached-1" ruo91/arcus:memcached
docker run -d --name="arcus-memcached-2" -h "memcached-2" ruo91/arcus:memcached
docker run -d --name="arcus-memcached-3" -h "memcached-3" ruo91/arcus:memcached
