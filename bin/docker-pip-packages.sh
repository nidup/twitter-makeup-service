#!/usr/bin/env bash

docker-compose run --rm cli echo '- installed packages'
docker-compose run --rm cli echo '----------------------------------------------------------------------'
docker-compose run --rm cli pip list
docker-compose run --rm cli echo '----------------------------------------------------------------------'
docker-compose run --rm cli echo '- show twitter makeup'
docker-compose run --rm cli echo '----------------------------------------------------------------------'
docker-compose run --rm cli pip show twitter-makeup
